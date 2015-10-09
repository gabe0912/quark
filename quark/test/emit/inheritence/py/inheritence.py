import os, sys

_Map = dict
class _List(list):
    def __repr__(self):
        return "[%s]" % ", ".join([str(e) for e in self])

def _println(obj):
    if obj is None:
        sys.stdout.write("null\n")
    else:
        sys.stdout.write("%s\n" % obj)

class A:
    def _init(self): pass
    def __init__(self): self._init()
    
    def foo(self):
        _println("A");
    

class B(A):
    def _init(self):
        A._init(self)
        
    
    
    def foo(self):
        _println("B");
    

class C(A):
    def _init(self):
        A._init(self)
        
    


def main():
    a = A();
    (a).foo();
    b = B();
    (b).foo();
    c = C();
    (c).foo();
    _println("--");
    a = b
    (a).foo();
    a = c
    (a).foo();


if __name__ == "__main__":
    main()