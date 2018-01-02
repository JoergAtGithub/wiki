# Setting-up CI on your own fork

You can configure our CI systems to automatically build your own github
fork of Mixxx. This way, you can push your code into your own fork and
know if it builds correctly before opening a pull request.

The Mixxx project currently use two different CI systems :

  - Travis-CI builds Mixxx under Linux and MacOS (64 bits)
  - Appveyor builds Mixxx under windows (32 and 64 bits)

In the following, we assume you already have a github account and have
forked Mixxx on github.

## Travis-CI

FIXME

## Appveyor

  - go to the appveyor.com website
  - click sign-in on top-right and login using your github account
  - authorize appveyor to connect to your github account
  - create your new CI project by clicking on "New Project"
  - select github as the repository provider and authorized appveyor to
    acces the list of your repositories on github
  - select your fork and click add
  - As we use deployment environment, you have to setup a deployment
    environement with the same name to avoid having each build failing.
    Appveyor doesn't provide a "no-op" provider so we will post a
    webhook to some random website
  - in the top bar, click on "environment"
  - click on "New Environment"
  - select the webhook provider
  - name the environement "downloads.mixxx.org" - the name is important
    here as it must match the name used in appveyor configuration file
    appveyor.yml
  - select a website to poste the webhook to. It should return an HTTP
    200 code. for example, you can use <https://google.com/>
  - Click eon "Add Environment"
  - You're now done. You can manually trigger a build of the master
    branch by clicking on "New Build" nad each push and PR will trigger
    a build.
