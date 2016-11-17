void test_any_type() {
    Any a;
    List<Any> aListAny;
    List<Any> noListAny;

    bool aBool = true;
    bool noBool;
    int aInt = 42;
    int noInt;
    String aString = "yay";
    String noString;
    //float aFloat = 4.2;
    //float noFloat;
    List<int> aListInt = [42];
    List<String> aListString = ["yay"];


    a = aBool.asAny();
    assertEqual(1, a.type());
    assertEqual(aBool, a.asBool());
    assertEqual(noInt, a.asInt());
    assertEqual(noString, a.asString());
    //assertEqual(noFloat, a.asFloat()); // XXX need float for this test
    assertEqual(noListAny, a.asList());
    //assertEqual(null, a.asMap());  // XXX need null for this test

    a = aInt.asAny();
    assertEqual(2, a.type());
    assertEqual(noBool, a.asBool());
    assertEqual(aInt, a.asInt());
    assertEqual(noString, a.asString());
    //assertEqual(noFloat, a.asFloat()); // XXX need float for this test
    assertEqual(noListAny, a.asList());
    //assertEqual(null, a.asMap());  // XXX need null for this test

    a = aString.asAny();
    assertEqual(3, a.type());
    assertEqual(noBool, a.asBool());
    assertEqual(noInt, a.asInt());
    assertEqual(aString, a.asString());
    //assertEqual(noFloat, a.asFloat()); // XXX need float for this test
    assertEqual(noListAny, a.asList());
    //assertEqual(null, a.asMap());  // XXX need null for this test

    //a = aFloat.asAny()
    //assertEqual(4, a.type());
    //assertEqual(noBool, a.asBool());
    //assertEqual(noInt, a.asInt());
    //assertEqual(noString, a.asString());
    //assertEqual(aFloat, a.asFloat()); // XXX need float for this test
    //assertEqual(noListAny, a.asList());
    //assertEqual(null, a.asMap());  // XXX need null for this test

    a = aListInt.asAny();
    assertEqual(5, a.type());
    assertEqual(noBool, a.asBool());
    assertEqual(noInt, a.asInt());
    assertEqual(noString, a.asString());
    //assertEqual(noFloat, a.asFloat()); // XXX need float for this test
    aListAny = a.asList();
    assertEqual(1, aListAny.size());
    assertEqual(aListInt[0], aListAny[0].asInt());
    //assertEqual(null, a.asMap());  // XXX need null for this test

    a = aListString.asAny();
    assertEqual(5, a.type());
    assertEqual(noBool, a.asBool());
    assertEqual(noInt, a.asInt());
    assertEqual(noString, a.asString());
    //assertEqual(noFloat, a.asFloat()); // XXX need float for this test
    aListAny = a.asList();
    assertEqual(1, aListAny.size());
    assertEqual(aListString[0], aListAny[0].asString());
    //assertEqual(null, a.asMap());  // XXX need null for this test
}