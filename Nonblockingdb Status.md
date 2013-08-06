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

My fork of Mixxx at GitHub: <https://github.com/troyane/mixxx>

-----

# Most interesting for now

1.  Article on Library refactoring prototype --
    <https://docs.google.com/document/d/1K2XpAmN68f5U6iv9SSZcmaDrpVjhp61S7GkQCMmLjm4/pub>
2.  Code review of pause feature in library scanner --
    <https://github.com/mixxxdj/mixxx/pull/55>

# Main goals for final term

1.  **Pausable Library scanner.** We are on this way.
2.  **No writes access to database from the GUI thread.**
3.  **`ThreadDAO`** -- let's do and test on just one query, and then
    generalize to common case -- do queue.
4.  **Clever locking** -- to avoid the race condition with duplicated
    data from database and models/member variables and to discard double
    user database commands. 
5.  Some kind of widget in Mixxx, like status-bar, `QProgressIndicator`
    or a Mouse cursor.
6.  Fix some linked bugs.

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
2.  **Week *(24.06 -- 30.06)***
    1.  Dig into Mixxx and find all usage of db access, analyze it,
        write brief description of different types of DB usage in Mixxx
        and think on what to aware of when designing solution.
    2.  Find all related bugs.
    3.  (some of items was moved forward to next week)
3.  **Week *(01.07 -- 07.07)***
    1.  Dig into Sqlite and define or find some suitable test cases.
    2.  Dig into Mixxx and find all usage of db access, analyze it,
        write brief description of different types of DB usage in Mixxx
        and think on what to aware of when designing solution.
    3.  Prepare UML class (and probably, sequence) dias for nowadays
        Mixxx DB accesss. // For this purposes I use Dia
        (<http://projects.gnome.org/dia/>), ArgoUML
        (<http://argouml-stats.tigris.org/>) or Umrello
        (<http://uml.sourceforge.net/)//>
    4.  Begin writing documentation.
    5.  Writing the specs for a possible solution.
    6.  Prepare UML class (and probably, sequence) dias for new DB
        accesss in Mixxx.
    7.  Create separate repo on GitHub for prototype.
    8.  Start implementing of prototype database access class with
        separate test project.
    9.  (Try to) Fix some bugs.
4.  **Week *(08.07 -- 14.07)***
    1.  Start Open discussion to involve other developers to review
        prototype.
    2.  Implement prototype database access class with separate test
        project.
    3.  (Try to) Fix some bugs.
5.  **Week *(15.07 -- 21.07)***
    1.  Get acquainted with "Google Test" framework. 
    2.  Write tests using "Google Test" framework.
    3.  (Try to) Fix some bugs.
6.  **Week *(22.07 -- 28.07)***
    1.  Add and test all possible ways of database usage present in
        Mixxx handled by DAO.
    2.  (Try to) Fix some bugs.
7.  **Week *(29.07 -- 04.08)***
    1.  Finish prototype that is able to handle asynchronous db access,
        ..., flexible and extendable.

<!-- end list -->

  - **Important date** *29.07* -- Begins midterm deadline
  - **Important date** *20.08* -- Midterm deadline
  - **For midterm** I'll prepare separate prototype project on separate
    repo.

-----

1.  Week *(05.08 -- 11.08)*
    1.  Plan (re-plan) schedule of work for finalterm.
    2.  Discussion possible race conditions.
    3.  Discuss further work on
        <https://github.com/mixxxdj/mixxx/pull/55> (pausable library
        scanner and this branchs place in further library refactoring).
    4.  Work on
        <https://github.com/troyane/mixxx/tree/LibraryConcurencyRefactoring>
        to introduce separate thread for DB access \`ThreadDAO\` class.
    5.  Discuss migration to C++11.
    6.  *Do re-planning for further work (if needed).*
2.  Week *(12.08 -- 18.08)*
    1.  Disscuss better way to do locking of UI -- "Clever locking".
    2.  Implement locking of UI.
    3.  *Do re-planning for further work (if needed).*
3.  Week *(19.08 -- 25.08)*
    1.  Implementing of queue (or not queue but one-shot if it would be
        better) queries inside \`ThreadDAO\`.
    2.  Test implemented solution.
    3.  (Try to) Fix some bugs.
    4.  *Do re-planning for further work (if needed).*
4.  Week *(26.08 -- 01.09)*
    1.  Implementing & testing.
    2.  Fixing bugs using implemented scheme. Here is blueprint
        <https://blueprints.launchpad.net/mixxx/+spec/nonblockingdb>,
        and there are linked bugs, which could be solved using new API.
    3.  *Do re-planning for further work (if needed).*
5.  Week *(02.09 -- 08.09)*
    1.  Write specs and docs on solution.
    2.  Prepare general API for applying queries.
    3.  Fixing bugs using new API.
    4.  *Do re-planning for further work (if needed).*
6.  Week *(09.09 -- 15.09)*
    1.  Iron out remaining bugs.
    2.  Merge my branch with master.
7.  Week *(16.09 -- 22.09)* 

<!-- end list -->

  - **Important date** *16.09* -- Pencils down begins

<!-- end list -->

1.  Week *(23.09 -- 29.09)* : 

<!-- end list -->

  - **Important date** *27.09* -- Finalterm deadline

<!-- end list -->

1.  01.10 : end

# Current status

Currently I'm working on:

1.  SQLite tests (including using WAL, see:
    <http://www.sqlite.org/wal.html>).
2.  Reading and by the way cleaning code of database access.
3.  Preparing prototype of access to database.
4.  Working on implementing "pause" feature in library scanner (See
    `LibraryRefactoring` branch here --
    <https://github.com/mixxxdj/mixxx>).

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
