package quark_ffi_signatures_md;

public class interfaces_Foo_m3_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public interfaces_Foo_m3_Method() {
        super("quark.void", "m3", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.List<quark.String>"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        interfaces.Foo obj = (interfaces.Foo) (object);
        (obj).m3((java.util.ArrayList<String>) ((args).get(0)));
        return null;
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}
