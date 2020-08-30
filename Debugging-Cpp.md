## Tests
Run tests with `ctest --output-on-failure` to print stdout of failing tests.

## Debugging
### gdb
Use `gdb` to get backtraces in case of crashes
- `gdb mixxx-test`, then wait until it has read all the symbols
  - to run only specific tests, use `gdb --args mixxx-test --gtest_filter=TESTNAME\*`
- `run` to execute the program
- gdb will automatically stop on crash, then use `backtrace` to inspect the call-sites

Use a debugger with breakpoints at suspicious lines to inspect program state.

#### gdb & Qt - gdbinit
For more helpful debug inspection results, [create a `.gdbinit` file](https://unix.stackexchange.com/a/202375), here some [instructions from KDE](https://community.kde.org/Guidelines_and_HOWTOs/Debugging/Debugging_with_GDB) and [Lekensteyn](https://github.com/Lekensteyn/qt5printers).

There are specific guides for [CLion](https://www.jetbrains.com/help/clion/qt-tutorial.html#debug-renderers) and [Eclipse](Eclipse#set-up-debug).