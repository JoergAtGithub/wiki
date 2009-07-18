# Mixxx test suite

*Based on [Google Test](http://code.google.com/p/googletest/)*

## For testers

1.  Build Mixxx using `scons test=1`. You'll get a `mixxx-test` binary
    alongside the usual `mixxx` binary.
2.  Run `mixxx-test`. It will run every test in each of our test suites,
    and return to you the passes/failures, along with the tests that
    failed.

When we run this test suite, we will have higher assurance that our
development efforts are eliminating bugs and at the same time, not
regressing on old ones.

## For developers

To add a test, all you have to do is add a source file to `src/test/`
which inherits from `testing::Test`. As an example, check out some basic
ControlObject tests I added in `src/test/controlobjecttest.cpp`

To read more about how to use Google Test, check out this primer:
<http://code.google.com/p/googletest/wiki/GoogleTestPrimer>

### Why Google Test?

  - Supported on our three main platforms.
  - Since Google use it extensively, we know it's been tested in serious
    environments, and will continue to be a healthy project.
  - Impressive support for a number of different kinds of tests (death
    tests, etc)
