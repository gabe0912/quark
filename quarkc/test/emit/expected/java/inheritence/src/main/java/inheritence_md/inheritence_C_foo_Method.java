package inheritence_md;

public class inheritence_C_foo_Method extends builtin.reflect.Method implements io.datawire.quark.runtime.QObject {
    public inheritence_C_foo_Method() {
        super("builtin.void", "foo", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        inheritence.C obj = (inheritence.C) (object);
        (obj).foo();
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