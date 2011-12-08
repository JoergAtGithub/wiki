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

<!-- end list -->

``` 
- 
```

## Writing a new test

We require that any new code classes have tests written for them as well
in order to consider the code for inclusion into Mixxx.

Mixxx uses the Google C++ Testing Framework. If it's new to you, [read
the
primer](http://code.google.com/p/googletest/wiki/Primer#Basic_Concepts).

After you understand how it works, do the following:

1.  Write the code that will test your chosen Mixxx class and place it
    in mixxx/src
2.  Build Mixxx with `scons test=1`

<!-- end list -->

``` 
- 
```
