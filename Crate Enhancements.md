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

***TBA***
