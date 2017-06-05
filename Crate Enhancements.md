# Crate Enhancements

*by Anastasis Grammenos* (gramanas)

<span class="underline">Email:</span> `anastasis.gramm2@gmail.com`

[This](https://drive.google.com/file/d/0Bx6GQqCGx6HhdzJHaHVRdWt5aU0/view?usp=sharing)
is the final proposal with witch I got accepted as a participant in GSoC
2017.

**<span class="underline">Current State</span>**

  - [Crate filter](https://github.com/mixxxdj/mixxx/pull/1263) is merged
    in master.
  - There is an open PR for [crate filter
    tests](https://github.com/mixxxdj/mixxx/pull/1277).
  - Currently planing for the Nested Crates feature.

## Crate Filter

A new filter is added in mixxx's search bar. User can now type `crate:`
and anything after that will get matched with the crates the user has
created, and display the results.

### Implementation

First of all a new search filter node was created to handle the crate
filtering. It is called `CrateFilterNode`. Since the crates each song is
in can't be found by the `library_cache_view` that `mixxxlibraryfeature`
provides I had to create a workaround in order for `match()` and
`toSql()` to work.

`cratestorage` handles all the crate related database access, so I added
a few functions there to generate/run the SQL required both by `match()`
and `toSql()`.

Then `searchqueryparser` got modified to recognise the `crate` keyword
and through the `CrateFilterNode` generate the correct SQL query to get
the trackIds of the songs matching the crate the user has entered.

## Nested Crates

This will likely be developed on top of [Library
Redesign](https://github.com/mixxxdj/mixxx/pull/1117). With that in mind
I'd like to add some notes on the implementation of the Nested Crates.

  - [QT Tree
    Model](http://doc.qt.io/qt-5/qtwidgets-itemviews-simpletreemodel-example.html)
    will be used for the nesting purposes.
  - A new table in the database will hold the parent child relationship
    and aplly the nessecary restrictions. (Child can't be parent of it's
    parent nor itself)

## Timeline

<span class="underline">**May 15 - June 5**</span>

  - Crate Filter
  - Crate Filter Tests

<span class="underline">**June 6 - June 15**</span>

  - Plan for Nested Crates implementation
  - Familiarize with the new library layout

<span class="underline">**June 16 - June 26**</span>

  - Get ready for the first evaluation

<span class="underline">\*\*June 27 - \*\*</span>

  - *TBA*
