# Unit testing

Essential to any software quality control process is unit testing:
isolating each piece of a system and hitting it with all manner of valid
and invalid input values to check for all of the following:

  - That it produces correct results on all ranges of valid input
    (especially corner cases)
  - That it produces reasonable results or accurate error messages on
    every kind of invalid input
  - That it doesn't crash or otherwise misbehave under load or with any
    mix of valid or invalid input
  - That all code paths have been exhaustively tested for the above

Such tests should be run on all of Mixxx after every code change, as
this also finds unintended interactions or consequences of a change. Our
build servers will be configured to do this automatically and will fail
a build if a test fails.

## Running the test suite

To manually run the existing tests on your copy of Mixxx (required
before final submission of patches or branch merge proposals,) do the
following:

1.  Build Mixxx with `scons test=1`
2.  To run all tests: `$ ./mixxx-test` 
3.  To run a specific test: `$ ./mixxx-test --gtest_filter=MyTest*`

## Writing a new test

We require that any new code classes have tests written for them as well
in order to consider the code for inclusion into Mixxx.

Mixxx uses the Google C++ Testing Framework. If it's new to you, [read
the
primer](http://code.google.com/p/googletest/wiki/Primer#Basic_Concepts).

After you understand how it works, do the following:

1.  Write the code that will test your chosen Mixxx class and place it
    in mixxx/src/test/
    1.  **If your class is ClassName, please name your test file
        `classname_test.cpp`**
2.  Follow the above steps for Running the tests. Mixxx will
    automatically see and build your new test.

## Using Mocks

Mocking is an advanced technique for testing code. Say you have two
classes, Foo and Bar. If Foo relies on calling methods of Bar, then
using traditional unit testing methods you can't test Foo without also
testing Bar. Mocks allow you to solve this problem by creating a mock of
Bar. Using a mocking framework, you create a MockBar class which returns
arbitrary data.

For mocking, we use the [Google
Mock](http://code.google.com/p/googlemock/) framework. It integrates
very well with Google Test. To see an example of mocking in action, see
the EngineMaster tests in `enginemastertest.cpp`. The [Mocking For
Dummies](http://code.google.com/p/googlemock/wiki/ForDummies) guide on
the Google Mock wiki is great for learning more about mocking,
dependency injection, and other advanced testing techniques.
