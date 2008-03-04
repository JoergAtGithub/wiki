# rhythmbox

One caveat:
[rhythmbox](http://whttp://www.gnome.org/projects/rhythmbox/ww.gnome.org/projects/rhythmbox)
is hobbled by the legal restrictions imposed upon the MP3 format and
decoder software; it won't play mp3's as installed. It's easy enough to
fix however, gstreamer plugins from the "ugly" repositories add mp3
support to rhythmbox:

\<code\> $ sudo apt-get install gstreamer0.10-plugins-ugly\</code\>

This will drag in enough code to make it work.

# Rhythmbox annoyance(s)

\<rant\>Sheesh, all these music programs insist on doing me 'favors'
that I didn't ask for. Like, it has it's own idea of a "music
collection", which is "every playable file I ever come across, ever",
when the real answer is for a person to "put your music in a folder, and
point to it". \</rant\>

rhythmbox accumulates every playable file ever seen into it's
"collection". You'd think that the Edit -\> Preferences -\> Music tab
path would be where it looked for music, but you would be wrong.

To enforce that rhythmbox actually *do so*, occasionally do this:

Quit rhythmbox,

    $ rm .gnome2/rhythmbox/rhythmdb.xml

Then restart.
