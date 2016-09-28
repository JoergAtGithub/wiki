# Coding Guidelines

## General Philosophy

When you're writing code for open source projects, the most important
rule to follow is this: **Try to make your code blend in with the
existing code.**

When in doubt, use the [Google C++ Style
Guide](https://google.github.io/styleguide/cppguide.html). It's a
treasure trove of C++ advice. Just double Google's indentation -\> 2
spaces become 4 spaces; 4 spaces become 8 spaces.

That being said, there are large chunks of Mixxx that are written in
slightly differing styles (mainly variable naming conventions). In order
to avoid this in the future, it's best for us to have some coding
guidelines for developers to follow.

**As you change a part of Mixxx, please update it to match this style
guide. That way, eventually all of Mixxx will be written in this style.
Do not send us patches that are purely cosmetic with respect to source
changes -- this is a waste of time since it does not benefit users
directly.**

## Tabs vs. Spaces

Mixxx's old developers more or less used the convention that **indents
are 4 spaces**. The consensus is that we should try to stick to this, if
only for consistency.

Please bear this in mind when writing code.

## Line Widths

Please configure your editor to have a max column-width of 80-columns.
While it is not a strict requirement, 80-column cleanliness makes it
easy to tile multiple buffers of code across a laptop screen, which
provides significant efficiency gains to developers. Use double indent
for broken lines or aligne with a "(" in the line above, if that not
results in a 4 space indent.

## Auto-Formater

We currently do not provide an Auto-Formater or Code-Checker.

If you use Eclipse as IDE, the Code Style "K\&R" works well with these
tweaks

  - Tap policy = Space only 
  - New Lines = before colon in constructor initializer list

Please not that there are still some exceptions, so do not autoformat a
whole sourcefile.

# Mixxx C++ Style Guide

This is an overview of the various conventions that the Mixxx team
follows when writing Mixxx code. Most of these conventions are not
intended to start holy-wars, rather they are simply intended to keep the
Mixxx codebase **consistent**. You should strive to follow these
guidelines as much as possible. If you do not, we may ask you to clean
up your code to follow the style guide during code-review.

## Naming

What's in a name?

### Variables

Give variables and classes a descriptive but succinct name.

**Avoid:** Variable names that do not give a hint for their purpose.
**Examples:** ix, i, index, position, name, foo, bar

Local variables should follow either a camelBack case or
lowercase\_with\_underscores style:

``` cpp-qt
QString hotcue_name;
int composerSortOrder;
```

Pointers should be prefixed with a "p" to indicate they are a pointer.
The "\*" should be aligned with the type and **not** the name.

**Examples:**"

``` cpp-qt
int* pHotcueIndex;
```

Optionally include minimal type information with variables. This can be
handy to know at a glance the rough type of an object. For example, for
a [ControlObject](ControlObject) a common pattern is to prepend "CO" to
the variable name:

``` cpp-qt
ControlObject* m_pCOPlayButton;
```

### Classes

  - Class names must be in CamelCase (e.g. "MyName"), with each word
    capitalized. 
  - Member functions of classes must be camelBack cased (e.g.
    "thisFunction") 
  - Member variables **must** be prefixed with "m\_". It is essential to
    know the scope of a variable is at the class-member level with a
    simple glance for easy readability of source files.
  - Class variables (static class members) **must** be prefixed with
    "s\_".

## Braces

Braces should not be given their own newline. They should always be
separated from surrounding code by a single space.

**Good:**

``` cpp-qt
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

``` cpp-qt
if (expression)
{
}
else
{
}
```

## If Statements

One-line statements following an `if` clause are acceptable, but it is
preferable to wrap them in braces since someone may add a line at the
same indentation level, not realizing that there are no braces.

**OK:**

``` cpp-qt
if (expression)
    statement
```

There should be one space following the `if` keyword, and one space
following the closing parenthesis of the condition before the brace.

**Better:**

``` cpp-qt
if (expression) {

}
```

Do not add padding inside the conditional or omit a space between the
`if` keyword and the conditional parenthesis.

**Bad:**

``` cpp-qt
if( expression ){

}
```

## For Loops

Similarly to `if`-statements, there should be a single-space of padding
after the `for` keyword and after the closing conditional parenthesis.
Additionally, a single-space padding should come after the semicolon
separators between the initializer, conditional, and increment
statements.

**Good:**

``` cpp-qt
for (initializer; conditional; increment) {

}
```

## Comments

Use C++-style comments only. Do not use C-style comments or Java-syle
comments. Comments should be complete, descriptive sentences in the
present tense. If a comment is a warning or something that might need to
be re-evaluated in the future, date the comment with the current month
and year, along with your username.

**Good:**

``` cpp-qt
// This is required because we don't have enough foo's in the bar -- rryan 2/2011
doSomething();
```

Plain-text comments should be separated from the comment symbol by a
single space. Commented-out code should have no space between the
comment symbol and the code:

**Good:**

``` cpp-qt
// Textual comment
//if (thisSectionIsDeprecated) {
//    // Do something crufty
//}
```

**Bad:**

``` cpp-qt
//Textual comment
// if (thisSectionIsDeprecated) {
//     // Do something crufty
// }
```

Avoid comments that do not add more information than the words contained
in the statement that follows them. Instead, write a descriptive summary
of what the following lines accomplish.

**Bad:**

``` cpp-qt
/* init boofar */
initBoofar();
```

**Bad:**

``` cpp-qt
/*
 * Java-style comment
 */ 
thisCommentIsReallyVerboseFactoryMethodInjectorObserver()
/* C-style comment -- avoid because you can't nest them */
```

### TODO's

If you'd like to leave a `TODO` for yourself, format them like this:

``` cpp-qt
// TODO(rryan) Make sure to double-check this.
```

If you'd like to leave a general `TODO` for the team, use the name
`XXX`:

``` cpp-qt
// TODO(XXX) Make this more general
```

Remember to actually go back and investigate your `TODO`'s :).

**Bad:**

``` cpp-qt
// TODO Make this more general
```

## C++ Header Files

This section outlines our various standards for writing header (.h)
files.

### Credit and License

If you wish to credit yourself and leave a notice for who people should
contact for help about a file, do so in the most brief way possible. Do
not insert ASCII art. Do not include a copyright notice, or license
because the project has a root LICENSE file which covers these
declarations, and so any file-level declarations would be redundant.

``` cpp-qt
// filename.h 
// Created 2/21/2011 by RJ Ryan <email> 
```

### ifndef guard

The \#ifndef guard should be the filename with the dots replaced with an
underscore.

``` cpp-qt
#ifndef LIBRARY_H
#define LIBRARY_H

#endif
```

### includes

File includes should be done in the following order:

1.  System Includes
2.  Qt Includes
3.  Includes of Mixxx library dependencies
4.  Mixxx local includes
5.  Class forward-declarations

Each different group of includes should be separated by a single empty
line. **Order the includes in alphabetical order.** Relative includes
**should never be used**. Always include Mixxx local files by specifying
them from the root of the `src` folder. Do not forward declare any
classes other than Mixxx project classes.

**Example:**

``` cpp-qt
#include <math.h>
#include <sys/types.h>

#include <QtCore>
#include <QtDebug>
#include <QTreeView>

#include <taglib/taglib.h>

#include "library/library.h"

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

``` cpp-qt
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
    void bindWidget(WLibrarySidebar* sidebarWidget,
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

### GOTO

Using the `goto` statement is not allowed. Typically uses of `goto` are
better handled by the C++ idiom of [Resource Acquisition Is
Initialization](http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization).

### virtual

The *virtual* modifier is inherited by all implementations of that
method in derived classes. Keep redundant virtual keywords in derived
function implementation for documentation purpose.

## C++11

As of the Mixxx 2.0 release, Mixxx is switching to C++11. We are taking
a conservative approach to adopting C++11 features and whitelisting them
one by one. If a C++11 feature you would like to use is not listed here,
please email mixxx-devel to make a case for it and we will consider
whitelisting it.

We are limited to what is supported across our 3 supported compilers:

  - [Clang 3.3](http://clang.llvm.org/cxx_status.html)
  - [GCC 4.8](https://gcc.gnu.org/projects/cxx0x.html)
  - [Microsoft Visual
    Studio 2013](https://msdn.microsoft.com/en-us/library/hh567368.aspx)

In general, Microsoft Visual Studio is the one that prevents us from
using features.

See also: [C++11 features in
Qt5](http://woboq.com/blog/cpp11-in-qt5.html).

### initializer lists

<http://en.cppreference.com/w/cpp/language/list_initialization>

Use with caution\!

**WARNING** on windows, they are not well supported with QT4. see the
following links for details

  - <https://sourceforge.net/p/mixxx/mailman/message/34805913/> 
  - <https://bugs.launchpad.net/mixxx/+bug/1627826> 
  - <https://github.com/mixxxdj/mixxx/pull/1019> 

### static\_assert

Use\!

### nullptr

Yes\! Always prefer to NULL.

### unique\_ptr / std::move

Yes\! Prefer to QScopedPointer.

By including the custom file "util/memory.h" instead of the system
header \<memory\> you are even able to make use of
std::make\_unique\<\>() that was missing from the C++11 specification
and is now provided by C++14. This generic function should always be
used instead of *operator new* for the allocation of objects that are
wrapped in a *unique\_ptr*.

### default / delete functions

Use.

### delegating constructors

Use.

### constexpr

**Not Supported in Microsoft Visual Studio**. Blame Microsoft.

Use
[Q\_DECL\_CONSTEXPR](http://doc.qt.io/qt-5/qtglobal.html#Q_DECL_CONSTEXPR)\!
On compilers that support it, a constexpr will be used. Otherwise it
will be evaluated at runtime. Be careful since this means that you're
relying on the compiler to optimize it out.

### unicode string literals

**Do Not Use**. Use
[QStringLiteral](http://doc.qt.io/qt-5/qstring.html#QStringLiteral).

Blame Microsoft.

### right angle brackets

<http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2005/n1757.html>

Yes\!

### override / final

Use\! Any case where a method intentionally overrides that of a parent
class should use the *override* keyword.

In contrast to the pre-C++11 rules (see above) when using *override* on
a function in a derived class it is recommended to omit the redundant
*virtual* keyword, because *override* implies *virtual*.

Destructors in derived classes should also be marked with *override*
instead of *virtual*. This ensures at compile time that the base class
has declared a *virtual* destructor. If the base class has not declared
a *virtual* destructor the destructor of a derived class might not be
invoked.

### alignment

**Use carefully.** MSVC only supports some of the C++11 alignment
keywords:

> Alignment: Neither VC10 nor VC11 implement the Core Language keywords
> alignas/alignof from the alignment proposal that was voted into the
> Working Paper. VC10 had aligned\_storage from TR1. VC11 adds
> aligned\_union and std::align() to the Standard Library.

### cstdint

Appears to be supported by MSVC 2013. Use\!

### range-based for loops

Use them\! Prefer them over Qt's `foreach` macro which has enjoyed
widespread usage throughout the Mixxx codebase.

``` cpp-qt
for (const QString& item : list) {
  qDebug() << "WOOHOO" << item;
}
```

### auto

We do not follow a aaa-style (almost-always-auto).

Our rules of thump:

  - use auto to prevent repeating yourself
  - auto when the type is long and does not add any value

Auto is acceptable in function-level scopes (i.e. only within function
bodies. Do not use auto in a function or method prototype as this makes
the code less self-documenting and would require reading the body of the
function to determine its return type or arguments.

More details can be found here:
<https://google-styleguide.googlecode.com/svn/trunk/cppguide.html#auto>

Good:

``` cpp-qt
void mixAudio(const QVector<QString>& values, QVector<EngineChannel*>* channels) {
  auto bufferSize = 256; // this avoids uninitialised locals
  
  for (const auto& value: values) { // Type can't get wrong 
      qDebug() << "blah:" << value;
  }
  
  for (auto* channel: *channels) {
      channel->process(bufferSize);
  }
}
```

Bad:

``` cpp-qt
auto mixAudio(const QVector<QString>& values, QVector<EngineChannel*>* channels) -> bool {
    return true; // need to read the function body 
}
```

Bad:

``` cpp-qt
auto value getValue(); // because the type is out of sight
```

Bad:

``` cpp-qt
QVector<RowInfo>::iterator it = rowInfo.begin();
// Explicit type is only clutter and can be easily guessed from the context. 
```

Bad:

``` cpp-qt
QList<int>* pList = new QList<int>(); // do not repeat yourself 
```

### closures / lambdas

Use carefully\! Closures can obscure the control flow of a system and
introduce tricky data lifetime issues. Using a lambda in your code will
require more time in code review and you may be asked to re-write the
code to avoid the usage by your code reviewer. Before using a closure,
please consider whether it's truly necessary.

Use 8 space indent for line break or reasonable alignment + 4 indent for
a new logical block. Allays beak after "},"

**Good:**

``` cpp-qt
    m_pTrackCollection->callSync(
            [this](TrackCollectionPrivate* pTrackCollectionPrivate) {
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

In general, do not use.

**Note:** *auto&&* is a universal reference and not an r-value
reference\! It should be used instead of an explicit l-value *auto&*
reference in *range-based for loops* over non-const (= mutable)
containers as shown below.

**Good:**

``` cpp-qt
for (auto&& item: mutableContainer) {
  // read and write item
} 

for (const auto& item: immutableContainer) {
  // read only item
} 
```

The universal reference *auto&&* could be used in both cases, but prefer
*const auto&* if you don't intend to modify the item inside the loop's
body.

### forward declared / strongly typed enums

Use.

### atomics

For now, prefer using Qt atomic primitives. We may switch at some
point... atomically. 8-)

### inherited constructors

Do not use -- [not supported in
VC2013](https://msdn.microsoft.com/en-us/library/hh567368.aspx), which
our build system and many windows developers rely on.
