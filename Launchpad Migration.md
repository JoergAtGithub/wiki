# Problems with Launchpad Bugs

Many people have expressed frustration with [bug tracking on
Launchpad](https://bugs.launchpad.net/mixxx). This is a place to
enumerate the problems so we have an objective list when comparing
alternate solutions.

Note that Launchpad is open-source, so it is possible for us to directly
improve it. (See below.) It also now supports Git repositories.

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

# Possible solutions

## GitHub Issues

Many have suggested using GitHub's issue tracker since it naturally
integrates with its code review system.

Migration tools:
<http://lp2gh.readthedocs.io/en/latest/moving_issues.html>

### Advantages

  - Easy to cross-reference pull requests and issues
  - [Close issues automatically when merging pull
    requests](https://github.com/blog/1506-closing-issues-via-pull-requests)

### Disadvantages

  - Doesn't explicitly support rich states other than just open/closed
  - Using labels for this is just a workaround and might become
    confusing. 
  - Not possible to link related issues
  - Not possible to specify different kinds of relationships
    (parent/child, predecessor/successor, duplicates, etc.)
  - Someone needs to commit to managing migration
  - Closed-source
  - Company is not very responsive to community feature requests and has
    no public issue tracker for their server software
  - Requires nonfree client-side JavaScript

## GitLab

<https://about.gitlab.com/>

### Advantages

Note that for public open source repositories, the [GitLab.com hosted
service](https://about.gitlab.com/gitlab-com/) has all the features of
the paid nonfree Enterprise Edition Premium server software.

  - Company is highly engaged with the community with a public issue
    tracker and accepts code contributions
  - Server software is developing rapidly with new features rolled out
    monthly
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

  - Someone needs to commit to managing migration
  - Has had issues with page load speed and uptime in the past but has
    improved lately and they're continuing to work very hard on this
  - Some features only available in paid Enterprise editions for
    self-hosted server software

## Improve Launchpad

<https://dev.launchpad.net/>

### Advantages

  - No need to migrate data
  - Can run our own instance (if ever GitHub closes or decides to
    charge)
  - Open-source

### Disadvantages

  - Coding our own bug tracker would be an enormous for Mixxx developers

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
