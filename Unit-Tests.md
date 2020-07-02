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
this also finds unintended interactions or consequences of a change. We
have two continuous integration (CI) services set up with our GitHub
project that automatically build each pull request and run all the
tests. Every time you push an update to a branch that you have an open
pull request for, they will rebuild your branch and run the tests again.
It is a good idea to run the tests locally first so you do not have to
wait for CI to let you know you broke a test (which typically takes
around an hour, sometimes longer) - especially if you are working on a
complicated area of Mixxx where it is easy to break things. Travis is
our CI service for GNU/Linux & Mac OS X and AppVeyor is our CI service
for Windows. We use the free version of these services which have a time
limit for each job, so sometimes a build times out before it finishes.
If Travis or AppVeyor fails, check their log to see if the build or a
test actually broke or just timed out.

Writing tests can be difficult at first, especially when trying to
isolate pieces of a very large codebase like Mixxx. However the payoff
is great, and as the test suite grows it becomes gradually easier to 
add new tests.

## Running the test suite

To manually run the existing tests on your copy of Mixxx (required
before final submission of patches or branch merge proposals,) do the
following:

1.  Build Mixxx with `cmake --build . --target mixxx-test --parallel $(nproc)`
2.  To run all tests: `./mixxx-test` 
3.  To run a specific test: `./mixxx-test --gtest_filter=MyTest*`

## Writing a new test

We strongly prefer that any new code classes have tests written for them
as well in order to consider the code for inclusion into Mixxx

Mixxx uses the [Google C++ Testing Framework](https://github.com/google/googletest).
If it's new to you, read the 
[Google Test primer](https://github.com/google/googletest/blob/master/googletest/docs/primer.md)
and [Google Mock primer](https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md).

Make sure to read
[this section of the Advanced testing guide](http://code.google.com/p/googletest/wiki/AdvancedGuide#Floating-Point_Comparison)
on floating point comparison. It is very important for writing Mixxx audio tests.

After you understand how it works, do the following:

1.  Write the code that will test your chosen Mixxx class and place it
    in src/test/  
    **If your class is ClassName, please name your test file `classname_test.cpp`**
2.  Follow the above steps for Running the tests. 
    Mixxx will automatically see and build your new test.

## Using Mocks

Mocking is an advanced technique for testing code. Say you have two
classes, Foo and Bar. If Foo relies on calling methods of Bar, then
using traditional unit testing methods you can't test Foo without also
testing Bar. Mocks allow you to solve this problem by creating a mock of
Bar. Using a mocking framework, you create a MockBar class which returns
arbitrary data.

For mocking, we use the
[Google Mock framework](http://code.google.com/p/googlemock/). 
It integrates very well with Google Test. To see an example of mocking 
in action, see the EngineMaster tests in `src/test/enginemastertest.cpp`.
The [Mocking For Dummies](http://code.google.com/p/googlemock/wiki/ForDummies)
guide on the Google Mock wiki is great for learning more about mocking,
dependency injection, and other advanced testing techniques.

## What do I test?

The two best times to write tests are during initial development and
when you're fixing bugs. During development, you want to know that your
classes and functions do what you think they do. While it's not
necessary to test a function like void setMyFoo(Foo\* f) {m\_f = f;},
write a basic test for nearly everything else. Not only will you catch
bugs more quickly, but **code that is easily testable is almost always
better code.** If your code is hard to test, that's a sign that it's not
well-written.

There is no need to account for every possible problem. Check to see how
your code handles NULL pointers or out-of-bounds values, but don't go
crazy. Test for correct input and then two or three examples of bad
input that come to mind immediately. If you miss something, you can
always add another test later.

When you are investigating a bug report, begin by writing a test that
exercises the bug. While you're fixing the bug you can run the test
instead of starting up Mixxx every time you rebuild. This will improve
your iteration time dramatically. Then, once you're done, you'll have a
regression test all ready to go - that particular bug should never
slip through again.

## An example test

Here's an excerpt of [a test that Owen wrote for the master sync branch](https://github.com/mixxxdj/mixxx/blob/master/src/test/enginesynctest.cpp):
``` cpp
#include "test/mockedenginebackendtest.h"

class EngineSyncTest : public MockedEngineBackendTest {
};


TEST_F(EngineSyncTest, InternalMasterSetFollowerSliderMoves) {
  // If internal is master, and we turn on a follower, the slider should move.
  QScopedPointer<ControlObjectThread> pButtonMasterSyncInternal(getControlObjectThread(
          ConfigKey("[Master]", "sync_master")));
  pButtonMasterSyncInternal->slotSet(1);
  ControlObject::getControl(ConfigKey("[Master]", "sync_bpm"))->set(100.0);
  
  // Set the file bpm of channel 1 to 160bpm.
  ControlObject::getControl(ConfigKey(m_sGroup1, "file_bpm"))->set(80.0);
  
  QScopedPointer<ControlObjectThread> pButtonMasterSync1(getControlObjectThread(
          ConfigKey(m_sGroup1, "sync_mode")));
  pButtonMasterSync1->slotSet(SYNC_FOLLOWER);
  
  ASSERT_FLOAT_EQ(getRateSliderValue(1.25),
                  ControlObject::getControl(ConfigKey(m_sGroup1, "rate"))->get());
  ASSERT_FLOAT_EQ(100.0, ControlObject::getControl(ConfigKey(m_sGroup1, "bpm"))->get());
}

```

This tests the interaction of various control objects when Master Sync
is active. The function definition "TEST\_F" is actually a specialized
macro - the parameters are the name of the testing class. In this case,
the class EngineSyncTest is a copy of another testing class called
MockedEngineBackendTest, which sets up an engine master, two decks
(called \[Test1\] and \[Test2\]), and even loads a couple of fake tracks
into the decks. (m\_sGroup1 is **not** "\[Channel1\]" because I want to
make sure we're not relying on specific string values in internal code.)

The body of the test itself sets the master bpm and file bpm for a
track, and then checks that the rate slider of the deck is adjusted as
expected. The rate slider CO value is dependent on the rate range, so
the function getRateSliderValue(double) performs the conversion from
multiplier value to CO value.

Note the use of ASSERT\_FLOAT\_EQ, which tests equality at a low enough
tolerance that minor floating point errors won't cause test failures.

Some tests only make sense if a track is playing. To test a playing
track, set the "play" CO and then tell the testing enginemaster
to process one callback buffer:

``` cpp
ControlObject::getControl(ConfigKey(m_sGroup1, "play"))->set(1.0);

ProcessBuffer();
```

You can find a test in [enginesynctest.cpp](https://github.com/mixxxdj/mixxx/blob/master/src/test/enginesynctest.cpp)
that calls ProcessBuffer() a couple times to see if the actual 
playback rate of the decks has been correctly updated.

The fake tracks always produce complete silence - a buffer of all
zeros. So this particular testing class is only useful for testing
rates, seeking, and other playback metadata. If you want to test actual
sound processing, take a look at 
[enginebufferscalelineartest.cpp](https://github.com/mixxxdj/mixxx/blob/master/src/test/enginebufferscalelineartest.cpp).
