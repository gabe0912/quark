package quark_ffi_signatures_md;

public class generics_ccc_Context_global_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public generics_ccc_Context_global_Method() {
        super("generics.ccc.Context", "global", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        generics.ccc.Context obj = (generics.ccc.Context) (object);
        return generics.ccc.Context.global();
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}
