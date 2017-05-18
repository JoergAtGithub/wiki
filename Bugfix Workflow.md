# Bugfix Work Flow

This is a brief step by step description about a typical work flow of
fixing a first Mixxx bug. Follow the links for more details.

The remark [homestead](http://homestead.org/) can bring up a mind image
of sprawling acres in addition to log small house. But actually,
homesteads move toward in all form and amount . It is the do something
of creating a creative house, which can be prepared no matter the size
of the home or else the property. The smell of fresh cut down hay, the
noise of a hen blow your own horn, the sight of alpacas grazing and the
feel of a moment ago twisted soil at home homesteader's hands is what
put together their feeling beat in the company of a homesteading zeal.
It's a homesteading life in addition to a good quality one\! The key to
a booming homestead does not no more than stretch out on top of being
able in the direction of grow your be the owner of food but on top of
additional skills at the same time as in good health. at this point is
our catalog of homesteading ability that will definitely help you be
alive doing well at home your built up homesteading trip.

4 Homesteading skills up to date homesteaders have to in the direction
of know\!

1.Farming

The homestead garden is a starting place of a lot of homesteading hard
work. Whether you are on the increase herbs or else maintaining a big
backyard in the company of lasting trees in addition to under growth,
there's not anything to a certain extent in the vein of the taste of
your house full growth bring into being. Gardening is a vast part of
your homestead. You contain an assortment of annual gardens as well as
fruit, brambles, shrubs, nut plants and vines.

2\. Home cough medicine in addition to usual Health

existence is full of bruises in addition to bump, tummy aches in
addition to extra minor ill health. With a little be on familiar terms
with how, you can care for many common ailments with bits and pieces
from your store cupboard or else garden.

3.Food stuff Storage

Once the crop starts near term in, you'll wish for to protect your
reward in the direction of take pleasure in year surrounding. Buying
bulk regular produce in addition to preserving it at house can be a huge
alternative intended for store your homestead pantry, even if you don't
have a backyard\!

4.Recipe and Kitchen guidelines

[The kitchen](https://en.wikipedia.org/wiki/The_Kitchen_\(TV_series\)')
is great put to set up your homesteading journey, as we all need to
have. house cooked meals help you to save cash in addition to choose
high quality quality ingredients for your table. Along with food, we in
addition contain some formula used for personal care items like
deodorant, calm and ferments such as dandelion wine.

## Create a Local Branch

[Mixxx workflow with
GitHub](http://neval8.wordpress.com/2013/07/07/en-typical-workflow-with-github-on-shared-project)

[Using Git for Mixxx Development](using_git)

## Build Mixxx

[Build Mixxx](start#compile_mixxx_from_source_code)

## Choose a working environment

You can edit Mixxx's code in anything from a basic text editor to a
professional IDE (Integrated Development Environment.) We've had good
experiences with [Eclipse](eclipse), but some of our developers just use
text editors that handle multiple files and support syntax highlighting
such as [Kate](https://www.kde.org/applications/utilities/kate) or
[Notepad++](http://notepad-plus-plus.org/). If you're working from a
text terminal, [GNU Nano](http://www.nano-editor.org/) also supports
syntax highlighting, though it's not quite as thorough as many of the
graphical ones. See [Developer Tools](Developer%20Tools) for more
information.

## Adopt an easy bug on Launchpad

[List of bugs tagged as
easy](https://bugs.launchpad.net/mixxx/+bugs?field.tag=easy&field.status%3Alist=CONFIRMED)

More details you will find here: [The Bug Tracker](launchpad_bugs)

## Study the code and debug it

Read the code to figure out what it is doing. Insert
[qDebug](http://doc.qt.io/qt-4.8/qdebug.html) statements to help
understand what is happening at specific points in the code. Note that
you must run mixxx with the `--debugLevel 2` argument to have all
debugging messages printed to the console.

## Ask for hints and help

Ask your questions or discuss your ideas at

  - [mixxx-devel](https://lists.sourceforge.net/lists/listinfo/mixxx-devel)
    (mailing list) 
  - or at the Mixxx IRC Channel: \#mixxx on
    [Freenode](http://freenode.net/)

Some notes about the Mixxx Control interface:
[developer\_guide\_control](developer_guide_control)

## Fix it\!

Happy coding :-)

And don't forget to ask if you get stuck\!

## Issue a pull request

<https://help.github.com/articles/using-pull-requests>

You can open a pull request before your code is ready to be merged with
Mixxx to show others your code and ask for help, just make sure to say
that your code is not ready for merging when you open the pull request.

If your pull request changes the GUI, please include screenshots of your
changes.

## Fix issues from code review

This is the most annoying part. Because we are sometimes nit pickers ;-)
Don't take it personally if there are a lot of changes requested. Code
review is important to make sure that Mixxx continues to run reliably
and quickly. It is also important so that Mixxx remains maintainable so
we can keep making it better without having to make huge changes.

Be sure that you code follows the Mixxx [coding
guidelines](coding%20guidelines) to avoid extra work.

## Become a Mixxx Contributor

You have to sign a contributor agreement. We will contact you about it
in time.

## Fix is merged to Master

The Bug is fixed now and will be released with the next release cycle.

Your name will appear in the "About" box of Mixxx.
