**NOTE:** This document is work in progress. [GameGod](/User/GameGod)
07:40, 6 June 2007 (PDT)

# Coding Guidelines

## General Philosophy

When you're writing code for open source projects, the most important
rule to follow is this: **Try to make your code blend in with the
existing code.**

When in doubt, use the [Google C++ Style
Guide](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml).
It's a treasure trove of C++ advice.

That being said, there are large chunks of Mixxx that are written in
slightly differing styles (mainly variable naming conventions). In order
to avoid this in the future, it's best for us to have some coding
guidelines for developers to follow.

## Classes and Members

  - Class names follow the "MyName" format, with each word capitalized. 
  - Member functions follow the usual "thisFunction" naming convention. 
  - Private variables throughout the class should ideally start with
    "m\_", and although this hasn't been followed thus far, it's a good
    idea to use it because it tells you the scope of a variable without
    having to dig through a header file.

## Tabs vs. Spaces

Mixxx's old developers more or less used the convention that **indents
are 4 spaces**. The consensus is that we should try to stick to this, if
only for consistency.

Please bear this in mind when writing code.

## General tips

## Engine Coding Guidelines

The mixing engine code inside Mixxx needs to run in realtime and must
execute as quickly as possible in order to minimize the chance of buffer
underruns in the soundcard.

Here's some coding tips to help keep performance decent:

  - Don't use signals/slots in code that gets called in the callback
    thread - that is, use signals/slots to interact with any
    EngineObject's process() function.
  - Don't access ConfigKeys in code that gets called in the callback
    thread (same as above).
