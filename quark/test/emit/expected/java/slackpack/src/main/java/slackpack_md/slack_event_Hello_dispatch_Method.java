package slackpack_md;

public class slack_event_Hello_dispatch_Method extends builtin.reflect.Method implements io.datawire.quark.runtime.QObject {
    public slack_event_Hello_dispatch_Method() {
        super("builtin.void", "dispatch", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"slack.SlackHandler"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        slack.event.Hello obj = (slack.event.Hello) (object);
        (obj).dispatch((slack.SlackHandler) ((args).get(0)));
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
