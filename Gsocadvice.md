# Google Summer of Code Advice

Thank you for your interest in working on Mixxx with Google Summer of
Code\! GSoC can be a fun and rewarding way to put your coding skills to
use by contributing to free software. GSoC students gain valuable
experience not only in programming, but also collaborating with an
international community to make awesome software used by thousands of
people around the world. We welcome you into our community and hope that
you find working on Mixxx as fun as we do\!

Mixxx is relatively small project, so students' work often makes a large
impact. During and after your Summer of Code project you will have the
opportunity to put your work in the hands of real DJs and hear how
they've used it. Past students have had a lot of fun working on Mixxx
and learned a lot at the same time. If you want challenging problems,
freedom to develop your ideas, interesting people and an all-round
brilliant summer, then apply to work on Mixxx.

This page has some general advice for students thinking about applying
for Summer of Code with Mixxx. If you wish to apply for the program then
you will need to visit [the official Google Summer of Code
website](https://summerofcode.withgoogle.com).

## Getting Involved

We consider more than the words in your application when deciding which
students to accept. We look for signs that you will become an active
participant in our community and that you are someone we would want to
work with over several months. Although it is not a requirement, we hope
you continue to stay involved after GSOC ends. The best way to show us
you will become a part of our community is to get involved before
beginning your application. Here are some ways to get started:

  - Play with Mixxx and explore what it can do. Read the [Mixxx
    manual](https://mixxx.org/manual/latest/) to get a better
    understanding of Mixxx's capabilities and what people use it for.
  - Introduce yourself on our [Zulip
    chat](https://mixxx.zulipchat.com/). Start a new topic in the \#gsoc
    stream. Do not hesitate to ask questions, or ask for a helping hand
    to get started. Please make sure you have read **this** page
    carefully before. **If the first question you ask is clearly
    answered on this page, you will likely not be accepted, because it
    strongly suggests that you lack the ability to work independently.**
  - Help users with technical questions about Mixxx on the
    [forum](https://mixxx.org/forums/).
  - [Test pull requests](testing).
  - Look through the [start\#Developer
    Documentation](start#Developer%20Documentation) and make a small
    code contribution to fix a bug or enhance an existing feature.
  - Report bugs on our [bug tracker](https://bugs.launchpad.net/mixxx/).

We expect that you make an effort to answer your own questions like
reading the source or exploring this wiki before asking us. But don't
hesitate to ask if you cannot answer a question on your own. We are
happy to give you guidance and assist you when you get stuck working on
code, but we will not do work for you. **If your questions show us that
you have not explored the code nor even practiced using Mixxx, you will
likely not be accepted.**

## What Project Should I Work On?

GSOC lasts several months, so it is important that you choose a project
that you are personally passionate about that you will be excited to
work on for an extended period. We cannot tell you what want you want to
work on, but we have some suggestions for project ideas. Before thinking
too much about what project you want to work on, we suggest spending
time using Mixxx and [\#Getting Involved](#Getting%20Involved) in the
community. This will help you understand what Mixxx currently does well
and what areas could be improved. In general, your project proposal can
be inspired by any of the following:

  - A project from our [GSoC 2020 Ideas Page](gsoc2020ideas)
  - A project you come up with\! Make sure to contact us on
    [Zulip](https://mixxx.zulipchat.com/) **before** submitting to get
    feedback if this is your plan. Please spending more than a few days
    using Mixxx and participating in the community before suggesting
    your own ideas. This will help you develop an understanding of what
    Mixxx's current weaknesses are that could use improvement.
  - You can use our [Wishlist
    Bugs](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&field.importance%3Alist=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.tag=&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&search=Search)
    page for inspiration for your project.

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

## Am I Experienced Enough?

This is a common question asked by prospective students, the answer is
generally: "Yes". You do need some prior experience with C++, even if it
was only for a small school project, but you do not need experience with
the specific libraries or algorithms Mixxx uses.

We value general software design and development experience above
specific knowledge of a library or API. We have found in the past that
an interested and motivated student who is willing to learn is more
valuable than anything else. For example, if you've never used Qt before
but have done lots of Java and Gtk+ UI development, please let us know
that in your application.

Of course if you do have direct experience with the tools we use, you
should definitely tell us about that too. The main external tools we
rely on are Qt and Git.

## Our expectations from students

  - Be self-motivated and stick to the schedule you write in your
    proposal
  - Try to answer your own questions before asking for help
  - Ask for help when you are not sure about the best way forward
  - Write a weekly report on your progress on the wiki page for your
    project.
  - Commit early, commit often, and push to GitHub so that we can see it
  - Actively work on your project plan and communicate with us during
    the community bonding period
  - Communicate every working day with your mentor. Just say "hello" if
    you like. We primarily use [Zulip](https://mixxx.zulipchat.com/) and
    comments on [GitHub pull
    requests](https://github.com/mixxxdj/mixxx/pulls) to communicate.
  - If there are good reasons for not communicating please announce them
    early. If you know there will be times that you are not able to work
    on your project as much during the summer, please let us know in
    your application.
  - If you don't communicate with us regularly, we will fail you.

#### Midterm and Final evaluations

  - Set a realistic goal for mid-term. If you fail to meet your own goal
    we are more likely to fail you in the evaluations.
  - Have some code merged into the master Git branch at the end of the
    summer to pass the final evaluation. This does not necessarily mean
    that your whole project must be 100% complete by the end of GSOC.
  - The later is a hard requirement so make sure that your time plan
    includes it.

## How Do I Write A Great Application?

Firstly, think about your choice of project carefully. You're going to
be doing it for a couple of months, so it's important that you choose
something you're going to enjoy. Once you've made your mind up:

1.  Make sure you've thought about the project and understand what it
    entails
2.  Don't be afraid to come up with original solutions to the problem
3.  [Set up an IDE](Developer%20Tools#Using%20IDEs) to start exploring
    the area of the code you will be working on and understanding how
    the classes work together. Read the [Developer
    Guide](Developer%20Guide) for an introduction to the organization of
    the Mixxx code. Feel free to ask us on
    [Zulip](https://mixxx.zulipchat.com/) if you need help figuring out
    where to start looking in the code.
4.  Figure out what parts of the code need to be changed and come up
    with a general idea of what those changes will be.
5.  Don't be afraid to give us lots of detail about how you would
    approach the project
6.  UI mockups are very much encouraged where appropriate
7.  Consider how much time you need for each part of the project

Overall, your application should make us believe that you are capable of
completing the project and delivering the functionality to our users. If
you aren't sure about anything, get in touch with us, we're happy to
advise you.

### Application evaluation criteria

Here are some criteria that we consider when reviewing applications. We
suggest that you think about these when writing your application.

  - Has the student interacted with the Mixxx community before
    submitting their application?
  - Does the student understand the purpose of their project? Do they
    understand what impact their project will have on users?
  - Has the student demonstrated that they have the ability to work with
    Mixxx's code? The best way to do this is by submitting pull requests
    and getting them merged. It can also be okay if a student works on a
    bug but is unable to solve it before the application deadline if
    they demonstrate competence working with the Mixxx code. Students
    *must* have submitted a pull request to Mixxx or provide links to
    code they have written before in their application (ideally both).
  - Has the student demonstrated that they can work independently and
    solve problems on their own without asking for help every step of
    the way?
  - Does the student understand the design and technical details of what
    will be required to implement their proposal?
  - Is the proposed timeline realistic considering any other obligations
    the student may have during GSOC?

### Splitting up your project into smaller pieces

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
Mixxx':

``` 
 - handle reading/storing covers in the database and application
 - Show the cover next to the track name in a deck
 - display the covers in the library view
 - add picture flow
```

During your summer you'll encounter bugs in Mixxx or find code that can
be refactored to help you implement your ideas. You can also immediately
fix them in the master branch and help us all out. This has several
advantages. All your pull request will only concentrate on specific
features and are much better to review. And you'll also get direct
feedback from other developers and users during the summer.

### Having good time estimates

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

#### Example

Stéphane Lepin has kindly published his [successful 2017
application](https://docs.google.com/document/d/1rbMR85tzp9VDIoMOSuSbToIwXSpzl3XmjaJh3ABxZGY).

We look forward to your application\! :) - The Mixxx Development Team
