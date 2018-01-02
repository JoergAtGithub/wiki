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

[[/media/appveyor-01.jpg|]]

  - click sign-in on top-right and login using your github account

[[/media/appveyor-02.jpg|]]

  - authorize appveyor to connect to your github account

[[/media/appveyor-03.jpg|]]

  - create your new CI project by clicking on "New Project"

[[/media/appveyor-04.jpg|]]

  - select github as the repository provider and authorized appveyor to
    acces the list of your repositories on github

[[/media/appveyor-05.jpg|]] [[/media/appveyor-06.jpg|]]

  - select your fork and click add

[[/media/appveyor-07.jpg|]]

  - As we use deployment environment, you have to setup a deployment
    environement with the same name to avoid having each build failing.
    Appveyor doesn't provide a "no-op" provider so we will post a
    webhook to some random website
  - in the top bar, click on "environment"

[[/media/appveyor-08.jpg|]]

  - click on "New Environment"

[[/media/appveyor-09.jpg|]]

  - select the webhook provider

[[/media/appveyor-10.jpg|]]

  - name the environement "downloads.mixxx.org" - the name is important
    here as it must match the name used in appveyor configuration file
    appveyor.yml
  - select a website to poste the webhook to. It should return an HTTP
    200 code. for example, you can use <https://google.com/>
  - Click on "Add Environment"

[[/media/appveyor-11.jpg|]]

  - You're now done. You can manually trigger a build of the master
    branch by clicking on "New Build" nad each push and PR will trigger
    a build.
