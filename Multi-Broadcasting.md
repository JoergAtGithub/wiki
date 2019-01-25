# Multi-broadcasting

Google Summer of Code project by Stéphane Lepin

**Current State** (as of 2019-01-25): Multi-broadcasting released in
2.1, Opus encoding merged (likely released in the upcoming 2.3),
finishing touches on the FDK-AAC encoder

### Project description

This project adds multi-broadcasting to Mixxx as well as support for
Opus and AAC/HE-AAC encoding (which has been requested by users in the
past). Multi-broadcasting is the ability to do live audio broadcasting
to several streaming servers, each broadcasting connection having its
own set of stream and encoding settings. One example use case of this
would be a DJ willing to provide several levels of bitrates and audio
formats to its listeners. Opus and AAC encoders are implemented as
recording and live streaming encoders, and the AAC encoder uses dynamic
loading to avoid infringing both Mixx's FOSS license and AAC's
licensing/patent holders rights

### Relevant source code

  - **Multi-broadcasting: [Mixx PR \#1300 on
    GitHub](https://github.com/mixxxdj/mixxx/pull/1300)**
  - **Opus encoder: [Mixxx PR \#1386 on
    GitHub](https://github.com/mixxxdj/mixxx/pull/1386)**
  - **AAC/HE-AAC encoder using fdk-aac: [Mixxx PR \#1387 on
    GitHub](https://github.com/mixxxdj/mixxx/pull/1387)**
  - Live Broadcasting implemented with [a version of
    libshout](https://launchpad.net/~palakis/+archive/ubuntu/libshout-aac)
    modified for AAC streaming
  - Finds a dynamically-loadable libfdk-aac automatically. Windows
    version can even find and use B.U.T.T's ("Broadcast Using This Tool"
    by Daniel Nöthen) version of the library.
  - Supports AAC-LC (a.k.a traditional AAC), HE-AAC and HE-AACv2
  - Left to do:

<!-- end list -->

``` 
    * Add options for VBR recording
    * Add track metadata
```

### GSoC Phase 1: Broadcasting profiles subsystem

Broadcasting profiles allow management of several sets of server
settings/credentials and encoder settings. They use XML documents as
their storage backend and deprecate the existing key/value pairs stored
in Mixxx's config file which is unfit for storing several sets of
settings profiles. Profiles serve as the settings backend for the Live
Broadcasting Connections implemented in Phase 2, and have the same
standard Icecast/Shoutcast and encoder settings as the existing Live
Broadcasting settings schema.

#### Technical details

  - Profiles are saved as \*.bcp.xml files under a "broadcast\_profiles"
    subdirectory in the settings folder. This file nature is hidden from
    the user, and the profile list in the preferences UI is built by
    listing files in that folder.
  - Added a new BroadcastProfile class:
  - Moved all settings properties from BroadcastSettings to
    BroadcastProfile
  - The BroadcastProfile class takes care of its
    serialization/deserialization from/to XML, using Qt's built-in XML
    features

<!-- end list -->

``` 
    * Has a save() method to save the profile
    * A static method takes care of loading a profile from a .bcp.xml file on disk and building an instance of BroadcastProfile from the XML document's values.
* The profile filename (without the .bcp.xml extension) serves as its name (no need to store it inside the XML document)
* Refactored the BroadcastSettings class:
* Removed all settings properties, which belong to BroadcastProfile
* Keeps a QMap of broadcast profiles (for fast name-based lookup)
* When creating the class, the internal list of broadcast profiles is filled by listing the contents of the "broadcast_profiles" settings subdirectory
* Several data change signals are provided to allow other parts of Mixxx to stay in sync with the profile list (namely: the Live Broadcasting engine and the Live Broadcasting Preferences panel)
```

##### UML diagrams

*Note: these are a bit outdated because a lot happened after this part.*

|                                              |                                             |
| -------------------------------------------- | ------------------------------------------- |
| [[/media/wiki/gsoc_palakis_phase1_umlbefore.png|]] | [[/media/wiki/gsoc_palakis_phase1_umlafter.png|]] |
| *Class structure before modifications*       | *Class structure after modifications*       |

-----

### GSoC Phase 2: Multiple broadcasting outputs

Built on top of the profiles subsystem implement of Phase 1, these
additions provide the actual multi-broadcasting functionalities which
will allow users to do Live Broadcasting to several Icecast/Shoutcast
servers. Management of the streaming connections is done in the Live
Broadcasting Preferences panel. It shows the list of configured
broadcasting outputs, and selecting a connection in the list shows its
profile settings in an editable form below the connections list. While
Live Broadcasting is active, each individual connection can be enabled,
disabled and re-enabled again.

[[/media/multi-broadcasting.png|]] *UI mockup of the original design*

#### Technical details

  - The streaming code originally in EngineBroadcast has been put into a
    new class named ShoutConnection, and EngineBroadcast has been
    deleted
  - ShoutConnection features:

<!-- end list -->

``` 
    * Linked with a Broadcasting Profile (instance of BroadcastProfile) passed as constructor parameter
    * Has its own FIFO buffer filled by the engine
    * Has its own thread (base on EngineBroadcast's) to process frames made available in the FIFO buffer
 * SoundDeviceNetwork (audio engine part responsible for Live Broadcasting) now handles several outputs
 * Management of ShoutConnection instances is done by a refactored BroadcastManager. 
* Has an internal list of ShoutConnection instances, kept in sync with BroadcastSettings' profiles using signals and slots
* Manages output workers in EngineNetworkStream (which has been reworked to have several output workers and a seperate input worker)
* The Live Broadcasting settings UI has been updated (see description above)
```

-----

### GSoC Final period

#### Live Broadcasting: UI polishing

  - Changes in LB preferences UI:
  - Simpler and complete "Remove connection" workflow
  - Show state of each connection in the profile list
  - Error reporting: show an error message when one or more active
    connections failed to connect

#### Broadcasting profiles: secure password storage

In XML broadcasting profiles, two fields are considered sensitive:
"Login" (username) and "Password" By default, these sensitive fields are
stored in plaintext within . These can be optionally encrypted
(enabled/disabled by a user setting) to avoid privacy and/or security
issues. One way of securely storing credentials is to use the OS'
keychain using the [3rd-party QtKeychain
library](https://github.com/frankosterfeld/qtkeychain), which is
compatible with Windows, Linux and OS X. With secure password storage
enabled, the broadcasting profile subsystem puts and gets sensitive
information into and from the encrypted OS' keychain instead of the
plaintext profile document. Broadcasting profiles are currently not
meant for import/export and sharing, so storing values outside of the
XML document is fine. Users doing manual transfers of profiles from one
system to another do so at their own responsibility and will see empty
values for the sensitive fields on the target computer.

Entries stored through QtKeychain have three attributes

  - Service: application name
  - Key: generally used as the account's name
  - Data: generally used as the account's password

The schema for entries meant for broadcasting profiles look like this:

  - Service: broadcasting profile name, prefixed by "Mixxx - "
  - Key: server username (called Login in profiles)
  - Data: server password

#### AAC streaming support

  - Confirmed on the wishlist:
    <https://bugs.launchpad.net/mixxx/+bug/726991>
  - Uses libfdk-aac via dynamic loading
  - Both AAC (LC) and AAC+ (HE-AAC and HE-AAC v2) are supported, among
    other AAC object types
  - Windows: extract libfdk-aac-1.dll from a BUTT installation, or find
    and use from BUTT installation
  - OS X: install fdk-aac from Homebrew (maybe too technical?)
  - Linux: install libfdkaac package
  - Libshout support: needs a custom version, because upstream doesn't
    support AAC streams (unsupported MIME)
  - Uses a FIFO buffer internally to always feed the encoder with a
    defined number of samples

#### Opus streaming support

  - Confirmed on the wishlist:
    <https://bugs.launchpad.net/mixxx/+bug/1338413>
  - libopus is quite easy to use
  - Opus encoded data is muxed in an Ogg stream
  - Requires header frames specific to Opus streams: OpusHead and
    OpusTags
  - These headers are standard. No library exist to generate these,
    however their structure is quite simple and similar to Vorbis'
    headers and comment packets.
  - Same as fdk-aac encoder: uses a FIFO buffer internally to always
    feed the encoder with a defined number of samples
  - Contrary to fdk-aac, this is clearly stated in the encoder's
    documentation

-----

### Weekly schedule

#### Phase 2: Multi-broadcasting

##### June 26 - June 30

  - School project

##### July 3 - July 7

  - Libshout streaming logic separate from EngineBroadcast to new class
    ShoutOutput
  - Add QList\<ShoutOutput\> instance list to EngineBroadcast

##### July 10 - July 14

  - Keep BroadcastSettings' profile list in sync with EngineBroadcast's
    instance list
  - Only on "Apply" button click on Live Broadcasting preferences
  - Active connections shouldn't be restarted
  - Begin work on settings UI refactor
  - BroadcastSettings: add "rename profile" method

##### July 17 - July 21

  - Continue work on settings UI refactor

##### July 24 - July 28

  - Bug hunting in the Live Broadcasting engine
  - Write PoC for secure credential storage

#### Phase 3: Final period

##### July 31 - August 4

  - Implement secure password storage for Broadcasting profiles
  - Live Broadcasting: UI polishing

##### August 7 - August 11

  - Live Broadcasting preferences: actually apply settings to profiles
    only when clicking "Apply" or "OK"
  - Work on preferences UI

##### August 14 - August 18

  - Bug fixing in multi-broadcasting
  - Add support for AAC/AAC+ streaming with fdkaac
  - Add support for Opus streaming 

##### August 21 - August 25

  - Fix remaining UI bugs
  - Rework parts of the wiki page

-----

### Weekly reports

#### Week 1: May 30th - June 2th

I wrote the implementation for the BroadcastProfile class: it currently
has its XML load/save code that needs to be tested and the get/set
behaviour of settings is a bit different compared to the settings
management in BroadcastSettings: settings get/set methods in
BroadcastSettings (that will be removed) "directly talk" with the
mixxx.cfg file, while BroadcastProfile stores values temporarily in
private members until save() is called to write the values to the
profile's XML file. Also, methods beginning with "getDefault" don't
exist in BroadcastProfile because these are set on instanciation of the
class.

I got a bit late because of dev setup issues on my Windows system: I
tried to work on Mixxx with Eclipse on Windows by using the build.bat
provided in the Windows Dev Setup guide from the wiki. Building works,
cleaning too (with a small addition to the Batch script) but Eclipse's
"code checker" throws a lot of errors about undefined symbols (for the
record: include paths for Qt and Mixxx's source code where added in the
project's settings, along with appropriate search paths). In the end, I
switched to Qt Creator, and it suits me for now.

For the next week of coding, I expect to have results on the XML
profiles load/save mechanisms and UI by Friday.

#### Week 2: June 5 - June 9

I refactored BroadcastSettings as a manager of BroadcastProfile
instances. It's integrated in the current UI, which saves settings to a
file named "Default Profile.bcp.xml" in
$SETTINGS\_DIR/broadcast\_profiles.

Actual implementation of BroadcastProfile differs a bit from the
original design: file management (create/rename/delete/open) was
initially planned to be done in a profile instance itself, but was
eventually moved to BroadcastSettings to have this responsibility
handled in a single class instead of several parts across several
classes. However, the XML save/load code is still the responsibility of
BroadcastProfile.

I got late with UI, so next week's plan is:

  - First, make sure BroadcastSettings is instancianted only once
  - Replace instances in DlgPrefBroadcast and EngineBroadcast with a
    pointer to a single instance
  - Work on UI from Monday to Wednesday
  - Testing during the remaining days.

#### Week 3: June 12 - June 16

I had progress on the UI but there was still a lot of work left to do to
make sure everything is functioning properly. Instead of implementing
the new Broadcasting Profiles UI, Daniel and I agreed on a slimmed-down
schedule for the remaining of phase 1. The plan is to focus on the XML
profile subsystem to have a good foundation for multiple broadcasting
outputs (a.k.a multi-broadcasting, each profile being a connection) for
phase 2, with proper instance reference passing and unit tests. See
[this Pull Request](https://github.com/mixxxdj/mixxx/pull/1283).

The UI will be left untouched, and the work already done is kept
separately for later re-use.

#### Week 4: June 19 - June 23

Work went as planned for this week: unit tests for BroadcastProfile were
written, pointers to BroadcastProfile instances are now QSharedPointers,
turned BroadcastSettings into a Qt object to be able to implement basic
read-only model support and profile name synchronization with signals &
slots between BroadcastSettings' hashmap and the instances' name
attribute. getCurrentProfile and setCurrentProfile were deleted because
no longer useful, and were instead replaced with a more future-proof
call to profileAt(int) that returns a profile based on its list index.
Seems like work on Phase 1 is over. Further additions will come during
phase 2, where those will be testable.

#### Week 5: June 26 - June 30

School project

#### Week 6: July 3 - July 7

So here starts Phase 2, where I get to implement multi-broadcasting\!
The streaming code has been separated from EngineBroadcast into a new
class (ShoutOutput) that can be instanciated as needed. A ShoutOutput
instance is linked with a profile pointer (BroadcastProfilePtr). Values
are passed to libshout on connection start and when settings are applied
from the Live Broadcasting preferences panel. Frames are polled from
EngineBroadcast's thread like before, but are then passed to each
ShoutOutput's process() method. Connections within EngineBroadcast are
kept in sync with BroadcastSettings' profiles list using several
signals/slots.

Currently I see one design flaw in my code: instead of passing a
BroadcastProfilePtr to a ShoutOutput, ShoutOutput should be a child
class of BroadcastProfile. Since the profile is never changed during the
lifetime of a ShoutOutput instance, this would make the link between the
two more obvious and logical.

Week 7's work is for the Preferences UI. Testing is already possible
with the current UI, and the first WIP of the new UI will allow for
testing on several streaming outputs. // EDIT: bad idea.//

#### Week 7 and 8: July 10 - July 23

In this past two weeks, I managed to work my way mostly through UI work.
The QTableView used as a profile list is now properly formatted, and
removing profiles/connections is now possible. Working with QTableView
and Qt models was a bit confusing at first, but I managed to find
solutions for my problems.

Engine-wise, I've migrated most of EngineBroadcast's code to a separate
class called ShoutOutput. The initial design planned to pass each frame
received by EngineBroadcast to every instance of ShoutOutput with
ShoutOutput::process(), but this caused crackling audio (due to
excessive latency between calls to process()) when too many connections
were involved, with crackling increasing with the number of active
connections. In the end, each ShoutOutput now has a FIFO buffer where
EngineBroadcast puts new frames available to read. An idea to try out
would be to implement a "slow start" for the ShoutOutput threads, where
each thread waits for a defined number of available frames to be
available before processing them.

Still engine-wise but related to settings, I've made a lot of
improvements and bugfixes to the sync process between BroadcastSettings
and EngineBroadcast. There are still improvements to be made in that
area, though.

#### Week 9: July 24 - July 28

I finally managed to have working multi-broadcasting\! The initial
design was broken and lacked testing. Each ShoutOutput has its own FIFO
buffer, fed by EngineBroadcast's thread which is in turn fed by
EngineNetworkStream (responsible for overall buffer sync management).
The final version must get rid of EngineBroadcast's thread and have
proper buffer management as in EngineNetworkStream.

Regarding the idea of having secure password storage in XML profiles, I
managed to have a working implementation using QtKeychain, so that's one
less thing to worry about.

#### Week 10: July 31st - August 4

The secure password storage implementation is now complete, along with a
proper compile flag to disable it at compile time. The preferences UI
for Live Broadcasting has its design complete too. Work remains of minor
behaviour fixes and the ability to cancel changes made to profiles.
Engine-wise, work has been done to remove EngineBroadcast's thread and
have proper buffer management with multiple streaming connections as
SoundDeviceNetwork and EngineNetworkStream did before with a single
connection. Most of the heavy thinking has been done on this, so what
remains to do is putting proper structure into the latest changes.

#### Week 11: August 7 - August 11

Secure password storage now has error messages in case something goes
wrong when reading from or writing to the OS keychain. The preferences
UI now has proper separation between temporary settings and "live"
settings. To achieve this, the model parts of BroadcastSettings were
moved to a separate class, with a sync mechanism between the two
triggered only when applying settings. With this and the colorful
connection states, the preferences UI is near feature-complete. The
audio engine part is now complete: work on the audio engine refactor for
multi-broadcasting has been merged into the main work branch, and the
remaining bits to tidy up (input of NetworkStreamWorker, proper
structure) were addressed.

There's little much left to do on multi-broadcasting: bug hunting/fixing
and fixing minor UI aspects still in discussion. Next week's focus will
be to address these, as well as implementing new streaming encoders.

#### Week 12: August 14 - August 18

Opus, AAC and HE-AAC encoders are now a reality in Mixxx\! These
encoders are on the project's wishlist and much awaited by users. But in
the process, other aspects mentioned in the previous report were
slightly overlooked...

The Opus encoder uses libopus for encoding, and the resulting encoded
data in muxed into an Ogg stream using libogg. Opus streams embed in Ogg
need a special "OpusHead" header packet sent to make the stream
recognized as Opus data, and a "OpusTags" packet to provide stream/track
comments (artist/title metadata) to players in a format identical to
Vorbis comments. No library exists to generate instance of these two
packets, but fortunately the structure is easy to understand and simple
enough to implement with bit manipulations.

Each Opus frame has a fixed frame size in milliseconds, defined by the
user or developer among a set of possible values. This means the encoder
requires a specific amount of frames to be passed to it, no less, no
more. Whether in Live Broadcasting or Recording uses, the engine
provides way too much samples that the encoder can't process in one go,
so a FIFO buffer is used to store samples and get a specific number of
samples from it on each encoder call. The same situation happens in the
AAC encoder, with one difference: the frame size/sample count is not
configurable by the user.

The AAC encoder uses libfdk-aac and the resulting encoded data doesn't
need additional muxing or specific headers (these aspects are handled by
libfdk-aac, depending on encoder configuation). Mixxx's encoder
implementation currently supports AAC-LC (traditional plain AAC), HE-AAC
(previously AAC+) and HE-AAC v2.

The AAC encoder doesn't require libfdk-aac when compiling and
distributing Mixxx. Instead, the external library is loaded at run-time
(a process called dynamic loading) from a known name and location. This
behaviour is similar to Mixxx's use of libmp3lame for MP3 encoding. The
library can be placed in Mixxx's installation folder or searched for in
potential locations (including finding it in B.U.T.T's installation
folder on Windows if installed in AppData)

#### Final week: August 21 - August 27

Here it is. Three months and more than 170 (and counting) commits later,
the official final coding period for the Google Summer of Code is over.
Remaining engine issues in multi-broadcasting and, to a lesser extent,
the fdk-aac and Opus encoders have been fixed. Actual work is not over
yet\! Discussion is still going on regarding some few specific details
of the new Live Broadcasting user experience and takes place in the
GitHub Pull Request for multi-broadcasting.

It's been an honor as well as a great pleasure to work on Mixxx during
GSoC. In the process, I got better at C++ and with Qt and had a glimpse
at what an audio engine looks like. Once the work on multi-broadcasting
is done, I'd be happy to contribute other features to Mixx outside of
GSoC. Thanks to the Mixxx Team (and Daniel, my mentor) for letting me be
part of this adventure\!
