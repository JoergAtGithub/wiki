# Crate Enhancements

*by Anastasis Grammenos* (gramanas)

<span class="underline">Email:</span> <anastasis.gramm2@gmail.com>

[This](https://drive.google.com/file/d/0Bx6GQqCGx6HhdzJHaHVRdWt5aU0/view?usp=sharing)
is the final proposal with witch I got accepted as a participant in GSoC
2017.

**<span class="underline">Current State</span>**

  - Currently coding the Nested Crates feature. ([More
    details](https://gramanas.github.io/website/NestedCrates.html))

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

This will be developed on top of [Library
Redesign](https://github.com/mixxxdj/mixxx/pull/1117). With that in mind
I'd like to add some notes on the implementation of the Nested Crates.

  - `TreeItemModel` will be used for the nesting purposes.
  - A new table in the database will hold the parent child relationship
    and aplly the nessecary restrictions. (Child can't be parent of it's
    parent nor itself)

### General Notes

  - Crates can hold songs AND other crates.
  - There is no limit to how deep you can get.
  - A child can't have it's parent or it's parent's parent (etc) as a
    child.
  - When the user picks a crate up the hierarchy it's implied that he
    wants all the songs under that crate AND the nested ones under it.
  - The above serve as a custom tagging system for DJ's to organise
    their music library in every way imaginable.

### Database

For the nested crates to work, we need a viable option to save them in
the database.

  - [Stack Overflow's
    opinion](https://stackoverflow.com/questions/4048151/what-are-the-options-for-storing-hierarchical-data-in-a-relational-database)
  - [What we'll
    implement](http://dirtsimple.org/2010/11/simplest-way-to-do-tree-based-queries.html)

Basicaly I'll add a table

'' | ParentID | ChildID | Depth | ''

exaclty as in the example above.

Also I'll add a table with columns `| CrateID | path |` where path is a
string that will get generated whenever the user updates the database by
creating/moving/renaming/deleting a crate. This will be used in the
crate: filter witch will itself be used to replace the way the crates
are currently displayed (by generated a query just like in the new
library redesign).

### Crate Filter

Since the way the user selects crates will change to reflect the way the
rest of the library works, here I'll describe how the filter will work
for the nested crates.

Consider the following example:

  - Metal 
  - Progressive

<!-- end list -->

``` 
    * Instrumental
* Alternative
* Rock
* Instrumental
  
```

After each modification of the crate database by the user
(add/delete/move/rename a crate), a string will be generated for each
crate from the first table I mentioned above, and get stored to the path
table, witch will correspond to the "path" of the crate in the tree.
This path is actually quite useful.

It will look like this for the examples above:

`/Metal`  
`/Metal/Alternative`  
`/Metal/Progressive`  
`/Metal/Progressive/Instrumental`  
`/Rock`  
`/Rock/Instrumental`  
The text the user has inserted after `crate:` filter will get matched to
this string, so that the user can narrow down his search either by
typing `crate:rock crate:instrumental` *(Here I assume that the
different filters are joined together by `AND`)* or
`crate:rock/instrumental` to get everything under rock/instrumental.
Also since the new library has an exact filter match I will also add an
exact crate filter `crate:=` for consistency.

\* To get all the instrumental tracks of this library the user naturally
searches for `crate:instrumental`

### Crate Tree Model

All these will be shown to the user as a tree structure (again like the
new library) using the same method used by the tracks. When a user
selects a crate, a query will get generated to narrow the users view of
the library to the crate that he/she selected using the `path` variable
described above.

While the user organises the library, he/she might want to see only the
tracks under crate `/Metal` but not those in the nested crates
underneath. For this a checkbox will be implemented next to the tree.
When checked it will change the query generated by the action of
clicking a crate to something else that will only list the tracks under
`/Metal`. This will be the exact crate filter `crate:=` that matches
it's argument exactly to the path, so `/Metal` crate gets returned but
not `/Metal/Progressive` or `/SomeOtherCrate/Metal`

#### Implementation

I think a nice way to create the tree is to use the paths of each crate.

Using the closure table I can get all the ancestors of a crate sorted by
depth. Then it's just a matter of iterating through them and appenind
them to the end of a string.

Next the `TreeItemModel` will read the paths table and for each crate if
it has a previous crate in it's path insert it there as a child, else
insert it at the top.

You can be sure that every time you add a child the parent is already
there, because this whole think is sorted alphabetically (Just like the
example with the paths above - In order for `/Metal/Alternative` to be
added it must come after `/Metal`).

# Timeline

<span class="underline">**May 15 - June 5**</span>

  - Crate Filter
  - Crate Filter Tests

<span class="underline">**June 6 - June 15**</span>

  - Plan for Nested Crates implementation
  - Familiarize with the new library layout
  - Start coding the new way to select crates (via query)

<span class="underline">**June 16 - June 26**</span>

  - Get ready for the first evaluation
  - Start modifying the database adding triggers and the new table

<span class="underline">**June 27 - July 20**</span>

  - Start work on the tree model
  - Add lmitations to the database
  - Start tweaking the filter and the way crates are selected

<span class="underline">**July 20 - July 28**</span>

  - 2nd evaluation

<span class="underline">\*\*July 29 - \*\*</span>

  - *TBA*

# Weekly Devlog

In this section I will mark my progress with a weekly report about the
stuff I've been up to with mixxx.

Since I am starting this at June 13 here is a summary of what has been
done so far:

  - [Crate filter](https://github.com/mixxxdj/mixxx/pull/1263) is merged
    in master.
  - [Crate filter tests](https://github.com/mixxxdj/mixxx/pull/1277) as
    well.
  - There were some issues with the filters with the new library
    redesign and here is

<!-- end list -->

    the now merged PR at [[https://github.com/daschuer/mixxx/pull/19|daschuer's repo]] to fix them.

<span class="underline">**June 12 - June 19**</span>

This week has been pretty slow. I got finals at the moment so I spend
some of my time studying.

After the merge of the recent master commits to the new library redesign
a SearchQueryParser test was failing, so since I want to start working
on the new filter for the nested crates I had to fix it.

After some discussions we decided to change the filter functionality
from what it used to be, in order to work better with the library query
helper that generates the queries when the user selects something from
the new library column. Used to be that `artist:""` for example would
return all the library since it's just an empty filter. Now in order for
the user to be able to narrow down to songs with NULL artist `artist:""`
returns just that (Unknown artist).

This was already implemented but in a slightly wrong way, so the test
failed.

The [pull request](https://github.com/daschuer/mixxx/pull/19) got merged
and now I am ready to start working on the crates themselves.

Next will I'll delve into the `CrateFeature` code. From what I
understand a tree item model is already in use for the crates, it's just
that there are no levels.

<span class="underline">**June 19 - June 26**</span>

I started with modifying the database and adding the aforementioned
tables for the crate hierarchy.

Since everything is at a testing phase for now I have them embedded in
the code as crate storage functions that create the tables and insert
the data to them.

The closure table works really fine, and I've been able to generate
paths for the nested crates as well.

The next step for the database is to implement ways to check that the
hierarchy follows the rules. (No same name children etc...)

Now my goal is to use the paths to create the tree. For that I've
created a `CrateTreeModel` that derives from `TreeItemModel` and will
handle the drawing of the tree just like `mixxxlibraryfeature`.

<span class="underline">**June 26 - July 3**</span>

I got the tree structure working with my dummy database. So I have the
DB mockup and the UI mockup. The problem is that this is untestable to
everyone else but me.

I'll work on solving that by providing functions to insert child crate
and such. This is far from the final product, in witch you can freely
move crates to other crates to change their parents etc.

I hope by the end of the following week I'll have a work in progress PR.

<span class="underline">**July 3 - July 10**</span>

I opened a PR with the progress I made
[here](https://github.com/mixxxdj/mixxx/pull/1304) I am wondering if the
way I do things leaves a big impact on memory.

The next step is to tie the filter the the crates feature. Selecting a
crate will generate the correspoding filter search just like the
libraryfeature. For starters I'm gonna have to understand the current
way crates are being displayed and then alter it.

I am very happy with the progress so far. I hope I'll have the filter
working by next week.

<span class="underline">**July 10 - July 17**</span>

<span class="underline">**July 17 - July 24**</span>

<span class="underline">**July 24 - July 31**</span>

<span class="underline">**July 31 - August 7**</span>

<span class="underline">**August 7 - August 14**</span>

<span class="underline">**August 14 - August 21**</span>

<span class="underline">**August 21 - August 28**</span>
