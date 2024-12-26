# Instant/live download & streamed track support

[Launchpad
blueprint](https://blueprints.launchpad.net/mixxx/+spec/streamed-live-downloaded-tracks)

There is much interest in being able to play tracks directly from
various streaming services in Mixxx during a DJ set. Since each service
may have different terms of use both for the service itself and its API,
Mixxx needs a library plug-in mechanism where each service's plugin is
loaded from a shared object file (`.so, .dylib, .dll`). This
architecture provides the most stability and flexibility.

As well, since much of the infrastructure required for streamed track
support applies to direct downloading within Mixxx such as from online
stores and music services/DJ pools, we should implement with this use
case in mind as well. (For example, to avoid drop-outs mid-song, it
would be useful to cache large portions of a streamed track, which is
essentially a download.)

## Preconditions

  - Qt5 (in progress for Mixxx 2.2.x)
  - Library Redesign single pane (in progress for 2.2.x) 

## Steps

The time estimates are rough, given in person-weeks. (One developer
working 40 hours.)

### Library plug-Ins

  - Find and load Library plug-Ins: 1 PW 
  - Make preferences extensible, in this case a Live Tracks icon on the
    left that shows a custom preferences pane for each loaded service
    plug-in: 1 PW
  - Make Library side bar extensible and show custom content in the
    pane: 1 PW
  - Add column in Library that marks a track as downloadable/not-local,
    with a hint on how to fetch it, redirecting to a download link: 1 PW
    (We can also consider moving Traktor/Rythmbox/Banshee support to
    this concept)

### Implement a demo download Web page plug-in

This would be useful to get something working in the short term until
complete Library support is added.

  - Implement the preferences page with an independent preferences file:
    1 PW
  - Implement a Web view in the Library: 1 PW 
  - This would require cooperation with the streaming service to provide
    a simplified page on their server
  - Implement a DownloadListener that downloads the track to a temp
    folder and creates the Library entry: 2 PW

### Code review & testing

\~4 person-weeks

### Manual update

\~4 person-weeks

## Ideal service API

The streaming/download service's API should be a JSON-based REST
interface providing methods to do at least the following.

  - **Authenticate the user**, then return an access token on success to
    use for the rest of the session with the other methods
  - **Submit a search query** for all fields as well as track name,
    artist name, genre, bpm, key and label individually, with a
    parameter that limits the number of returned items and one to
    specify which metadata fields to return for each track
  - **Retrieve metadata** for a specific track ID
  - **Initiate/resume a download** with parameters for the track ID, the
    byte to start with (first if not specified), and an optional one for
    the byte to end with in the case of a streaming track (see below)
  - **Verify the checksum** of a downloaded full or partial track with
    parameters for the algorithm and track ID, and optional parameters
    for start & end byte in the case of a partial download. (CRC32 is
    preferred as it's much faster than cryptographic algorithms and
    designed to catch data transport errors.)

The same download method would work for streamed tracks as well. The
metadata returned during the search could include a "streaming only"
flag, so Mixxx would handle the track differently based on that, the
only real difference being that Mixxx would only save the track to a
temporary area (encrypted if required using a temporary in-memory-only
key) if the track is streaming-only.
