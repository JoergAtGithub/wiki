# Mixxx Style Guide

## General Philosophy

When you're writing code for open source projects, the most important
rule to follow is this:
**Try to make your code blend in with the existing code.**

Stick closely to the 
[CppCoreGuidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
and follow its recommendations unless otherwise noted below. It has been written
by very active members of the C++ committee. We also recommend
to take a look at the 
[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html). 
It's a treasure trove of C++ advice. Just double Google's indentation - 
2 spaces become 4 spaces; 4 spaces become 8 spaces.

That being said, large chunks of Mixxx are written in
slightly differing styles (mainly variable naming conventions). In order
to avoid this in the future, it's best for us to have some coding
guidelines for developers to follow.

> As you change a part of Mixxx, please update it to match this style
guide and reformat it with ClangFormat. That way, eventually all of
Mixxx will be written in this style.  
Do not send us patches that are purely cosmetic with respect to source changes -
this is a waste of time since it does not benefit users directly.

## CO and setting keys

Newly introduced keys should use `snake_case` formatting. 

## Code Formatting

Since 2019-05-09 our code formatting rules are defined by the
[.clang-format](https://github.com/mixxxdj/mixxx/blob/master/.clang-format)
configuration file in the project root.  
Make use of it by auto-formatting new or modified code segments - but take care not to mass reformat unrelated code!

[ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) version \>= 4.0 is required.
On Ubuntu, ClangFormat is in the [official repositories](https://packages.ubuntu.com/search?suite=all&searchon=names&keywords=clang-format). From bionic (18.04) on you can install the plain `clang-format` package, use this on older distros as it is outdated there:
```sh
sudo apt-get install clang-format-8
sudo update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-8 1000
```

### pre-commit

To automatically adjust the code style in every commit, it is
recommended to install the [pre-commit](https://pre-commit.com/)
framework. It will run a few scripts, including clang-format, 
on every commit and pugh, to ensure the code guidelines are met.

The required config file, including installation instructions, is in the
Mixxx repository at
[.pre-commit-config.yaml](https://github.com/mixxxdj/mixxx/blob/master/.pre-commit-config.yaml).
Please note that it requires at least Python 3.7.
[Here](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-8-on-ubuntu-18-04-lts/)
are instructions for updating python3 on Ubuntu LTS.

### Command line

Alternatively you may use
[git-clang-format](https://raw.githubusercontent.com/llvm-mirror/clang/master/tools/clang-format/git-clang-format)
from the command line.

Use it like this to reformat after each commit:
``` sh
git-clang-format HEAD~
git commit -a --amend
```

or if the PR is already under review:
``` sh
git-clang-format upstream/master
git commit -a -m "Apply git-clang-format changes"
```

Apply *clang-format* to individual source files (only permitted for new files):
```sh
clang-format -i -style=file [<file> ...]
```
*clang-format* will pick up the confguration in the *.clang-format* file from
the current or any parent directory of the source file(s).

### Visual Studio Code

Code formatting is available in [Visual Studio Code](https://code.visualstudio.com).
Install the [C/C++ Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
and verify or update the following settings:

  - ***C\_Cpp.formatting*** = *Default* (default)
  - ***C\_Cpp.clang\_format\_style*** = *file* (default)
  - ***C\_Cpp.clang\_format\_fallbackStyle*** = *Google*
  - ***C\_Cpp.clang\_format\_sortIncludes*** = *null* (default)
  - ***C\_Cpp.clang\_format\_path*** = *null* (default) or *path to your
    clang-format executable* (optional)

Don't enable auto-formatting on save, because this will add unnecessary
noise to your pull request.

  - ***editor.formatOnSave*** = *false*
  - ***editor.formatOnType*** = *true*

### KDevelop

[KDevelop](KDevelop) has a [clang-tidy plugin](https://github.com/KDE/kdev-clang-tidy).

### Eclipse

If you use Eclipse as IDE, the code style "K\&R" works well with these
tweaks

  - tab policy = space only
  - new lines = before colon in constructor initializer list

Please note that there are still some exceptions, so do not auto-format
a whole file.

In addition you can install <https://marketplace.eclipse.org/content/cppstyle>
to use clang-format from the GUI.

### CLion

Make sure the ClangFormat plugin is installed and enable it in the
Settings under Editor > Code Style.

## Tabs vs. Spaces

In Mixxx **indents are 4 spaces**.
Stick to this and do not use tabs, if only for consistency.

## Line Wrapping

Please set up a max column-width of 80 columns in your editor.
While it is not a strict requirement, 80-column cleanliness makes it easier to
tile multiple buffers of code across a screen, which can provide
significant efficiency gains to developers.

For Mixxx's clang-format compatibility (ColumnLimit: 0):

  - Use double indent (8-spaces) for broken lines (ContinuationIndent: 8).
  - Break line after binary operators.
  - If you break a list of function parameters, put each parameter on a
    single line (BinPackArguments: false & BinPackParameters: false).

### Continuation Indent

We add 8 spaces of indentation for broken lines, which helps to easily
distinguish them from logical blocks.

**Good:**

```cpp

if (long_expression1 ||
        long_expression2 ||
        long_expression_with_along_parameter_1(parameter1) {
    long_expression_with_along_parameter_2(parameter1)
}

```

**Bad:**

```cpp
if (long_expression1 ||
    long_expression2 ||
    long_expression_with_along_parameter_1(parameter1) {
    long_expression_with_along_parameter_2(parameter1)
}

```

# C++ Style Guide

This is an overview of the various conventions that the Mixxx team
follows when writing Mixxx code. Do not start holy wars over these 
conventions - they are simply intended to keep the Mixxx codebase 
**consistent**. Strive to follow these guidelines as much as possible.
If you do not, we may ask you to clean up your code to follow the 
style guide during code-review.

## Naming

### Variables

Give variables and classes a descriptive but succinct name.

**Avoid:** Variable names that do not give a hint for their purpose.
**Examples:** ix, i, index, position, name, foo, bar

Local variables should follow either a camelBack case or
lowercase\_with\_underscores style:

```cpp
QString hotcue_name;
int composerSortOrder;
```

Pointers should be prefixed with a "p" to indicate they are a pointer.
The "\*" should be aligned with the type and **not** the name.

**Examples:**"

```cpp
int* pHotcueIndex;
```

Optionally include minimal type information with variables. This can be
handy to know at a glance the rough type of an object. For example, for
a [ControlObject](ControlObject) a common pattern is to prepend "CO" to
the variable name:

```cpp
ControlObject* m_pCOPlayButton;
```

### Classes

- Class names must be in CamelCase (e.g. `MyName`), with each word capitalized. 
- Member functions of classes must be camelBack cased (e.g. `thisFunction`).
- Member variables **must** be prefixed with `m_`. It is essential to
  know the scope of a variable is at the class-member level with a
  simple glance for easy readability of source files.
- Class variables (static class members) **must** be prefixed with `s_`.

## Braces

Braces should not be given their own newline.
Always separate them from surrounding code with a single space.

**Good:**

```cpp
if (expression) {
  // something
} else {
  // something else
}

if (long_expression1 ||
        expression2) {
  // something
  statement
}

```

**Bad:**

```cpp
if (expression)
{
}
else
{
}
```

### Using Braces

Always wrap the body of decision and looping statements (if, else, 
switch, while, for) in braces to keep the code consistent and readable.
This was unanimously [settled on Zulip](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/coding.20style.3A.20guard.20clauses/near/202839531).

### If Statements

There should be one space following the `if` keyword, and one space
following the closing parenthesis of the condition before the brace.

**Good:**

```cpp
if (expression) {

}
```

Do not add padding inside the conditional or omit a space between the
`if` keyword and the conditional parenthesis.

**Bad:**

```cpp
if( expression ){

}
```

Do not manipulate variables inside conditional expressions.
Variable assignment should be on its own line.

**Good:**:

```cpp
++counter;
if (counter > threshold) {

}
```

**Bad**:

```cpp
if (++counter > threshold) {

}
```

### For Loops

Similarly to `if` statements, there should be a single space of padding
after the `for` keyword and after the closing conditional parenthesis.
Additionally, a single-space padding should come after the semicolon
separators between the initializer, conditional, and increment statements.

**Good:**

```cpp
for (initializer; conditional; increment) {

}
```

## Namespaces

Please refer to the [Google C++ Style Guide's namespace
section](https://google.github.io/styleguide/cppguide.html#Namespaces).

In new code, please wrap the code in the "mixxx" namespace (avoid making
a hierarchy of namespaces). Put module-local helper functions in an
anonymous namespace in the cpp file.

### In the header file

```cpp
#include <SomeQtHeaderUsedInThisHeader>

#include "some/mixxx/file/used/in/this/header.h"

namespace mixxx {

class MyClass {
  public:
    MyClass();
  
  private:
    bool m_helper;
};

bool myFunction();

} // namespace mixxx
```

### In the implementation (.cpp) file

```cpp
#include "path/to/myclass.h"

#include <LocallyNeededQtHeader>

#include "locally/needed/mixxx/header.h"

namespace mixxx {
namespace {

// Put file-local helper functions and constants here.
bool myHelper() {
    return true;
}

} // namespace 

// Put class implementations, functions, and constants 
// that are meant to be used by other parts of Mixxx here.
MyClass::MyClass(): m_helper(myHelper()) {
}

bool myFunction() {
    return myHelper();
}

} // namespace mixxx
```

## Comments

Comments should be complete, descriptive sentences in the present tense.
If a comment is a warning or something that might need to be
re-evaluated in the future, date the comment with the current month and
year, along with your user name.

**Good:**

```cpp
// This is required because we don't have enough foo's in the bar -- rryan 2/2011
doSomething();
```

Prefer to use C++-style comments. All trailing line comments start with
a single space after the separator.

Avoid to use C-style comments or Java-style multi-line comments.

**Bad:**

```cpp
/*
 * Java-style comment
 */ 
thisCommentIsReallyVerboseFactoryMethodInjectorObserver()
/* C-style comment -- avoid because you can't nest them */
```

Avoid comments that do not add more information than the words contained
in the statement that follows them. Instead, write a descriptive summary
of what the following lines accomplish.

**Bad:**

```cpp
/* init boofar */
initBoofar();
```

Avoid to comment out code unless a preceding textual comment explains
the exact purpose of the following lines and why this code needs to be
preserved as a comment. Commented out debugging statements without an
additional description are acceptable if the intend is obvious.

### Documentation

Use `///` for documentation comments above class and member definitions
in header files. These comments are shown in IDEs associated with the
symbol.

Add a few sentences to explain the purpose and use of a class to its
header file for every new class you add.  Currently, a lot of the 
Mixxx code is lacking documentation, so please improve that as you 
work on it.

### TODO's

If you'd like to leave a `TODO` for yourself, format them like this:

```cpp
// TODO(rryan) Make sure to double-check this.
```

If you'd like to leave a general `TODO` for the team, use the name
`XXX`:

```cpp
// TODO(XXX) Make this more general
```

Remember to actually go back and investigate your `TODO`'s :).

**Bad:**

```cpp
// TODO Make this more general
```

## C++ Guideline Support Library

Use the [GSL](https://github.com/Microsoft/GSL) when applicable or recommended
by the C++ Core Guidelines, but prefer constructs from the C++ standard library
if possible.

## C++ Header Files

This section outlines our various standards for writing header (.h)
files.

### Credit and License

If you wish to credit yourself and leave a notice for who people should
contact for help about a file, do so in the most brief way possible. Do
not insert ASCII art. Do not include a copyright notice, or license
because the project has a root LICENSE file which covers these
declarations, and so any file-level declarations would be redundant.

```cpp
// filename.h 
// Created 2/21/2011 by RJ Ryan <email> 
```

### pragma once guard

For new header files use a \#pragma once directive instead of \#include
guards:

```cpp
#pragma once
```

There are many header files with legacy include guards like:

```cpp
#ifndef LIBRARY_H
#define LIBRARY_H

#endif
```

Replace these with `#pragma once` when you edit a header file.

### includes

File includes should be done in the following order:

1.  Matching header file include for current cpp file (if applicable)
2.  System Includes
3.  Qt Includes
4.  Includes of Mixxx library dependencies
5.  Mixxx local includes
6.  Class forward-declarations

Each different group of includes should be separated by a single empty
line. **Order the includes in alphabetical order.** Relative includes
**should never be used**. Always include Mixxx local files by specifying
them from the root of the `src` folder.

Generally do not forward declare any classes other than Mixxx project classes.
For forward declarations of *Qt* types use the `QT_FORWARD_DECLARE_CLASS` macro
that is defined in `<QtGlobal>`.

**Example:**

  ```cpp
  #include <math.h>
  #include <sys/types.h>

  #include <QtCore>
  #include <QtDebug>
  #include <QTreeView>

  #include <taglib/taglib.h>

  #include "library/library.h"

  QT_FORWARD_DECLARE_CLASS(QDomNode);

  class Cue;
  ```

### Class Declaration

The declaration of methods and member variables for classes should be
done in the following order:

1.  Q\_OBJECT macro, indented 4 spaces
2.  Public enums, constants, inner class declarations, etc.
3.  Public methods
4.  Public variables (**avoid**)
5.  Public `slots`
6.  Qt Signals 
7.  Protected enums, constants, inner class declarations, etc.
8.  Protected `slots`
9.  Protected methods
10. Protected variables
11. Private enums, constants, inner class declarations, etc.
12. Private `slots`
13. Private methods
14. Private member variables

A couple guidelines for class declarations:

  - Each access specifier should be indented **2 spaces**. 
  - Every different section (e.g. private methods, private member
    variables) should be separated by a single space. 
  - At your discretion you may insert separating lines between each
    method if it improves readability. 
  - **Every public method in a class should be accompanied by a comment
    describing what it does and how it should be invoked.** This is the
    only place that the overall functioning of member methods should be
    documented. The implementation of a member method should only have
    comments about the implementation. 
  - All destructors should have the 'virtual' keyword.
  - Consider marking single-argument constructors explicit so that they
    are not automatically invoked accidentally in assignment. 
  - Use C++-style comments, not C-style or Java-style comments.
  - All class declarations should be preceded with a brief description
    of the class and its purpose.

**Example:**

```cpp
// The Library is the manager class for all library functionality. It contains the LibraryFeature's 
// enabled for use with the library and connects them and their signals to the GUI's library widgets.
class Library : public QObject { 
    Q_OBJECT
  public:
    Library(QObject* pParent,
            ConfigObject<ConfigValue>* pConfig,
            bool firstRun);
    virtual ~Library();
    
    // bindWidget gives the Library a chance to insert logic into the library 
    // widgets (WLibrary and WLibrarySidebar).
    void bindWidget(
            WLibrarySidebar* sidebarWidget,
            WLibrary* libraryWidget,
            MixxxKeyboard* pKeyboard);
                    
    // Add a LibraryFeature to the list of features enabled in the Library.
    void addFeature(LibraryFeature* feature);
    
  public slots:
    // Request that the Library switch to the default track table and show the 
    // provided TrackModel. 
    void slotShowTrackModel(QAbstractItemModel* model);
    
    // Request that the library switch to the provided view name. Views should be 
    // registered in LibraryFeature::bindWidget() or Library::bindWidget
    void slotSwitchToView(const QString& view);
  
  signals:
    // Broadcast to the associated WLibrary widget that the provided model
    // should be switched to.
    void showTrackModel(QAbstractItemModel* model); 
    
    // Broadcast to the associated WLibrary widget that the view with the
    // provided name should be switched to.
    void switchToView(const QString& view);
    
  private:
    ConfigObject<ConfigValue>* m_pConfig;
    // List of LibraryFeature's enabled in the Library
    QList<LibraryFeature*> m_features;
};
```

## GOTO

Using the `goto` statement is not allowed. Typically uses of `goto` are
better handled by the C++ idiom of [Resource Acquisition Is
Initialization](http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization).

## Pointer, Object lifetime/Ownership

  - Follow the isocpp [no naked new
    rule](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#es60-avoid-new-and-delete-outside-resource-management-functions).
    Instead of using `new` and `delete` statements, use one of the
    following "smart pointers" to convey ownership right from the start:
    - `std::unique_ptr` for exclusive ownership: e.g. `auto p =
    std::make_unique<T>(...)`
    - `std::shared_ptr` for shared ownership: e.g. `auto p =
    std::make_shared<T>(...)`
    - `parented_ptr` for ownership by the QT object tree: e.g. `auto p =
    make_parented<T>(...)`

  - Pass reference `const T&` or `T&` if no ownership is transfered.
    Pass raw pointer `const T*` or `T*` if no ownership is transfered
    and `nullptr` is a valid argument value. A function which receives a
    reference or raw pointer should not hold onto it outside the scope
    of the function (e.g. by storing it in a member variable). An
    exception is the parent pointer passed into the constructor of a
    `QObject` and internally stored as a non owning reference.

  - Pass smart pointers by value if ownership is transfered
    (`std::unique_ptr`) or shared (`std::shared_ptr`). Do not pass smart
    pointers by reference.

  - Use `make_parented` to create objects derived from `QObject` that
    will be assigned to a parent (and will therefore be managed by the
    Qt object tree). The created object must get a parent before the
    `parented_ptr` is destructed. Example:
    ```cpp
    auto pBrowseButton = make_parented<QPushButton>(tr("Browse"));
    // *pBrowseButton is not assigned to a parent yet
    pLayout->addWidget(pBrowseButton);
    // Now *pLayout is the parent
    ```

  - The destructor of `parented_ptr` asserts that the pointed-to object
    actually has a parent. This ensures that the pointed-to object isn't
    leaked. A consequence is that **a `parented_ptr` must never
    dangle**. Never store a `parented_ptr` in an object that outlives
    the parent. This is most easily done by storing the `parented_ptr`
    inside exact the parent. If the lifetime of the pointer relative to
    the parent is not clear then store the output of
    `parented_ptr::toWeakRef()` instead of a `parented_ptr`.

  - Any exceptions to these guidelines must be clearly documented inline
    in the code.

## Assertions

Use Mixxx assert macros form util/assert.h to assert an assumption that
can never fail.

The DEBUG\_ASSERT macro works only in debug builds. When the assert
fails, a message is logged. If Mixxx is compiled with `scons
debug_assertions_fatal=1` it will be terminated after that. If Mixxx is
started under a debugger with `mixxx --debugAssertBreak` it will break
(SIGINT) in that case.

Use VERIFY\_OR\_DEBUG\_ASSERT if an error handling is required to
recover gracefully in a release build.

**Good**

```cpp
#include <util/assert.h>

...

bool failed = neverFails();
VERIFY_OR_DEBUG_ASSERT(!failed) {
   qWarning() << "neverFails() has failed"
   return;
}
```

## QString

Use [QStringLiteral](http://doc.qt.io/qt-5/qstring.html#QStringLiteral).
This has a variety of
[benefits](https://woboq.com/blog/qstringliteral.html).

Escape non ASCII characters:

```cpp
const QString kMessage = QStringLiteral("Hello I\u2019ve to go");
```

Due to [copy/move elision](https://en.cppreference.com/w/cpp/language/copy_elision)
in C++11 no temporary objects will be created by the assignment.
Prefer this style for all new code to improve readability.

QChars can be initialized with ASCII characters 16 bit Unicode
L’\\u00fc' if required. Both are constexpr.

```cpp
constexpr QChar kc = 'c'
constexpr QChar kue = L'\u00fc' // for "ü"
```

From Mixxx 2.3 we set QT\_USE\_QSTRINGBUILDER to use QStringBuilder for
operator+. Use + in favour of % for better readability.

## Non-Const References

In the C++ community are two mutually exclusive styles established:

1.) Google(original)/Qt: "References can be confusing, as they have value syntax
but pointer semantics."

_Note: Because of controversial opinions, Google has recently dropped the related paragraph without replacement. Here a link to the original version:_
<https://drake.mit.edu/styleguide/cppguide.html#Reference_Arguments>

2.) Cpp Core Guidelines: "This makes it clear to callers that the object
is assumed to be modified"
<https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#f17-for-in-out-parameters-pass-by-reference-to-non-const>

Since we have followed the original Google style we avoid using value syntax to change
variables via a lvalue reference. Using rvalue references to access
nested variables is permitted.

If method in question does not accept `nullptr`, pass `gsl::not_null<T*>` 
instead of `*T` to force the nullcheck to happen in the caller instead
of the callee.

**Good:**

```cpp

T& X::refIObject();

x.refObject().setValue() // The effected object is still part of the statement 

T* pObject = &refObject(); 
...
pObject->setValue(5); // The pointer syntax reveals the an external object is written 

```

**Bad:**

```cpp

T& X::refIObject();

T& object = refObject(); 
...
object.setValue(5); // It looks like a local variable is changed.  
```

## C++17

As of the Mixxx 2.3 release, Mixxx is switching to C++17. We are taking
a conservative approach to adopting C++11/14/17 features and
whitelisting them one by one. If a C++11/14/17 feature you would like to
use is not listed here, please email mixxx-devel to make a case for it
and we will consider whitelisting it.

We are limited to what is supported across our 3 supported compilers:

  - [Clang \>= 3.4](http://clang.llvm.org/cxx_status.html)
  - [GCC \>= 5.4 (Ubuntu Xenial)](https://gcc.gnu.org/projects/cxx0x.html)
  - [Microsoft Visual Studio 2017 (\_MSC\_VER \>= 1910)](https://msdn.microsoft.com/en-us/library/hh567368.aspx)

In general, Microsoft Visual Studio is the one that prevents us from
using features.

See also: [C++11 features in Qt5](http://woboq.com/blog/cpp11-in-qt5.html).

### initializer lists

<http://en.cppreference.com/w/cpp/language/list_initialization>

Use with caution!

**WARNING** on windows, they are not well supported with QT4. see the
following links for details

  - <https://sourceforge.net/p/mixxx/mailman/message/34805913/> 
  - <https://bugs.launchpad.net/mixxx/+bug/1627826> 
  - <https://github.com/mixxxdj/mixxx/pull/1019> 

### static\_assert

Use!

### nullptr

Yes! Always prefer to NULL.

### unique\_ptr / std::move

Yes! Prefer over QScopedPointer.

By including the custom file "util/memory.h" instead of the system
header \<memory\> you are even able to make use of
std::make\_unique\<\>() that was missing from the C++11 specification
and is now provided by C++14. This generic function should always be
used instead of *operator new* for the allocation of objects that are
wrapped in a *unique\_ptr*.

If possible, prefer std::unique\_ptr in std:: containers over
QSharedPointer in Qt containers.

Do not use unique\_ptr for QObjects which have a parent, in this case
the parent has the ownership. An early delete due to a smart pointer
emit unnecessary signals.

Prefer std::unique\_ptr over the Qt Object tree to manage the lifetime
of an object.

Side note: Deleting sender objects before receiver objects is faster,
because the sender owns the connection.

### default / delete functions

Use.

### delegating constructors

Use.

### constexpr

Use whenever possible, prefer it over preprocessing instructions such as `#define`.
Use PascalCase for naming variables and prefix with "k", e.g. `kSilenceThreshold`.

### right angle brackets

<http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2005/n1757.html>

Yes!

### override / final

Use always!
Any case where a method intentionally overrides that of a parent
class should use the *override* keyword.

In contrast to the pre-C++11 rules (see above) when using *override* on
a function in a derived class it is recommended to omit the redundant
*virtual* keyword, because *override* implies *virtual*.

Destructors in derived classes should also be marked with *override*
instead of *virtual*. This ensures at compile time that the base class
has declared a *virtual* destructor. If the base class has not declared
a *virtual* destructor the destructor of a derived class might not be
invoked. This applies also for default destructors even if it looks
noisy.

```cpp
~ClassName() override = default;
```

### alignment

Use (support added in VS2015). Some positive reports from
[another project](https://groups.google.com/forum/#!topic/cryptopp-users/KqODnEPjkbU).

### cstdint

Appears to be supported by MSVC 2013. Use!

### range-based for loops

Use the\! Prefer them over Qt's `foreach` macro which has enjoyed
widespread usage throughout the Mixxx codebase.

> Be very careful when updating old code from foreach to range-based-for.
[It is very easy to write a bug](https://www.kdab.com/goodbye-q_foreach/).

```cpp
for (const QString& item : list) {
  qDebug() << "WOOHOO" << item;
}
```

### auto

We do not follow a aaa-style (almost-always-auto).

Our rules of thumb:

  - use auto to prevent repeating yourself
  - auto when the type is long and does not add any value

Auto is acceptable in function-level scopes (i.e. only within function
bodies). Do not use auto in a function or method prototype as this makes
the code less self-documenting and would require reading the body of the
function to determine its return type or arguments.

More details can be found here:
<https://google.github.io/styleguide/cppguide.html#auto>

Good:

```cpp
void mixAudio(const QVector<QString>& values, QVector<EngineChannel*>* channels) {
  auto bufferSize = 256; // this avoids uninitialised locals
  
  for (const auto& value : values) { // Type can't get wrong 
      qDebug() << "blah:" << value;
  }
  
  for (auto* channel : *channels) {
      channel->process(bufferSize);
  }
}
```

Bad:

```cpp
auto mixAudio(const QVector<QString>& values, QVector<EngineChannel*>* channels) -> bool {
    return true; // need to read the function body 
}
```

Bad:

```cpp
auto value getValue(); // because the type is out of sight
```

Bad:

```cpp
QVector<RowInfo>::iterator it = rowInfo.begin();
// Explicit type is only clutter and can be easily guessed from the context. 
```

Bad:

```cpp
QList<int>* pList = new QList<int>(); // do not repeat yourself 
```

### closures / lambdas

Use carefully\! Closures can obscure the control flow of a system and
introduce tricky data lifetime issues. Using a lambda in your code will
require more time in code review and you may be asked to re-write the
code to avoid the usage by your code reviewer. Before using a closure,
please consider whether it's truly necessary.

Use 8 space indent for line break or reasonable alignment + 4 indent for
a new logical block. Always break after "},"

**Good:**

```cpp
    m_pTrackCollection->callSync(
            [this](TrackCollectionPrivate*-pTrackCollectionPrivate.md) {
                connect(&pTrackCollectionPrivate->getCrateDAO(),
                        SIGNAL(added(int)), this, SLOT(slotCrateAdded(int)));
                connect(&pTrackCollectionPrivate->getCrateDAO(),
                        SIGNAL(renamed(int, QString)), this,
                        SLOT(slotCrateRenamed(int, QString)));
                connect(&pTrackCollectionPrivate->getCrateDAO(),
                        SIGNAL(deleted(int)), this,
                        SLOT(slotCrateDeleted(int)));
                connect(&pTrackCollectionPrivate->getCrateDAO(),
                        SIGNAL(autoDjChanged(int, bool)), this,
                        SLOT(slotCrateAutoDjChanged(int, bool)));
            },
            __PRETTY_FUNCTION__);
```

### variadic templates

Email mixxx-devel with your use case.

### r-value references / move constructors / move assignment operators

In general, do not use. Do not add gratuitous move constructors -- this
decision should be motivated by profiling data to help avoid needless
copies.

**Note:** *auto&&* is a universal reference and not an r-value
reference\! It should be used instead of an explicit l-value *auto&*
reference in *range-based for loops* over non-const (= mutable)
containers as shown below.

**Good:**

```cpp
for (auto&& item : mutableContainer) {
  // read and write item
} 

for (const auto& item : immutableContainer) {
  // read only item
} 
```

The universal reference *auto&&* could be used in both cases, but prefer
*const auto&* if you don't intend to modify the item inside the loop's
body.

### forward declared / strongly typed enums

Use. Both the name of the enum type and its enumerated values should be
written in CamelCase with the first letter capitalized. Do not add new C
style enums and please replace those with enum classes when you are
working on code that uses them.

```cpp
enum class ChannelLayout {
    Unknown,
    Mono, // 1 channel
    DualMono, // 2 channels with identical signals
    Stereo, // 2 independent channels left/right
    // ...
};
```

### atomics

For now, prefer using [Qt atomic](https://doc.qt.io/qt-5/atomic-operations.html)
[primitives](https://doc.qt.io/qt-5/qatomicinteger.html).
We may switch at some point... atomically. 8-)

### inherited constructors

Use sparingly (supported in VS2015). Consider the readability
implications.

### non-static data member initializers

Use sparingly. While very handy, these can hamper readability since you
now need to look in multiple places (the constructor member initializer
list, constructor body, and the member variable declarations) to see
what value member state takes on.

Rule of thumb: If a class has non-inline constructors or is more than
100 lines long, prefer initializing everything in the constructor.

**Good:**

```cpp
class Helper {
  public:
    Helper() {}
    Helper(int baz): baz(baz) {}
    
    int derivedResult() {
        return foo * bar * baz;
    }
    
  private:
    int foo = 1;
    int bar = 2;
    int baz = 3;
};
```

**Avoid:**

```cpp
class SomeClass {
  public:
    SomeClass(int baz); // Defined in some other file.
    
    int derivedResult() {
        return foo * bar * baz;
    }
    
  private:
    int foo = 1;
    int bar = 2;
    int baz = 3;
};
```

### magic statics

C++11 added required thread-safe initialization of static variables.
Prior to C++11, it was possible for multiple threads to initialize a
static concurrently. To prevent this, it was necessary to use a
synchronization helper.

Due to [Bug \#1653368](https://bugs.launchpad.net/bugs/1653368) we build
Mixxx with magic statics disabled on Windows. Until this is fixed, we
cannot rely on magic statics.

### attribute `[[nodiscard]]`

Use it when not checking the return value is a program error like a
memory leak. Don't use it everywhere, like in simple getter functions
where the compiler will discard the call if the return value is not
used.

## specifier `nexecept` 

We follow the Google style guide regarding `noexcept`. In addition the following rules apply:
1. **Use** `noexcept` for on special member functions where recommended by clang-tidy and where it might be used for optimizations using conditions like the [`*_nothrow_*` classes of `<type_traits>`](https://en.cppreference.com/w/cpp/header/type_traits)*
2. **Do not use** on functions where not required for significant optimization or where the compiler can infer noexcept based on the implementation.

*Hints:* 
* you may use `try-catch` in functions that should be `noexcept` when handling the exception is possible and makes sense.
* you may use `noexcept(expression)` for using `noexcept` in templates 

### `gsl::not_null<T*>` checking

When passing pointers via `gsl::not_null<T*>`, make sure to check the
the pointer for `nullptr` explicitly. Otherwise `not_null` might 
terminate the programm, which is fatal in live-situation.

**Good:**
```cpp
#include <gsl/pointers>

void foo(gsl::not_null<T*> pWidget);

void bar(Widget* pWidget) {
    VERIFY_OR_DEBUG_ASSERT(pWidget == nullptr) {
        // safe handling of "unhappy path"
        // since this method just returns void, we can just return
        // but other handling might be required in your case.
        return;
    }
    // depending on context and compiler-optimization the 
    // potentially terminating null-check is even optimized out.
    foo(gsl::not_null<T*>(pWidget));
}

void baz() {
    bar(nullptr);
}
```


**Bad:**
```cpp
#include <gsl/pointers>

void foo(gsl::not_null<T*> pWidget);

void bar(Widget* pWidget) {
    // potentially crash
    // be warry of the implicit conversion too!
    foo(pWidget);
}

void baz() {
    // either guaranteed crash or compile-time error depending on 
    // compiler-optimization
    bar(nullptr);
}
```
