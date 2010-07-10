## Abstract

While working on icons in my dev branch
<https://code.launchpad.net/~jus/mixxx/skins> i found out the
//res/images/ // folder in Mixxx sources needs a clean-up. Lot of
old/unused images with confusing name in there. The information provided
here are as of now only applicably to the dev branch.

If this branch gets merged with trunk i\`ll update the informations
accordingly. Some changes mentioned here might not be pushed to
Launchpad yet--- *[jus](jus-AT-justmail.de) 2010/07/10 06:21*

## Tips for Designers

Here are some tips that you might find useful as you develop icons or
other drawable assets:

  - [Android Icon Design
    Guidelines](http://developer.android.com/guide/practices/ui_guidelines/icon_design.html#design_tips)
  - [Choosing the Right Size and Format for
    Icons](hhttp://www.visualpharm.com/articles/icon_sizes.html)

## Common naming conventions for icon assets

Try to name files so that related assets will group together inside a
directory when they are sorted alphabetically. In particular, it helps
to use a common prefix for each icon type. For example:

| Asset Types       | Prefix            | Example                                     |  |
| ----------------- | ----------------- | ------------------------------------------- |  |
| Icons             | ic\_              | ic\_mixxx.png                               |  |
| Preferences Icons | ic\_preferences\_ | ic\_preferences\_broadcast.png              |  |
| Library Icons     | ic\_library\_     | ic\_library\_playlists.png                  |  |
| Icon Templates    | ic\_template\_    | ic\_template\_library\_and\_preferences.svg |  |

## Working space organisation

### mixxx/res/images/

**ic\_mixxx.ico**

  - Windows icon container. A full set should contain 16×16, 32×32,
    48×48 and 256×256.
  - [Microsoft Vista+ Icons
    Guide](http://msdn.microsoft.com/en-us/library/aa511280.aspx) 

**ic\_mixxx.png**

  - Application icon for Linux .desktop file . Primary size for
    application icons 48x48
  - [Desktop Entry
    Specification](http://standards.freedesktop.org/desktop-entry-spec/latest/)
  - [GNOME icon
    specification](http://library.gnome.org/devel/hig-book/stable/icons-types.html.en)
  - [QT Desktop File
    Standard](http://doc.qt.nokia.com/qtextended4.4/desktopfiles.html)

**ic\_mixxx\_16x16.png**

  - Window icon displayed in the corner of an application's top-level
    windows. Primary size for Window icons 16x16
  - [Setting the application icon in
    QT 4](http://doc.trolltech.com/4.6/appicon.html)

**mixxx\_install\_logo.bmp**

  - Bitmap image to display on the header of installers pages for
    Windows NSIS installer. Recommended size 150x57.
  - [NSIS Modern UI
    Documentation](http://nsis.sourceforge.net/Docs/Modern%20UI%202/Readme.html)

#### library

Sub-folder that holds all 48x48 \*.png icons for display in Mixxx
library widget

#### preferences

Sub-folder that holds all 48x48 \*.png icons for display displayed in
Mixxx preferences dialog

#### templates

Sub-folder that holds various templates for image files

  - ic\_template\_mixxx.svg = multilayered Inkscape template for Mixxx
    application icon, holds special layer for 16x16 icon too
  - ic\_template\_library\_and\_preferences.svg = multilayered Inkscape
    template for all icons in library widget & preferences dialog.
  - logo\_mixxx.png = Mixxx logo ( too bad it is not in svg format)

### mixxx/res/osx

**application.icns**

  - Apple icon container for display in in Mixxx\` \*.app bundles for OS
    X.
  - A full set should contain 16×16, 32×32, 128×128,256×256 and 512×512
  - [Apple Human Interface
    Guidelines](http://developer.apple.com/documentation/UserExperience/Conceptual/AppleHIGuidelines/XHIGIcons/XHIGIcons.html#//apple_ref/doc/uid/20000967-TPXREF115)
    

**VolumeIcon.icns**

  - Apple icon container for display in Mixxx\` \*.dmg images for OS X. 
  - A full set should contain 16×16, 32×32, 128×128 ( 128 is maximum
    size OS X desktop grid, enough for dmg\`s)

### mixxx/res/unused/images

holds all the unused files lurking for some reasons in
//mixxx/res/images/ // until
