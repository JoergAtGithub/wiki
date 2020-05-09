# Problems with Launchpad Bugs

Many people have expressed frustration with [bug tracking on
Launchpad](https://bugs.launchpad.net/mixxx). This is a place to
enumerate the problems so we have an objective list when comparing
alternate solutions.

Note that Launchpad is open-source, so it is possible for us to directly
improve it. (See below.) It also now supports Git repositories and has a
[Web services API](https://help.launchpad.net/API/).

([Discussion on the
forum](https://mixxx.org/forums/viewtopic.php?f=1&t=9425).)

  - ~~Login process is complex: it is a multi step process and the
    platform keeps asking about showing some username~~ The Ubuntu One
    registration/login only asks for your name, E-mail address and a
    password.
  - No formatting
  - Can't edit comments
  - They can be hidden on bugs though.
  - E-mail notifications are slow
  - There is an intentional 5-minute delay so that modifications done
    close together are sent in one message. Beyond that, running our own
    instance could fix this.
  - "Wishlist" designation is mutually exclusive with a priority
    designation, making it impossible to prioritize feature requests
  - Can't @mention people
  - Posting code and screenshots requires attaching a separate file that
    isn't displayed inline in the conversation.
  - Can't make templates for bug reports (e.g. to have people attach
    `mixxx.log` in the initial report)
  - No integration with the code review system (side effect of no longer
    hosting code in LP)
  - Yet another account needed. (Now six total: forum, Freenode, wiki,
    Launchpad, GitHub, mailing list)
  - [OpenID Connect](http://openid.net/connect/faq/) (which uses OAuth)
    would be a good solution to this in general. See [bug
    \#1732715](https://bugs.launchpad.net/mixxx/+bug/1732715).
  - Run by Canonical, which [does not have the greatest track
    record](https://en.wikipedia.org/wiki/Ubuntu_\(operating_system\)#Amazon_controversy)
  - Development of Launchpad has ~~stagnated~~ slowed in recent years.
    <https://github.com/live-clones/launchpad/graphs/contributors>
  - LP had its staffing heavily cut a few years back, but there are
    still a couple paid full-time developers working on it -- and
    several major features that have been developed since that cut.
  - launchpad, sourceforge, savannah once played and important role in
    OSS, but are now rather niche. New users and developers are less
    likely to be familiar with it, and thus less likely to interact with
    the platform.
  - No integration with the source code on GitHub. Automatic PR/issue
    interactions not possible.

# Possible solutions

[List of Application Lifecycle Management
suites](https://en.wikipedia.org/wiki/Application_lifecycle_management#ALM_software_suites)

[Comparison chart of different project management software packages on
Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_project_management_software)

## GitHub Issues

Many have suggested using GitHub's issue tracker since it naturally
integrates with its code review system.

Migration tools:
<http://lp2gh.readthedocs.io/en/latest/moving_issues.html>

### Advantages

  - Easy to cross-reference pull requests and issues
  - Rich formatting
  - [Close issues automatically when merging pull
    requests](https://github.com/blog/1506-closing-issues-via-pull-requests)
  - Everyone uses it.

### Disadvantages

  - Doesn't explicitly support rich states other than just open/closed
  - Using labels for this is just a workaround and might become
    confusing. 
  - Not possible to link related issues
  - Not possible to specify different kinds of relationships
    (parent/child, predecessor/successor, duplicates, etc.)
  - Someone needs to commit to managing migration
  - Closed-source
  - Company is [not very responsive to community feature
    requests](https://github.com/dear-github/dear-github) and has no
    public issue tracker for their server software
  - Requires nonfree client-side JavaScript

## GitLab

<https://about.gitlab.com/>
<https://blueprints.launchpad.net/mixxx/+spec/gitlab-migration>

### Advantages

Note that for public open source repositories, the [GitLab.com hosted
service](https://about.gitlab.com/gitlab-com/) has all the features of
the paid proprietary Enterprise Edition Premium server software.

  - Company is highly engaged with the community with a public issue
    tracker and accepts code contributions
  - Server software is developing rapidly with new features rolled out
    monthly
  - Modern look-and-feel
  - [Issue Board](https://about.gitlab.com/features/issueboard/) with
    drag-and-drop workflow for organizing issues. Can [span across
    multiple
    repositories](https://docs.gitlab.com/ee/user/project/issue_board.html#group-issue-boards)
    (code, manual, website)
  - [Automatic issue
    closing](https://docs.gitlab.com/ce/user/project/issues/automatic_issue_closing.html)
    when code is merged (GitHub can do this too)
  - [Due
    dates](https://docs.gitlab.com/ce/user/project/issues/due_dates.html)
    for issues
  - [Related
    issues](https://docs.gitlab.com/ee/user/project/issues/related_issues.html)
  - [Multiple assignees for
    issues](https://docs.gitlab.com/ee/user/project/issues/multiple_assignees_for_issues.html)
  - [Issue
    weighting](https://docs.gitlab.com/ee/workflow/issue_weight.html)
  - [Easily move discussion from code review to a new
    issue](https://docs.gitlab.com/ce/user/discussions/#move-all-unresolved-discussions-in-a-merge-request-to-an-issue)
  - [Threaded discussions](https://docs.gitlab.com/ce/user/discussions/)
    on issues and merge requests with ability to mark different parts of
    the conversation as resolved
  - [Image
    discussions](https://docs.gitlab.com/ee/user/discussions/#image-discussions)
  - [Protected Git
    branches](https://docs.gitlab.com/ee/user/project/protected_branches.html)
  - [Templates](https://docs.gitlab.com/ce/user/project/description_templates.html)
    for issues and merge requests with possibility for different
    templates (such as bug report and feature request)
  - Projects can have multiple repositories (for example, code and
    manual) with interrelated milestones and issues
  - More nuanced [permission
    system](https://docs.gitlab.com/ce/user/permissions.html) than
    GitHub
  - Continuous integration service is integrated
  - [Automatic merge when CI
    completes](https://docs.gitlab.com/ce/user/project/merge_requests/merge_when_pipeline_succeeds.html)
  - Wouldn't have to pay for CI that doesn't time out like Travis and
    AppVeyor free plans
  - [Hosting artifacts from
    CI](https://docs.gitlab.com/ee/user/project/pipelines/job_artifacts.html)
    (built packages, manual PDFs)
  - [Todo list](https://docs.gitlab.com/ce/workflow/todos.html) can
    replace email notifications
  - Migrating code from GitHub would be easy and it wouldn't be hard for
    developers to adapt

### Disadvantages

  - Write access to GitLab wikis is coupled with write access to source
    code, so we still need to run our own wiki.
    <https://gitlab.com/gitlab-org/gitlab-ce/issues/19798>
  - Someone needs to commit to managing migration
  - Has had issues with page load speed and uptime in the past but has
    improved lately and they're continuing to work very hard on this
  - Some features only available in paid Enterprise editions for
    self-hosted server software. <https://about.gitlab.com/products/>

## Improve Launchpad

<https://dev.launchpad.net/>

### Advantages

  - Very good bug tracking and release management features
  - No need to migrate
  - Can run our own instance (if ever GitHub closes or decides to
    charge)
  - Open-source
  - Would (eventually) suit us perfectly

### Disadvantages

  - Maintaining our own bug tracker would be an enormous drain for Mixxx
    developers that would be better spent developing Mixxx

## Apache Allura

<http://allura.apache.org/>

### Advantages

  - Integrated code, wiki and tickets/issues
  - Can run our own instance (if ever GitHub closes or decides to
    charge)
  - Open-source

### Disadvantages

  - Must run our own instance (no pre-hosted environments, though
    possibly from third party)
  - Looks like old SourceForge
  - Indeed, SourceForge (used to?) use(s) it
  - Need to migrate data from three different systems
  - Someone needs to commit to managing migration

## Tuleap

<https://www.tuleap.org/>

### Advantages

  - Complete integration (code hosting & versioning with Git, code
    review, bugs/tickets, docs/files, CI/Jenkins, project management,
    collaboration)
  - Can run our own instance (if ever GitHub closes or decides to
    charge)
  - Open-source

### Disadvantages

  - Must run our own instance to avoid charges
  - Manual test management is only available in the paid version
  - Must also run Gerrit for code review functionality, Mattermost for
    chat
  - Someone needs to commit to managing migration

## JIRA

from <https://www.mixxx.org/forums/viewtopic.php?f=1&t=9425&start=10>

Jira seems to be popular for open source projects and [free Jira hosting
is available for public open source
projects.](https://www.atlassian.com/software/views/open-source-license-request)

It's a far better issue tracker than what GitHub offers. Someone wrote
about porting issues fro Launchpad to Jira:
<https://mariadb.org/scripts-for-migrating-bug-reporting-from-launchpad-to-jira/>

QT uses Jira <https://bugreports.qt.io> as well

### Advantages

  - Launchpad migration without losing Metadata
    <https://github.com/rasmushoj/LP2JIRA>
  - Using the Launchpad workflow, customize it. 
  - Open Source Plan:
    <https://www.atlassian.com/software/views/open-source-license-request>
  - Integrates with GitHub
    <https://www.atlassian.com/blog/jira-software/connecting-jira-6-2-github>
  - REST API
  - Allows anonymous bug filing.
  - Zulip integration
  - Marketplace with 1,000+ plug-and-play add-ons

### Disadvantages

``` 
 * Source Code available for review only
 * Not FOSS
```

## BitBucket

It has a issue tracker similar to Launchpad but not that complicated the
Jira. It combines code hosting, code review and issue tracking in the
same was as GitHub does.

Example
<https://bitbucket.org/tortoisehg/thg/issues?status=new&status=open>

### Advantages

  - Launchpad migration without losing Metadata
    <https://bitbucket.org/jonathanj/lp2bb>
  - Using the Launchpad workflow.
  - Open Source Plan:
    <https://www.atlassian.com/software/views/open-source-license-request>
  - REST API
  - Allows anonymous bug filing.
  - Zulip integration

### Disadvantages

``` 
 * Source Code available for review only
 * Not FOSS
```

# Selected solution: GitHub issues

We have selected GitHub issues, because our source code lives on GitHub
and we want to have the benefit of the integration of source code
repository and bug tracking.

### Workflow

We will not be mirroring Launchpad's states on GitHub. We will be using
a simplified set of tags:

  - beta blocker
  - release blocker
  - needs info
  - feature request
  - good-first-pr

Every new issue should be assigned to a milestone, closed, or tagged as
a feature request.

If it is closed by automatic expiration the bot will add a comment.

For duplicates type "Duplicate of" followed by the issue number and
close the issue. GitHub will automatically catch that.

In addition a "Launchpad" label is added to all imported issues

Status Fix Released / Fix Committed / Status Won't fix / Invalid /
Opinion are not imported from Launchpad.
