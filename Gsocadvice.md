# Google Summer of Code Advice

This page has some general advice for people thinking about applying for
Summer of Code with Mixxx. If you wish to apply for the program then you
will need to visit [the official Google Summer of Code
website](http://socghop.appspot.com/).

## What Project Should I Work On?

In general, your project proposal can be inspired by any of the
following:

  - A project from our [GSoC 2014 Ideas Page](gsoc2014ideas)
  - A project you come up with\! Make sure to contact us **before**
    submitting to get feedback if this is your plan.
  - You can use our [Wishlist
    Bugs](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&field.importance%3Alist=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.tag=&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&search=Search)
    page for inspiration for your project.
  - Projects from our past GSoC ideas pages: 
  - [GSoC 2012](gsoc2012ideas) 
  - [GSoC 2011](gsoc2011ideas) 
  - [GSoC 2010](gsoc2010ideas) 

## How Do I Contact Mixxx?

You are more than welcome to contact us before submitting your
application, we will be happy to advise on most aspects of the process.
Getting in touch first is especially recommended if you are planning to
apply to work on an original idea, rather than one of our suggestions
from the [ideas page](gsoc2013ideas).

So if you'd like to discuss your application, your ideas or just
introduce yourself, then feel free to get in touch in one of the
following ways:

1.  Send an email to our public developers' mailing list:
    [mixxx-devel](http://lists.sourceforge.net/lists/listinfo/mixxx-devel)
2.  Contact our GSoC administrators directly via email: 
    1.  RJ Ryan (rryan -A-T- mixxx.org)
    2.  Albert Santoni (alberts -A-T- mixxx.org)
3.  Hop on our IRC channel (\#mixxx on Freenode) and see if our mentors
    are around (bkgood, asantoni, rryan). 
    1.  We encourage idling in our IRC channel to get acquainted with
        the wider Mixxx community as well.

## What Would Working On Mixxx Be Like?

The Mixxx development environment is cooperative and relatively
informal. Our community is small but unusually diverse. Working on Mixxx
you would have an opportunity to interact with a unique mixture of
programmers, artists and DJs. Mixxx as a piece of software also offers
some unique challenges, we are both cross-platform and (soft) real-time
and support a huge range of MIDI and audio hardware devices. Students
with Mixxx will have an opportunity to learn advanced skills like
low-latency programming and cross-platform application deployment which
will look great on your resumé.

We also very much value the contributions students make. Because Mixxx
is relatively small, students' work often makes a large impact. During
and after your Summer of Code project you will have the opportunity to
put your work in the hands of real DJs and hear how they've used it.
Past students have had a lot of fun working on Mixxx and learned a lot
at the same time. If you want challenging problems, freedom to develop
your ideas, interesting people and an all-round brilliant Summer, then
apply to work on Mixxx.

## Am I Experienced Enough?

This is a common question asked by prospective students, the answer is
generally: "Yes". The Mixxx Summer of Code team value intelligence and
enthusiasm above specific knowledge of the libraries or algorithms we
use. We have found in the past that an interested and motivated student
who is willing to learn is more valuable than anything else.

We also value general software design and development experience above
specific knowledge of a library or API. For example, if you've never
used Qt before but have done lots of Java and Gtk+ UI development then
you should make sure you let us know about it in your application.

Of course if you do have direct experience with the tools we use, you
should definitely tell us about that too. The main external tools we
rely on are `Qt`, `scons`, `portaudio` and `git`.

## Our expectations from students

#### Communication

  - write us at least once a week a short report
  - commit early commit often and push to github so that we can see it
  - actively work on your project plan and communicate with us during
    the community bonding period
  - Communicate every working day with your mentor. Just say "hello" If
    you like. It can be via email,IRC or github comments.
  - If there are good reasons, for not communicating please announce
    them early.
  - If you don't communicate with us regularly we will fail you.

#### Midterm and Final evaluations

  - set a realistic goal for mid-term. If you fail to meet your own goal
    we are more likely to fail you in the evaluations.
  - have some code merged into master at the end of the summer to pass
    the final evaluation.
  - The later is a hard requirement so make sure that your time plan
    includes it.

## How Do I Write A Great Application?

Firstly, think about your choice of project carefully, you're going to
be doing it for a couple of months, so it's important that you choose
something you're going to enjoy. Once you've made your mind up:

1.  Make sure you've thought about the project and understand what it
    entails
2.  Don't be afraid to come up with original solutions to the problem
3.  Don't be afraid to give us lots of detail about how you would
    approach the project
    1.  Things like UI mockups are very much encouraged where
        appropriate
4.  Consider how much time you need for each part of the project

Overall, your application should make us believe that you are capable of
completing the project and delivering the functionality to our users. If
you aren't sure about anything, get in touch with us, we're happy to
advise you.

#### Splitting up your project into smaller pieces

We require our students to merge some of their code into our master
branch before the end of the summer. The best way to achieve this is to
divide your project into small self contained subprojects and plan to
merge at least one of them around midterm.

A good example for this is 'Improve our track managment':

``` 
 - handle property changes for a selection of tracks
 - add a custom editor for cue points
 - add an editor for the BPM-grid
 - build an editor to comment time slices of a track
```

Another approach is to analyze what the absolute minimal requirements
are and then adding features on top of that. eg 'implement cover art in
mixxx':

``` 
 - handle reading/storing covers in the database and application
 - Show the cover next to the track name in a deck
 - display the covers in the library view
 - add picture flow
```

During your summer you'll encounter bugs in mixxx or find code that can
be refactored to help you implement your ideas. You can also immediately
fix them in the master branch and help us all out. This has several
advantages. All your pull request will only concentrate on specific
features and are much better to review. And you'll also get direct
feedback from other devs and user during the summer.

Since this is a hard requirement we as mentors will also have an eye on
that and check if your proposal incorporates it and also warn you ahead
of time during the summer if we see that you might not make it.
Communicating with us on a regular basis is vital for that though.

#### Having good time estimates

To get a feeling for the code and get some experience with our code you
can go and tackle some of our easy bugs. Look at the code that you want
to change, check if it follows our coding guidelines. Do some research
on the API's you want to use, plan what classes you will add and how
their public API will look. Write down your algorithms in pseudo code.
The better your research is and the better you plan ahead the easier it
will be to judge how long a given task will take. For your time
estimates you should also consider that you can do less stuff during
exams and try to be a bit conservative. If you have never done anything
like GSoC before you will tend to underestimate the time to complete a
task. I know that giving these estimates is not easy and that also
professionals have problems with it. Having a good plan, knowing its
weak and strong points are can help a lot.

#### Some other (entirely optional) things you might consider doing

1.  Why not introduce yourself on the mailing list? Even just to say
    hello, your name and what you're applying to work on
2.  If you don't have Mixxx already, download it, play around with it
    for a while, let us know what you like or don't like
3.  For lots of bonus points:
    1.  Check out [the source](using_git) and compile it, play around
        with the code a little
        1.  Be sure to write about what you did in your application
        2.  If you can't get it to compile, it's probably our fault not
            yours, don't be embarrased to ask for help
    2.  Check out our
        [Wishlist](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&field.importance%3Alist=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.tag=&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&search=Search)
        bugs and [Easy
        Bugs](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.tag=easy+weekend+&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search)
        lists. 
        1.  Try picking something on the list and tackling it as a
            starter project\!
        2.  [Bugfix Workflow](Bugfix%20Workflow) 
4.  As mentioned in the contact section above, hang around on IRC at
    freenode.net \#mixxx
5.  Sign up for [the forums](http://www.mixxx.org/forums)

We look forward to your application :) - The Mixxx Development Team
