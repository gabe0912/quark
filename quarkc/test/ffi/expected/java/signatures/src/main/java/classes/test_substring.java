package classes;

public class test_substring extends string_test implements io.datawire.quark.runtime.QObject {
    public static quark.reflect.Class classes_test_substring_ref = quark_ffi_signatures_md.Root.classes_test_substring_md;
    public String what;
    public Integer start;
    public Integer end;
    public test_substring(String what) {
        super();
    }
    public test_substring that(Integer start, Integer end) {
        return (test_substring) (null);
    }
    public test_substring does(String expected) {
        return (test_substring) (null);
    }
    public String _getClass() {
        return "classes.test_substring";
    }
    public Object _getField(String name) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            return (this).what;
        }
        if ((name)==("start") || ((Object)(name) != null && ((Object) (name)).equals("start"))) {
            return (this).start;
        }
        if ((name)==("end") || ((Object)(name) != null && ((Object) (name)).equals("end"))) {
            return (this).end;
        }
        return null;
    }
    public void _setField(String name, Object value) {
        if ((name)==("what") || ((Object)(name) != null && ((Object) (name)).equals("what"))) {
            (this).what = (String) (value);
        }
        if ((name)==("start") || ((Object)(name) != null && ((Object) (name)).equals("start"))) {
            (this).start = (Integer) (value);
        }
        if ((name)==("end") || ((Object)(name) != null && ((Object) (name)).equals("end"))) {
            (this).end = (Integer) (value);
        }
    }
}
