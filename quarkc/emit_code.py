# Copyright 2015 datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .match import match, opt, choice, many
from .ir import (IR, Function, Interface, Class, Check, If,
                 While, Block, Evaluate, Local, Assign, Return, Set,
                 Message, Field, Method, Constructor, AssertEqual,
                 Null)
from . import tr

from .emit_target import Target, Python, Ruby, Java, Go, Javascript
from .emit_expr import expr
from .emit_ir import TestClass, TestMethod

@match(basestring, IR, Target, opt(basestring))
def opt_expr(glue, nd, target, default=""):
    return "{glue}{expr}".format(
        glue=glue, expr=expr(nd, target))

@match(basestring, None, Target, opt(basestring))
def opt_expr(glue, nd, target, default=""):
    return default

## Function

@match(Function, Python)
def code(fun, target):
    return tr.Compound(
        "def {name}({params})".format(
            name=target.nameof(fun.name),
            params=", ".join(expr(p, target) for p in fun.params)),
        code(fun.body, target))

@match(Check, Python)
def code(fun, target):
    return tr.Compound(
        "def test_{name}()".format(
            name=target.nameof(fun.name)),
        code(fun.body, target)
    )

@match(TestMethod, Python)
def code(fun, target):
    return tr.Compound(
        "def test_{name}(self)".format(
            name=fun.name),
        code(fun.body, target)
    )

@match(Function, Java)
def code(fun, target):
    return tr.Compound(
        "public static {type} {name}({params})".format(
            type=expr(fun.type, target),
            name=target.nameof(fun.name),
            params=", ".join(expr(p, target) for p in fun.params)),
        code(fun.body, target)
    )

@match(Check, Java)
def code(fun, target):
    return tr.Compound(
        "@Test\npublic void {name}()".format(
            name=target.nameof(fun.name)),
        code(fun.body, target)
    )

@match(TestMethod, Java)
def code(fun, target):
    return tr.Compound(
        "@Test\npublic void test_{name}()".format(
            name=fun.name),
        code(fun.body, target)
    )

@match(Function, Ruby)
def code(fun, target):
    return tr.Compound(
        "def self.{name}({params})".format(
            name=target.nameof(fun.name),
            params=", ".join(expr(p, target) for p in fun.params)),
        code(fun.body, target)
    )

@match(TestMethod, Ruby)
def code(fun, target):
    return tr.Compound(
        "def test_{name}".format(
            name=fun.name),
        code(fun.body, target)
    )

@match(Function, Go)
def code(fun, target):
    return tr.Compound(
        "func {name}({params}) {type}".format(
            type=expr(fun.type, target),
            name=target.nameof(fun.name),
            params=", ".join(expr(p, target) for p in fun.params)),
        code(fun.body, target)
    )

@match(Check, Go)
def code(fun, target):
    return tr.Compound(
        "func TestQ_{name}(t__ *testing.T)".format(
            name=target.upcase(fun.name.path[-1])),
        code(fun.body, target)
    )

@match(TestMethod, Go)
def code(fun, target):
    return tr.Compound(
        "func TestQ_{name}(t__ *testing.T)".format(
            name=target.upcase(fun.name)),
        code(fun.body, target)
    )

@match(Function, Javascript)
def code(fun, target):
    return tuple((
        tr.Compound(
            "function {name}({params})".format(
                name=target.nameof(fun.name),
                params=", ".join(expr(p, target) for p in fun.params)),
            code(fun.body, target)),
        tr.Simple("module.exports = {name}".format(
                name=target.nameof(fun.name)))
        ))

@match(TestMethod, Javascript)
def code(fun, target):
    return tr.Compound(
        "it('{name}', function()".format(
            name=fun.name),
        tr.Block(
            *[code(s, target) for s in fun.body.statements],
            extra_close = ")"
        )
    )
## If

@match(If, Target)
def code(if_, target):
    return tr.Compound(
        "if ({predicate})".format(predicate=expr(if_.predicate, target)),
        code(if_.consequence, target),
        "else",
        code(if_.alternative, target))

## While

@match(While, Target)
def code(wh, target):
    return tr.Compound(
        "while ({predicate})".format(
            predicate=expr(wh.predicate, target)),
        code(wh.body, target)
    )

@match(While, Go)
def code(wh, target):
    return tr.Compound(
        "for ({predicate})".format(
            predicate=expr(wh.predicate, target)),
        code(wh.body, target)
    )

## Blocks

@match(Block, Target)
def code(block, target):
    return tr.Block(*[code(s, target) for s in block.statements])

## Evaluate

@match(Evaluate, Target)
def code(evaluate, target):
    return tr.Simple("{expr}".format(
        expr=expr(evaluate.expr, target)))

## Return

@match(Return, Target)
def code(retr, target):
    return tr.Simple("return {expr}".format(
        expr=expr(retr.expr, target)))

## Local

@match(Local, choice(Python, Ruby))
def code(local, target):
    return tr.Simple("{name}{initializer}".format(
        name=local.name,
        initializer=opt_expr(" = ", local.expr or Null(local.type), target)))

@match(Local, Java)
def code(local, target):
    return tr.Simple("{type} {name}{initializer}".format(
        name=local.name,
        type=expr(local.type, target),
        initializer=opt_expr(" = ", local.expr, target)))

@match(Local, Go)
def code(local, target):
    return tr.Simple("var {name} {type}{initializer}".format(
        name=local.name,
        type=expr(local.type, target),
        initializer=opt_expr(" = ", local.expr, target)))

@match(Local, Javascript)
def code(local, target):
    return tr.Simple("let {name}{initializer}".format(
        name=local.name,
        initializer=opt_expr(" = ", local.expr, target)))

## Assign

@match(Assign, Target)
def code(ass, target):
    return tr.Simple("{name} = {value}".format(
        name=ass.lhs.name,
        value=expr(ass.rhs, target)))

## Set

@match(Set, Go)
def code(fset, target):
    return tr.Simple("{target}.{field} = {value}".format(
        target=expr(fset.expr, target),
        field=target.upcase(fset.name),
        value=expr(fset.value, target)))

@match(Set, choice(Python, Java, Javascript))
def code(fset, target):
    return tr.Simple("{target}.{field} = {value}".format(
        target=expr(fset.expr, target),
        field=fset.name,
        value=expr(fset.value, target)))

@match(Set, Ruby)
def code(fset, target):
    return tr.Simple("{target}.{field} = {value}".format(
        target=expr(fset.expr, target),
        field=fset.name,
        value=expr(fset.value, target)))

## Interface

@match(Interface, Python)
def code(iface, target):
    methods = [code(m, target) for m in iface.methods]
    return tr.Compound(
        "class {name}(object)".format(
            name = target.nameof(iface.name)),
        tr.Block(*methods))

@match(Interface, Ruby)
def code(iface, target):
    return tr.Compound(
        "class {name}".format(
            name = target.nameof(iface.name)),
        tr.Block(*[code(m, target) for m in iface.methods]))

@match(Interface, Java)
def code(iface, target):
    return tr.Compound(
        "public interface {name}".format(
            name = target.nameof(iface.name)),
        tr.Block(*[code(m, target) for m in iface.methods]))

@match(Interface, Go)
def code(iface, target):
    return tr.Compound(
        "type {name} interface".format(
            name = target.nameof(iface.name)),
        tr.Block(*[code(m, target) for m in iface.methods]))

@match(Interface, Javascript)
def code(iface, target):
    return tr.flattened(tuple((
        tr.Comment("interface"),
        tr.Compound(
            "function {name}()".format(
                name = target.nameof(iface.name)),
            tr.Block(
            )),
        tr.Simple("module.exports = {name}".format(
                name = target.nameof(iface.name))),
    )) + tuple(code(m, target) for m in iface.methods))

## Message

@match(Message, Python)
def code(fun, target):
    return tr.Simple("def {name}({params}): pass".format(
        name=fun.name,
        params=", ".join(expr(p, target) for p in fun.params)
    ))

@match(Message, Java)
def code(fun, target):
    return tr.Simple("public {type} {name}({params})".format(
        type=expr(fun.type, target),
        name=fun.name,
        params=", ".join(expr(p, target) for p in fun.params)
    ))

@match(Message, Ruby)
def code(fun, target):
    return tr.Compound(
        "def {name}({params})".format(
            name=fun.name,
            params=", ".join(expr(p, target) for p in fun.params)),
        tr.Block())

@match(Message, Go)
def code(fun, target):
    return tr.Simple(
        "{name}({params}) {type}".format(
            type=expr(fun.type, target),
            name=target.upcase(fun.name),
            params=", ".join(expr(p, target) for p in fun.params)
    ))

@match(Message, Javascript)
def code(fun, target):
    return tr.Compound(
        "{parent}.prototype.{name} = function({params})".format(
            parent = target.nameof(target.q.parent(fun)),
            name=fun.name,
            params=", ".join(expr(p, target) for p in fun.params)),
        tr.Block(
            tr.Simple("throw Error('abstract')")
        )
    )

## Class

@match(Class, Python)
def code(clazz, target):
    # XXX: do we want to support isinstance for implemented interfaces?
    return tr.Compound(
        "class {name}(object)".format(
            name = target.nameof(clazz.name)),
        tr.Block(*[code(m, target) for m in clazz.constructors + clazz.methods])
        )

@match(TestClass, Python)
def code(clazz, target):
    return tr.Compound(
        "class TestQ{name}(object)".format(
            name = target.nameof(clazz.name)),
        tr.Block(*[code(m, target) for m in clazz.constructors + clazz.methods])
        )

@match(Class, Ruby)
def code(clazz, target):
    return tr.Compound(
        "class {name}".format(
            name = target.nameof(clazz.name)),
        tr.Block(tuple([code(m, target) for m in clazz.fields + clazz.constructors + clazz.methods]))
        )

@match(TestClass, Ruby)
def code(clazz, target):
    return tr.Compound(
        "class {name} < Test::Unit::TestCase".format(
            name = target.nameof(clazz.name)),
        tr.Block(tuple([code(m, target) for m in clazz.fields + clazz.constructors + clazz.methods]))
        )

@match(Class, Java)
def code(clazz, target):
    return tr.Compound(
        "public class {name}{implements}".format(
            name = target.nameof(clazz.name),
            implements = implements("implements", clazz, target)),
        tr.Block(tuple([code(m, target) for m in clazz.fields + clazz.constructors + clazz.methods]))
        )

@match(TestClass, Java)
def code(clazz, target):
    return tr.Compound(
        "public class {name}".format(
            name = target.nameof(clazz.name)),
        tr.Block(tuple([code(m, target) for m in clazz.fields + clazz.constructors + clazz.methods]))
        )

@match(Class, Javascript)
def code(clazz, target):
    return tr.flattened(tuple((
        tr.Comment("class"),
    )) + tuple(code(m, target) for m in clazz.constructors + clazz.methods))

@match(TestClass, Javascript)
def code(clazz, target):
    return tr.flattened(tuple([code(m, target) for m in clazz.fields + clazz.constructors + clazz.methods]))

@match(basestring, choice(Class, Interface), Java)
def implements(keyword, clazz, target):
    if not clazz.implements:
        return ""
    return " {keyword} {interfaces}".format(
        keyword = keyword,
        interfaces = ", ".join(expr(i, target) for i in clazz.implements))

@match(Class, Go)
def code(clazz, target):
    return tuple(
        [tr.Compound(
            "type {name} struct".format(
                name = target.nameof(clazz.name)),
            tr.Block(tuple([code(m, target) for m in clazz.fields])))] +
        [code(m, target) for m in clazz.constructors + clazz.methods]
    )

## Field

@match(Field, Java)
def code(field, target):
    return tr.Simple("public {type} {name}".format(
        type=expr(field.type, target),
        name=field.name,
    ))

@match(Field, Ruby)
def code(field, target):
    return tr.Simple("attr_accessor :{name}".format(
        name=field.name,
    ))

@match(Field, Go)
def code(field, target):
    return tr.Simple("{name} {type}".format(
        name=target.upcase(field.name),
        type=expr(field.type, target),
    ))

## Method

@match(Method, Python)
def code(method, target):
    return tr.Compound(
        "def {name}({params})".format(
            name=method.name,
            params=", ".join(["self"] + [expr(p, target) for p in method.params])),
        code(method.body, target)
    )

@match(Method, Java)
def code(method, target):
    return tr.Compound(
        "public {type} {name}({params})".format(
            type=expr(method.type, target),
            name=method.name,
            params=", ".join(expr(p, target) for p in method.params)),
        code(method.body, target)
    )

@match(Method, Ruby)
def code(method, target):
    return tr.Compound(
        "def {name}({params})".format(
            name=method.name,
            params=", ".join(expr(p, target) for p in method.params)),
        code(method.body, target)
    )

@match(Method, Go)
def code(method, target):
    return tr.Compound(
        "func (this *{clazz}) {name}({params}) {type}".format(
            clazz=target.nameof(target.q.parent(method)),
            type=expr(method.type, target),
            name=target.upcase(method.name),
            params=", ".join(expr(p, target) for p in method.params)),
        code(method.body, target)
    )

@match(Method, Javascript)
def code(method, target):
    return tr.Compound(
        "{parent}.prototype.{name} = function({params})".format(
            parent = target.nameof(target.q.parent(method)),
            name=method.name,
            params=", ".join(expr(p, target) for p in method.params)),
        code(method.body, target)
    )


## Constructor

@match(Constructor, Python)
def code(constructor, target):
    return tr.Compound(
        "def __init__({params})".format(
            name=constructor.name,
            params=", ".join(["self"] + [expr(p, target) for p in constructor.params])),
        code(constructor.body, target)
    )

@match(Constructor, Java)
def code(constructor, target):
    return tr.Compound(
        "public {name}({params})".format(
            name=constructor.name,
            params=", ".join(expr(p, target) for p in constructor.params)),
        code(constructor.body, target)
    )

@match(Constructor, Ruby)
def code(constructor, target):
    return tr.Compound(
        "def initialize({params})".format(
            params=", ".join(expr(p, target) for p in constructor.params)),
        code(constructor.body, target)
    )

@match(Constructor, Go)
def code(constructor, target):
    clazz=target.nameof(target.q.parent(constructor))
    return tr.Compound(
        "func {name}__Construct({params}) *{clazz}".format(
            clazz=clazz,
            name=expr(constructor.type.name, target),
            params=", ".join(expr(p, target) for p in constructor.params)),
        tr.Block(
            tr.Simple("this := new({clazz})".format(clazz=clazz)),
            tr.Compound("", code(constructor.body, target)),
            tr.Simple("return this"))
        )

@match(Constructor, Javascript)
def code(constructor, target):
    clazz = target.nameof(target.q.parent(constructor))
    return tuple((
        tr.Compound(
            "function {name}({params})".format(
                name=clazz,
                params=", ".join(expr(p, target) for p in constructor.params)),
            code(constructor.body, target)
        ),
        tr.Simple("module.exports = {name}".format(
            name = clazz)),
        ))

## AssertEqual

@match(AssertEqual, Go)
def code(assrt, target):
    return tr.Compound("", tr.Block(
        tr.Simple("expected, actual := ({expected}), ({actual})".format(
            expected = expr(assrt.expected, target),
            actual = expr(assrt.actual, target))),
        tr.Simple("if (expected != actual) { t__.Error(expected, actual) }")))

@match(AssertEqual, Python)
def code(assrt, target):
    return tr.Simple("assert ({expected}) == ({actual})".format(
        expected = expr(assrt.expected, target),
        actual = expr(assrt.actual, target)))

@match(AssertEqual, Java)
def code(assrt, target):
    return tr.Simple("assertEquals(({expected}), ({actual}))".format(
        expected = expr(assrt.expected, target),
        actual = expr(assrt.actual, target)))

@match(AssertEqual, Ruby)
def code(assrt, target):
    return tr.Simple("assert_equal(({expected}), ({actual}))".format(
        expected = expr(assrt.expected, target),
        actual = expr(assrt.actual, target)))

@match(AssertEqual, Javascript)
def code(assrt, target):
    return tr.Simple("assert.strictEqual(({expected}), ({actual}))".format(
        expected = expr(assrt.expected, target),
        actual = expr(assrt.actual, target)))


###
### NOTE NOTE NOTE: this must be at the end of `code` definitions
###

orig_code = code
def code(*args, **kwargs):
    retval = orig_code(*args, **kwargs)
    validate_code(retval)
    return retval

@match(choice(tr.Statement, tr.Block, (many(tr.Statement),)))
def validate_code(retval):
    return True