package builtin_md;

public class builtin_ServerResponder_onFuture_Method extends builtin.reflect.Method implements io.datawire.quark.runtime.QObject {
    public builtin_ServerResponder_onFuture_Method() {
        super("builtin.void", "onFuture", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"builtin.concurrent.Future"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        builtin.ServerResponder obj = (builtin.ServerResponder) (object);
        (obj).onFuture((builtin.concurrent.Future) ((args).get(0)));
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
