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

# Current status

Currently I'm working on:

  - Extended article to collect as much as possible information about
    project and how to solve it.
  - My roadmap for this summer.

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
