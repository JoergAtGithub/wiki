## Tests
Run the tests with `ctest --output-on-failure`
or set the environment variable `CTEST_OUTPUT_ON_FAILURE`
to print logs of failed tests.

## Debugging
### gdb
Use `gdb` to get backtraces in case of crashes.

- Enter gdb through `gdb mixxx-test --gtest_filter=CLASS.TESTNAME`
  from the build directory and wait until it has read all the symbols.
  (always isolate a single test when using `mixxx-test` directly)
- `run` the test
- Gdb will automatically stop on crash,
  then use `backtrace` to inspect the call-sites.

Use a debugger with breakpoints at suspicious lines to inspect program state.

#### gdb & Qt - gdbinit
For more helpful debug inspection results,
[create a `.gdbinit` file](https://unix.stackexchange.com/a/202375),
here some [instructions from KDE](https://community.kde.org/Guidelines_and_HOWTOs/Debugging/Debugging_with_GDB) 
and [Lekensteyn](https://github.com/Lekensteyn/qt5printers).

There are specific guides for [CLion](https://www.jetbrains.com/help/clion/qt-tutorial.html#debug-renderers) 
and [Eclipse](Eclipse#set-up-debug).