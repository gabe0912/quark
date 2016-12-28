from .match import match, choice
from .errors import Errors, DuplicateSymbol, MissingSymbol
from .ast import (
    AST, File, Class, Method, Name, Block, Interface
)
from .parse import (
    parse, traversal, ParseError, wire
)
from .symbols import Symbols, depackage
from .types import Types
from .code import Code
from .traits import COMPILER

import stats

class Compiler(object):

    MATCH_TRAITS = COMPILER

    def __init__(self, package_name="pkg", verbose=0):
        self.errors = Errors()
        self.symbols = Symbols()
        self.types = Types(self.symbols)
        self.code = Code(self.symbols, self.types, package_name)
        self.files = []

    @match(basestring, basestring)
    def parse(self, name, content):
        try:
            with stats.charge("parse"):
                file = parse(name, content)
        except ParseError, e:
            self.errors.add(e)
            return

        with stats.charge("desugar"):
            for node in traversal(file):
                self.desugar(node)

        self.load(file)
        return file

    @match(File)
    def load(self, file):
        self.files.append(file)

    @match(Class)
    def desugar(self, cls):
        cons = [d for d in cls.definitions if isinstance(d, Method) and not d.type]
        if not cons:
            default = Method(None, Name(cls.name.text), (), Block([]))
            cls.definitions.append(default)
            wire(cls, default)

    # XXX: should Primitives have constructors?
    @match(choice(Interface, AST))
    def desugar(self, _):
        pass

    @match()
    def check_symbols(self):
        self.errors.check()

        # define symbols
        with stats.charge("define-symbols"):
            for file in self.files:
                for node in traversal(file):
                    if self.symbols.is_definition(node):
                        self.symbols.define(node)

        # resolve symbols
        with stats.charge("resolve-symbols"):
            for file in self.files:
                for n in traversal(file):
                    if self.symbols.is_usage(n):
                        self.symbols.resolve(n)

        for sym, nodes in self.symbols.duplicates.items():
            prev = depackage(self.symbols.definitions[sym])
            for n in nodes:
                self.errors.add(DuplicateSymbol(n, sym, prev))

        for nd, name in self.symbols.missing.items():
            self.errors.add(MissingSymbol(nd, name))

    @match()
    def check_types(self):
        self.errors.check()

        # define types
        with stats.charge("define-types"):
            for k, v in self.symbols.definitions.items():
                if self.types.is_type(v):
                    self.types.define(v)

        # resolve types
        visited = set()
        with stats.charge("resolve-types"):
             for k, v in self.symbols.definitions.items():
                 for node in traversal(v):
                     if node in visited:
                         break
                     else:
                         visited.add(node)
                     if self.types.has_type(node):
                         self.types.resolve(node)

        for n, errs in self.types.violations.items():
            for e in errs:
                self.errors.add(e)
        for err in self.types.unresolved:
            self.errors.add(err)

    @match()
    def check(self):
        self.check_symbols()
        self.check_types()
        self.errors.check()

    @match()
    def compile(self):
        with stats.charge("compile"):
            pkg = self.code.compile()
            return pkg
