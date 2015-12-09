var _qrt = require("datawire-quark-core");


// CLASS Test

function Test(name) {
    this.__init_fields__();
    (this).name = name;
}
exports.Test = Test;

function Test__init_fields__() {
    this.name = null;
}
Test.prototype.__init_fields__ = Test__init_fields__;

function Test__getClass() {
    return "test2.Test";
}
Test.prototype._getClass = Test__getClass;

function Test__getField(name) {
    if ((name) === ("name")) {
        return (this).name;
    }
    return null;
}
Test.prototype._getField = Test__getField;

function Test__setField(name, value) {
    if ((name) === ("name")) {
        (this).name = value;
    }
}
Test.prototype._setField = Test__setField;

function go() {
    var t = new Test("Hello World!!");
    _qrt.print((t).name);
    _qrt.print((new Test("Hello World!!")).name);
}
exports.go = go;