var _qrt = require("datawire-quark-core");
var builtin = require('builtin').builtin;
exports.builtin = builtin;
var test = require('./test');
exports.test = test;
var package_md = require('../package_md');
exports.package_md = package_md;



function go() {
    _qrt.print("GO!");
}
exports.go = go;

// CLASS Test
function Test() {
    this.__init_fields__();
}
exports.Test = Test;

function Test__init_fields__() {
    this.name = null;
}
Test.prototype.__init_fields__ = Test__init_fields__;
Test.test_Test_ref = package_md.Root.test_Test_md;
function Test_go() {
    _qrt.print("TGO!");
}
Test.prototype.go = Test_go;

function Test__getClass() {
    return "test.Test";
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

function main() {
    go();
    test.go();
    var t1 = new Test();
    var t2 = new test.Test();
    (t1).go();
    (t2).go();
}
exports.main = main;