# GSoC-2013 Status page for project "Non-Blocking Database Access"

**Student:** Nazar Gerasymchuk (email: nazar.gerasymchuk at gmail.com,
IRC: tr0)

**Mentor:** Daniel Schürmann (email: daschuer at mixxx.org, IRC:
daschuer)

# My blogs

You can find me there, and contact me through blogs comments:

  - <https://nonblockingdb.wordpress.com/> (EN) -- blog for news on my
    developing process at GSoC 2013.
  - <http://neval8.wordpress.com/> (EN, UA) -- my personal blog with
    tips'n'tricks, hacks and so on.

-----

# What plans do I have for this summer?

1.  Improve my Git skills
2.  Get involved in developing of Mixxx
3.  Solve different bugs on Mixxx
4.  Build new scheme for database access in Mixxx
5.  Test that scheme, try to find bottlenecks, possible deadlocks...
6.  Code that scheme separate from Mixxx
7.  Write documentation on scheme
8.  Apply that scheme to Mixxx
9.  Test Mixxx with my scheme
10. PROFIT :)

# Weeks schedule / Tasks

In general, I see two milestones:

1.  Before midterm: prepare separate working prototype for db access.
2.  Before finalterm: merge prototype into Mixxx.

<!-- end list -->

1.  **Week *(17.06 -- 23.06)***
    1.  Write down this schedule.
    2.  Write article *"Overview of all what we have in Mixxx (Qt,
        SQLite, threads, …). What to do with it?"*:
        <https://nonblockingdb.wordpress.com/2013/06/19/overview-of-all-what-we-have-in-mixxx-qt-sqlite-threads-what-to-do-with-it/>.
    3.  Fork Mixxx on GitHub.
2.  Week *(24.06 -- 30.06)*
    1.  Dig into Sqlite and define or find some suitable test cases.
    2.  Dig into Mixxx and find all usage of db access, analyze it.
    3.  Prepare UML class dias.
    4.  Solve some bugs.
3.  Week *(01.07 -- 07.07)*
    1.  Write tests using "QtTestLib" framework.
    2.  Begin writing documentation.
    3.  Solve some bugs.
4.  Week *(08.07 -- 14.07)*
    1.  Writing the specs for a possible solution.
    2.  Create separate repo for prototype.
    3.  Solve some bugs.
5.  Week *(15.07 -- 21.07)*
    1.  Start implementing of prototype database access class with
        separate test project.
    2.  Solve some bugs.
6.  Week *(22.07 -- 28.07)*
    1.  Add and test all possible ways of database usage present in
        Mixxx handled by DAO.
    2.  Solve some bugs.
7.  Week *(29.07 -- 04.08)* 
    1.  Finish prototype that is able to handle asynchronous db access,
        ..., flexible and extendable.

<!-- end list -->

  - **Important date** *29.07* -- Begins midterm deadline
  - **Important date** *20.08* -- Midterm deadline
  - **For midterm** I'll prepare separate prototype project on separate
    repo.

<!-- end list -->

1.  Week *(05.08 -- 11.08)*
    1.  Plan (re-plan) schedule of work for finalterm.

<!-- end list -->

``` 
  - 
  - Solve some bugs.
- Week //(12.08 -- 18.08)//
  - 
  - Solve some bugs.
- Week //(19.08 -- 25.08)//
  - Solve some bugs.
  - 
- Week //(26.08 -- 01.09)//
  - Solve some bugs.
  - 
- Week //(02.09 -- 08.09)//
  - Solve some bugs.
  - 
- Week //(09.09 -- 15.09)//
  - Iron out remaining bugs.
  - Merge my branch with master.
- Week //(16.09 -- 22.09)// 
* **Important date** //16.09// -- Pencils down begins
- Week //(23.09 -- 29.09)// : 
* **Important date** //27.09// -- Finalterm deadline
- 01.10 : end
```

# Current status

Currently I'm working on:

1.  Extended article to collect as much as possible information about
    project and how to solve it:
    <http://nonblockingdb.wordpress.com/2013/06/19/overview-of-all-what-we-have-in-mixxx-qt-sqlite-threads-what-to-do-with-it/>
2.  My very approximate roadmap for this summer:

**Roadmap:**

  - Learn SQLite deeper as Daniel pointed (learn sources of SQLite
    multi-threading).
  - Fork Mixxx on GitHub
  - Create empty class `DBAccessor`
  - add own class inherited from `QThread`, named, for example,
    DBAccessor
  - create handmade `DBAccessor`'s event-loop (like `while(1)`...)
  - make class `DBAccessor` Singletone and all-source-wide
  - make `DBAccessor` instantiate on Mixxx startup
  - code freeing `DBAccessor` on Mixxx exit
  - Code `DBAccessor`'s queue manager
  - code placing query into queue
  - code controlling on executed queries
  - code removing from queue 
  - ...
  - Code `DBAccessor`'s minimal access to SQLite db
  - *(Think first on how to)* Organize `DAO`'s names, priorities, and so
    on so we can send it as parameter to `DBAccessor`

-----

# Tasks

## Original task: Non-Blocking Database Access

Currently some database transactions are stalling the GUI. This is
because some database queries are preformed from the GUI thread.

This should be solved during the project by something like a standard
non blocking interface to sqlite. All Database queries should be issued
though this new interface.

This project would make Mixxx more reliable by this new concept how to
deal with database actions.

Your proposal should include a draft proposal how do you will achieve
the goal. You should have already have experience in parallel processing
and sqlite.

## My proposal

Let’s use RPC-style pure callbacks. I can propose to create class
`DBManager`. `DBManager` will be a singleton and it will be instance in
separate thread (inherited from `QThread`). This class will have own
event loop. Also it will have queue of queries and pointers to `QFuture`
objects to control (in own event loop) what queries have been executed.

We need one thread (`DBManager`) for management database access (and if
needed -- solve probably conflicts), other (there can be more than one,
so we can use `QtConcurrent::run` and pointers to `QFuture` objects to
handle states and results) is for executing queries to database.

The task of processing a short queue of queries to database is a
probably long time procedure, so we need to have separate thread for it.
By the way we don’t miss possibility to execute multiple queries in the
same time (if it is possible).

Executing queries from GUI thread is not good idea -- we’ll avoid it.
After DBManager will be applied, we’ll got only one unified entry point
to access database.

As this class will be singleton, it can be reachable from every module.
All queries will be applied through DBManager this way:

  - On module side (from concrete class):
  - prepare query,
  - set query parameters (such as type of needed `DAO`, priority or
    transaction recommendations),
  - prepare callback function (function to apply after successfully
    executing query),
  - call `DBManager`’s function to apply query with own callback
    functions(s) as parameter(s).
  - On `DBManager` side:
  - got new query into own queue of queries,
  - scan current active queries,
  - solve conflicts on how to place this query into queue of queries (to
    avoid blocking and other moments -- must discuss it),
  - create new thread using `QtConcurrent::run` and run query from queue
    (if possible) using respective `DAO`-object in it and control it
    using `QFuture`,
  - check what queries executed and execute respective callbacks. 

Of course, there are lot of moments to discuss on.

*More information will be here soon.*
