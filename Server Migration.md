# Server Migration

Mixxx is currently in a bad situation because too much of it's critical
infrastructure in relying on private servers and single individuals
(i.e. a lot of important key infrastructure is maintained by few
persons, which leads to a [bad "bus
factor"](https://en.wikipedia.org/wiki/Bus_factor)).

Also, maintaing custom servers is time-intensive and boring. We need to
make sure everything is updated regularily or risk being hacked.

## Website

Currently built on Jenkins. If Jenkins goes down, RJ is the only one who
can fix this. If we want to change the build process, we can't without
RJ.

Also, we can only preview a single website PR via staging.mixxx.org (the
most recently built one).

### Proposal

We switch over build & deploy via Netlify. That way we don't need to
take care of deployment and hosting ourselves. The build process can be
edited via file in the website git repository.

We can preview multiple different PRs via the Netlify interface.

**Preview:** <https://holzhaus-mixxx.netlify.app/>

### Migration

1.  Merge PR: <https://github.com/mixxxdj/website/pull/98>
2.  Enable Netlify for mixxxdj/website
3.  Switch mixxx.org domain over to Netlify

## Manual

Currently built on Jenkins. If Jenkins goes down, RJ is the only one who
can fix this. If we want to change the build process, we can't without
RJ.

Also, we can only preview a single manual PR via staging.mixxx.org (the
most recently built one).

Currently, the manual is hosted in the `/manual` subdirectory.

### Proposal

Building the manual in all versions and languages (including PDFs) takes
too much time (Netlify only allows 15 minutes of build time). Instead,
we can build on Travis CI and deploy to Netlify.

Since we can't deploy to a subdirectory, we need to create a new
subdomain (e.g. `docs.mixxx.org` or `manual.mixxx.org`) and use that for
the manual. Using Netlify's redirect system, we can catch all requests
for `/manual` on the website an redirect them to the corresponding page
on `docs.mixxx.org`.

**Preview:** <https://holzhaus-mixxx-manual.netlify.app/>

### Migration

1.  Merge PR: <https://github.com/mixxxdj/manual/pull/113>
2.  Enable Travis CI for mixxxdj/manual repository
3.  Enable Netlify for mixxxdj/manual repository
4.  Add custom domain for the manual

## Forum

The forum is currently a self-hosted phpBB3 instance at `/forums` and
has the charm of the early 2000s. Again, only RJ is able to fix if
issues arise. There are problems with E-Mails not being sent.

### Proposal

We can switch to a hosted Discourse instance and host it at
`forums.mixxx.org`.

### Migration

1.  Apply for a hosted Discourse forum (already done by Be)
2.  Point forums.mixx.org subdomain to hosted Discourse instance
3.  Migrate existing content using an SQL dump from our current phpBB
    install

## Wiki

The Wiki is currently hosted on our own Server. Again, issues can only
be fixed by RJ. We have long-standing issues with activation emails not
being sent, which has blocked some controller PRs for half a year
already.

Also, the DocuWiki syntax is cumbersome and not as straightforward as
markdown.

### Proposal

Move to GitHub Wiki. Then it's closer to the source code and people will
be more likely to take a look at that. If you already have a GitHub
account, no additional account is needed. We don't have to worry about
activation emails anymore.

This will move the Wiki from mixxx.org/wiki to
<https://github.com/mixxxdj/mixxx/wiki>. We can add a HTTP redirect.

### Migration

1.  Enable GitHub Wiki on mixxxdj/mixxx repository
2.  Migrate existing content from DocuWiki to GH Wiki
    (<https://github.com/hoxu/dokuwiki2git>) (We need RJ to give us
    access to server data)
3.  Add redirect from `/wiki` to
    `https://github.com/mixxxdj/mixxx/wiki`.

## Build Server

Right now Mixxx is built on Jenkins and on Travis CI/Appveyor. The
Jenkins build server can only be modified by RJ, and if he doesn't have
time to fix issues this will delay releases (as we're already seeing
this with the 2.2.4 release).

Also, Jenkins and Travis/Appveyor might diverge, so that CI builds pass
but Jenkins does not.

### Proposal

Building Mixxx already works on Travis/Appveyor. Instead of using
Jenkins for the release build, we should use these CI builds for
releases, too. The only thing missing is deploying build artifacts to
our download server.

Compiling the build environment could be done locally or stay on
Jenkins.

### Migration

1.  Get SSH access to the download server
2.  Modify Travis CI config to deploy build artifacts

## Download Server

Currently hosted by Garth, can stay as-is but we needs credentials to
deploy files from CI.

**URL:** <https://downloads.mixxx.org>