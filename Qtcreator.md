# How to setup Qt Creator for developing on Mixxx

## Preparation

First of all, we must install all build Mixxx dependencies (read about
it [Compiling on Linux](compiling_on_linux)).

Keep in mind, that SCons is written to work with any Python version \>=
2.4 and \< 3.0. So, you must have one installed in your system.

Of course, you must have your favorite Qt Creator (can get here:
<http://qt-project.org/downloads>).

Now, easiest way to get Mixxx sources is to download it
(<http://mixxx.org/download>), but also, if you like, you can download
sources from GitHub using git.

`git clone https://github.com/mixxxdj/mixxx.git`

If you downloaded `.tar.gz`-file, you can use the `tar` command from the
shell to unpack it.

`tar -xzf rebol.tar.gz`

The result will be a new directory containing the files. Also, on many
systems, when you download the `.tar.gz` from a web browser, an
un-packer will open, and you can just use that.

### Make Qt Creator and SCons be friends

#### Creating project

In Qt Creator you must:

1.  **File -\> New file or project -\> Import Project -\> Import
    Existing Project.** Click the **"Choose"** button.
2.  Enter a name for the project and navigate to the source directory.
    Where you unpack or get all Mixxx sources and choose `mixxx/`
    directory. 
3.  Verify that the File selection is as you want or fine-tune it. Click
    the **"Continue"** button. 
4.  Optional: choose if you want to add the files to a version control
    system. 
5.  Click the **"Finish"** button.

After this, Qt Creator will add four files to the top-level directory:

    $PROJECT_NAME.files
    $PROJECT_NAME.includes
    $PROJECT_NAME.config
    $PROJECT_NAME.creator

The most important one is `$PROJECT_NAME.files`, which is just a list of
all the files you want to show in the IDE. Here you can exclude unwanted
files. I've done that this way: <http://pastebin.com/EbHpi0s4>.

See
<http://qt-project.org/doc/qtcreator-2.7/creator-project-generic.html>
for details.

Now you have to add the `SConstruct` and `SConscript` files to the IDE.
Either edit by hand the `$PROJECT_NAME.files` or, in the IDE project
browser, right click on the top-level directory and select "Add existing
files", and then select `SConstruct` from the list. Do the same for the
`SConscripts`.

#### Adding a build and a clean target

On the left pane, click **"Projects"**. Verify that the tab name is
actually your project. Click on **"Build Settings"**. The **"build
directory"** field is a bit misleading with SCons. Don't modify the
default, it will use the source top-level directory. Same for the
**"Tool chain"** pull-down menu, leave the default, it is not used by
SCons.

Under **"Build Steps"**, remove the **"Make"** item by hovering on
**"Details"** by clicking the **x** that appears.

Click **"Add Build Step"**, select **"Custom process step"**, tick the
**"Enable custom process step"**, under **"Command"** enter the full
path to SCons (or just `scons` if it is in your `$PATH`). Leave the
other fields as they are. Eventually pass a `-jN` in the **"Commands
arguments"**, where `N` — is number of your real cores.

Under **"Clean Steps"**, do the same thing as for **"Add Build Step"**,
only difference is that you will add `-c` to **"Commands arguments"**.

[[/media/compiling/mixxx_creator_build.png|]]

On the tab **"Run"** of **"Projects"** you can manually specify where
will be your mixxx-build, and what executable to start (“Command”).
Also, I recommend add next text to **"Argument field"**: `--resourcePath
res/` (as described here [Compiling on Linux](compiling_on_linux))

[[/media/compiling/mixxx_creator_run.png|]]

### Additional information

  - Original article was published there --
    <http://neval8.wordpress.com/2013/04/30/using-scons-with-qtcreator>.
  - Official SCons recommendations:
    <http://www.scons.org/wiki/IDEIntegration#Qt_Creator>
