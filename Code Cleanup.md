# Code cleanup

The Mixxx codebase has been around for a long time and has had many
hands in it. Major parts of it have been re-written over time and as a
result, it has accumulated a number of problems that, if fixed, would
make future work easier and help fix current and avoid future bugs.

Here is a high-level list of things to do to make this happen:

  - Remove all Qt version 3 code
  - Search the code for "`Qt3`" and "`QT3`" and replace with Qt4
    equivalents
  - Address all developer questions and concerns in code comments
  - Search the code for each of the following and fix (discuss with
    others as needed):

<!-- end list -->

``` 
    * ''TODO''
    * <code>FIXME</code>
    * ''XXX''
    * ''hack''
    * ''wtf''
    * ''why''
    * ''?!''
* Replace deprecated code
  - Save the compiler output from a clean build
  - Search for "''deprecated''"
  - Replace all implicated code ([[fixes_for_qt_deprecations|this page]] might be helpful)
* Address all warnings
  - Save the compiler output from a clean build
  - Search for "''warning''"
  - Determine if the warning is avoidable (unused variables for example,) and if so, fix it. If not, make note of why. 
    * For unused variables, use ''Q_UNUSED(name);'' in the method body: <code cpp-qt>void MyClass::MyMethod(int myArg) { Q_UNUSED(myArg); }</code> This suppresses compiler warnings and has the added nicety of documenting that the argument is intended to go unused.
```
