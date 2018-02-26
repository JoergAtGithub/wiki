# Crate Enhancements

*by Anastasis Grammenos* (gramanas)

<span class="underline">Email:</span> <anastasis.gramm2@gmail.com>

[This](https://drive.google.com/file/d/0Bx6GQqCGx6HhdzJHaHVRdWt5aU0/view?usp=sharing)
is the final proposal with witch I got accepted as a student in GSoC
2017.

## GSoC 2017 recap

### Introduction

It's been a real pleasure working on this c++ software this summer, I
got hands on with a huuuge project and I somewhat understood how things
would work in a production environment. I learned a lot about the
database and how to interact with it though code, and maybe most
importantly I've learned the value of objects in OOP and how to use them
correctly to abstract away details that other classes shouldn't care
about.

Before I was accepted I was skimming through the code to see what I
would have to face in case I got in, and I was really unsure if I'm
gonna make it. It turns out it's a lot easier than it seems. You just
have to have a plan, work slowly and carefully and take note of your
progress. [Org Mode](http://orgmode.org/) really helped me to plan out
my algorithms in plain words and to keep track of what I've done so far
in the sometimes big files I had to deal with.

My two mentors also helped a lot, each in their own way, both with our
private conversations and with their comments on my PRs, and also by
contributing code to other areas of mixxx that affected my project. I
cate to appreciate OSS a bit more cause of them, and for that I have to
thank them\!

### The work I've done

Througout the summer I made a revamp to the crates subsystem. I
redisigned the class that manages crates, I added support for the
nesting features and I created a crate filter to use in the library.

These are the PR's I've made for this project:

  - [Crate filter](https://github.com/mixxxdj/mixxx/pull/1263)
  - [Crate filter tests](https://github.com/mixxxdj/mixxx/pull/1277)
  - [Small issues](https://github.com/daschuer/mixxx/pull/19)
  - [Nested Crates](https://github.com/mixxxdj/mixxx/pull/1304)

The last one changed the filter to it's current state in order to work
recursively.

All the work I've done is based on gsoc 2016 [Library
redesign](https://github.com/mixxxdj/mixxx/pull/1117) witch at the
moment of writing is not yet ready to ship and is in need of further
developement. This means that the nested crates feature will be delayed
until developement of the library redesign is finished. Witch brings us
to my final point.

### What remains to be done

The current model used for the tree view of the library doesn't support
what I call "dynamic expansion". Dynamic expasion is the ability to
insert new items in the tree or change the current ones (rename/remove)
without the need for the whole tree to be reloaded (witch results in the
folding of the tree).

It also doesn't support internal drag and drop(Drag one crate to
another). For this to work the tree items might need to also adapt to
support internal drag and drop.

I think the tree item model should be expanded to support those
features. This needs to happen carefully due to the fact that the tree
item model is used by other library features that don't need the extra
stuff (d\&d, dynamic expansion) to work.

The following are the ideas for the project, and the devlog where I was
writing what happened each week.

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

Basically I'll add a table

'' | ParentID | ChildID | Depth | ''

exactly as in the example above.

Also I'll add a table with columns `| CrateID | path |` where path is a
string that will get generated whenever the user updates the database by
creating/moving/renaming/deleting a crate. This is used to format the
tree of the crates.

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

When the user types some letters after `crate:` a query is executed that
joins the closure table with the crates table and returns all the crate
id's that match this word and all their children. Then using these id's
it finds the tracks and displays them just like any other filter.

The user can narrow down his search either by typing `crate:rock
crate:instrumental` *(Here I assume that the different filters are
joined together by `AND`)* to get everything under rock/instrumental.

To get all the instrumental tracks of this library the user naturally
searches for `crate:instrumental`

### Crate Tree Model

A similar procedure to the filter is used when selecting a crate from
the tree. Instead of relying to the crate's name this time we have
access to it's id so we use it instead to find the children.

While the user organises the library, he/she might want to see only the
tracks under crate `/Metal` but not those in the nested crates
underneath. For this a special tree item has been implemented next to
the tree that acts like an toggle switch. When it's on the crates are
shown recursively using the method I described above, when it's off it's
similar to how it used to work, where you only see only the crate and
not it's children.

#### Implementation

I think a nice way to create the tree is to use the paths of each crate.

Using the closure table I can get all the ancestors of a crate sorted by
depth. Then it's just a matter of iterating through them and appending
them to the end of a string.

Next the `CrateTreeModel` will read the paths table and for each crate
if it has a previous crate in it's path insert it there as a child, else
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
  - Add limitations to the database
  - Start tweaking the filter and the way crates are selected

<span class="underline">**July 20 - July 28**</span>

  - 2nd evaluation

<span class="underline">**July 29 - August 15**</span>

  - Finish the recursive aspects of the nested crates

<span class="underline">**August 15 - August 30**</span>

  - Testing and final tweaking 

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

After the merge of the recent commits to the new library redesign a
SearchQueryParser test was failing, so since I want to start working on
the new filter for the nested crates I had to fix it.

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
crate will generate the corresponding filter search just like the
libraryfeature. For starters I'm gonna have to understand the current
way crates are being displayed and then alter it.

I am very happy with the progress so far. I hope I'll have the filter
working by next week.

<span class="underline">**July 10 - July 17**</span>

Well I haven't touch the filter yet\!

There is some discussion regarding `TrackCollection` class and how it
will interface with `CrateStorage`/`CrateHierarchy`.

For now I've split the `CrateStorage` file taking away all the helper
classes and puting them inside `CrateStorageHelper.h` and also merged
`CrateHierarchy` into it.

ATM `CrateStorage` handles all the data writing and reading regarding
crates. This results to a huge file \~900 lines, witch is bound to get
bigger. I could split it into write and read operations or maybe there
is a better approach, but it's an issue that has to be addressed before
any real work can be done regarding the hierarchy features
(move/delete).

I got limited time available until the end of the month (summer job to
pay the bills), and in the two weeks left, I would like to have the
filter search work, at least at an experimental stage. I would also like
to figure things out with `CrateStorage` and move on to the recursion
stuff.

With August approaching I'm confident the nested crates feature will be
completed in time.

By the way, I've found
[this](https://www.percona.com/blog/2011/02/14/moving-subtrees-in-closure-table/)
it might help in the weeks to come.

<span class="underline">**July 17 - July 24**</span>

This week the focus was on refactoring `CrateStorage` to make it easier
to maintain and read through the code, with classes that (I hope) make
more sense.

The changes made are described
[here](https://github.com/mixxxdj/mixxx/pull/1304#issuecomment-317280988)
but I'll copy-paste them here for better readability.

`CrateStorage` was refactored into 5 new files:

  - `CrateStorageHelpers`
  - with the helper functions like CrateSelectResult
  - `CrateManager`
  - general manager for crates initialized at TrackCollection
  - `CrateStorage`
  - handles the crate storage data read/write
  - `CrateHierarchy`
  - handles the crate hierarchy data read/write
  - `CrateTracks`
  - handles the crate tracks data read/write

The biggest challenge of course was the design of the architecture. I
settled in the classes above by trying to keep each separate crate
related data access to the DB to it's own class. When I read through the
code I think it's easier to understand what does what.

<span class="underline">**July 24 - July 31**</span>

This week I implemeted a couple of new features for the nested crates.

  - Crate Filter

Finally I've implemented crate filter using the crate `namePath` witch
enables the recursive view of the crates.

Also just like `tracksFeature` selecting the crate will invoke the
corresponding filter search and that's how the crate is displayed.

The whole process seems to me a bit clumsy but it works for now. I am
thinking of ways I can improve that.

  - Duplicate crate

Duplicating a crate now makes a duplicate at level 1, containing just
the tracks of this crate.

  - Rename Crate

Here I optimised the way the crate naming works to secure the database
from corrupted entries (same name in different crate, hierarchy naming
conventions, etc)

Also you can freely rename crates while making sure the database won't
break.

Also I fixed various small details and made little optimisations here
and there.

Now about moving crates, I feel like it's a lot of effort for a feature
not really that useful. The naming conventions will be really hard to
enforce. Instead of moving crates you could just create them from
scratch or rename them to what you want them to be.

I am thinking about being able to move only the level 1 crates so the
workflow would be like: duplicate \> move to position but it might be a
bit confusing to the end user.

<span class="underline">**July 31 - August 14**</span>

I re implemented the crate filter and it no longer works with paths. It
now uses the closure table. I found the new one to be a bit faster and
it will also be much more stable in it's results because it doesn't rely
on a path string like before and uses the closure table to get it's
results.

I also changed the naming conventions according to what we think the
user will expect. You can name a crate whatever you want except:

  - The name of it's parent
  - The name of any of it's siblings (same level as the one we are
    creating/renaming and with the same parent)
  - The name of it's immediate children (direct children of a crate)

So it's basically more like a file system but you can't do this:
`/aName/aName/aName` You can do this however (if you feel like it):
`/aName/anotherName/aName`

I added the crate summary that existed before to give some info for each
crate.

Also if you rightclick a track and then add to crate, it now displays
the crate path so the user can distinguish one crate from the other.

The feature works great so far, and I can't make it crash mixxx or slow
the performance. Even with 15k tracks the crate queries take 100-150ms
with the setup of \~50 crates.

<span class="underline">**August 14 - August 28**</span>

These last weeks I've been cleaning the code here and there, while I've
also added some new features.

Moving crates throughout the tree is now possible via a right click
menu, witch displays only the valid positions you can move the selected
subtree. I found
[this](https://www.percona.com/blog/2011/02/14/moving-subtrees-in-closure-table/)
sometime ago, witch provided me with a really god way of moving subtrees
in a closure table via sql queries, and it proved to be real easy to
implement, after I figured out how to do it in sqlite instead of mysql.

While moving crates I encountered the problem of a user moving a crate
to a parent with the same name. Instead of throwing an error I decided
to just add a "\_" to the end of the crate's name. I made it so that no
matter what you can't break the naming conventions.

I also corrected the failing crate filter tests.
