## Tips for Designers

Here are some tips that you might find useful as you develop icons or
other drawable assets:

  - [Android Icon Design
    Guidelines](http://developer.android.com/guide/practices/ui_guidelines/icon_design.html#design_tips)
  - [Choosing the Right Size and Format for
    Icons](http://www.visualpharm.com/articles/icon_sizes.html)

## Common naming conventions for icon assets

Try to name files so that related assets will group together inside a
directory when they are sorted alphabetically. In particular, it helps
to use a common prefix for each icon type. For example:

| Asset Types       | Prefix            | Example                                     |
| ----------------- | ----------------- | ------------------------------------------- |
| Icons             | ic\_              | ic\_mixxx.png                               |
| Icon templates    | ic\_template\_    | ic\_template\_library\_and\_preferences.svg |
| Library icons     | ic\_library\_     | ic\_library\_playlists.png                  |
| Preferences icons | ic\_preferences\_ | ic\_preferences\_broadcast.png              |
| Skin templates    | skin\_template    | skin\_template\_outline.svg                 |

## Working space organisation

### mixxx/res/images/

**ic\_mixxx.ico**

  - Windows icon container. A full set should contain 16×16, 32×32,
    48×48 and 256×256.
  - [Microsoft Vista+ Icons
    Guide](http://msdn.microsoft.com/en-us/library/aa511280.aspx) 

**~~ic\_mixxx.png~~** **mixxx-icon.png**

  - Note: Original name *mixxx-icon.png* restored since Linux seems not
    to like underscores for icon file names in *.desktop* files. This
    resulted in missing application icons on Gnome/KDE with
    *mixxx.desktop* .
  - Application icon for Linux .desktop file . Primary size for
    application icons 48x48
  - [Desktop Entry
    Specification](http://standards.freedesktop.org/desktop-entry-spec/latest/)
  - [GNOME icon
    specification](http://library.gnome.org/devel/hig-book/stable/icons-types.html.en)
  - [QT Desktop File
    Standard](http://doc.qt.nokia.com/qtextended4.4/desktopfiles.html)

**ic\_mixxx\_window.png**

  - Window icon displayed in the corner of an application's top-level
    windows. Recommend size for Window icons 48x48
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
    vector template for all icons in library widget, preferences dialog
    & skins library style.
  - ic\_template\_keyboard\_mapping\_sheet.svg = multilayered Inkscape
    vector template for keyboard mapping chart (for printout,
    documentation...)
  - logo\_mixxx.svg = multilayered Inkscape vector template for Mixxx
    logo (holds bw variant too)
  - logo\_mixxx.png = Mixxx logo bitmap
  - skin\_template\_outline.svg = multilayered Inkscape vector template
    for Outline skin. See [Creating Skins](creating_skins).

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
