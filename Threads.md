# Threads in Mixxx

Mixxx is a highly multi-threaded program.

Here is a list of the threads Mixxx runs, as of 1.6.2:

  - GUI thread
  - MIDI thread - Receives MIDI events from hardware and sends through
    MIDI mapping system onto Mixxx's controls or to script functions.
  - MidiScriptEngine thread - executes any MIDI scripting functions
  - Audio thread (runs from PortAudio callback) - Does all audio
    processing that eventually hits your soundcard/ears. :)
  - Analyser thread - Performs BPM detection, wave summary generation
    (the mini waveforms)
  - 2 x Reader threads - Decode MP3s, OGGs, etc. asynchronously. Feeds
    decoded audio into EngineBuffer ringbuffer.
  - 2 x VinylControl threads - Process timecode signals 
  - Sidechain thread - Does non-realtime processing of audio. Used for
    recording to disk and shoutcast broadcasting.

Note that a list of threads can be seen when you [generate a backtrace
with GDB](creating_backtraces), like this one:

``` 
(gdb) thread apply all bt
 
Thread 14 (Thread 0xa3b25b90 (LWP 7427)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb686dae7 in poll () from /lib/tls/i686/cmov/libc.so.6
#2  0xb7cd66d6 in ?? () from /usr/lib/libportaudio.so.2
#3  0xb7cd7f57 in ?? () from /usr/lib/libportaudio.so.2
#4  0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#5  0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 13 (Thread 0xa43d4b90 (LWP 7409)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb686dae7 in poll () from /lib/tls/i686/cmov/libc.so.6
#2  0x081cf632 in MidiObjectALSASeq::run (this=0x9ba7c00)
    at src/midiobjectalsaseq.cpp:271
#3  0xb6d9593e in ?? () from /usr/share/qt4/lib/libQtCore.so.4
#4  0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#5  0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 12 (Thread 0xafd12b90 (LWP 7408)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb686dae7 in poll () from /lib/tls/i686/cmov/libc.so.6
#2  0xb63276fb in IA__g_poll (fds=0x9ac9658, nfds=1, timeout=-1)
    at /build/buildd/glib2.0-2.19.8/glib/gpoll.c:127
#3  0xb6319ef2 in g_main_context_iterate (context=0x9c332f0, block=1,
    dispatch=1, self=0xa004da0)
    at /build/buildd/glib2.0-2.19.8/glib/gmain.c:2761
#4  0xb631a1d8 in IA__g_main_context_iteration (context=0x9c332f0, may_block=1)
    at /build/buildd/glib2.0-2.19.8/glib/gmain.c:2511
#5  0xb6eb53a8 in QEventDispatcherGlib::processEvents ()
   from /usr/share/qt4/lib/libQtCore.so.4
#6  0xb6e87ffa in QEventLoop::processEvents ()
   from /usr/share/qt4/lib/libQtCore.so.4
#7  0xb6e8843a in QEventLoop::exec () from /usr/share/qt4/lib/libQtCore.so.4
#8  0xb6d92609 in QThread::exec () from /usr/share/qt4/lib/libQtCore.so.4
#9  0x08220e5b in MidiScriptEngine::run (this=0x9ba7de0)
    at src/script/midiscriptengine.cpp:96
#10 0xb6d9593e in ?? () from /usr/share/qt4/lib/libQtCore.so.4
#11 0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#12 0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 10 (Thread 0xb0513b90 (LWP 7391)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb7cbb0e5 in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /lib/tls/i686/cmov/libpthread.so.0
#2  0xb6d96982 in QWaitCondition::wait ()
   from /usr/share/qt4/lib/libQtCore.so.4
#3  0x080f87ba in AnalyserQueue::dequeueNextBlocking (this=0x9900bd8)
    at src/analyserqueue.cpp:32
#4  0x080f9376 in AnalyserQueue::run (this=0x9900bd8)
    at src/analyserqueue.cpp:97
#5  0xb6d9593e in ?? () from /usr/share/qt4/lib/libQtCore.so.4
#6  0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#7  0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 4 (Thread 0xb2cc5b90 (LWP 7104)):
#0  0xb6a3c601 in ?? () from /usr/lib/libmp3lame.so.0
#1  0x00000000 in ?? ()
 
Thread 3 (Thread 0xb3ca4b90 (LWP 7103)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb7cbb0e5 in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /lib/tls/i686/cmov/libpthread.so.0
#2  0xb6d96982 in QWaitCondition::wait ()
   from /usr/share/qt4/lib/libQtCore.so.4
#3  0x0815a6f8 in Reader::run (this=0x8e41320) at src/reader.cpp:252
#4  0xb6d9593e in ?? () from /usr/share/qt4/lib/libQtCore.so.4
#5  0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#6  0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 2 (Thread 0xb4ae6b90 (LWP 7102)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb7cbb0e5 in pthread_cond_wait@@GLIBC_2.3.2 ()
   from /lib/tls/i686/cmov/libpthread.so.0
#2  0xb6d96982 in QWaitCondition::wait ()
   from /usr/share/qt4/lib/libQtCore.so.4
#3  0x0815a6f8 in Reader::run (this=0x8e5a988) at src/reader.cpp:252
#4  0xb6d9593e in ?? () from /usr/share/qt4/lib/libQtCore.so.4
#5  0xb7cb74ff in start_thread () from /lib/tls/i686/cmov/libpthread.so.0
#6  0xb687849e in clone () from /lib/tls/i686/cmov/libc.so.6
 
Thread 1 (Thread 0xb6160710 (LWP 6987)):
#0  0xb7f65430 in __kernel_vsyscall ()
#1  0xb686dae7 in poll () from /lib/tls/i686/cmov/libc.so.6
#2  0xb63276fb in IA__g_poll (fds=0x8f25f08, nfds=12, timeout=5)
    at /build/buildd/glib2.0-2.19.8/glib/gpoll.c:127
#3  0xb6319ef2 in g_main_context_iterate (context=0x8c4b110, block=1,
    dispatch=1, self=0x8c49148)
    at /build/buildd/glib2.0-2.19.8/glib/gmain.c:2761
#4  0xb631a1d8 in IA__g_main_context_iteration (context=0x8c4b110, may_block=1)
    at /build/buildd/glib2.0-2.19.8/glib/gmain.c:2511
#5  0xb6eb53a8 in QEventDispatcherGlib::processEvents ()
   from /usr/share/qt4/lib/libQtCore.so.4
#6  0xb7162a55 in ?? () from /usr/share/qt4/lib/libQtGui.so.4
#7  0xb6e87ffa in QEventLoop::processEvents ()
   from /usr/share/qt4/lib/libQtCore.so.4
#8  0xb6e8843a in QEventLoop::exec () from /usr/share/qt4/lib/libQtCore.so.4
#9  0xb6e8a8e9 in QCoreApplication::exec ()
   from /usr/share/qt4/lib/libQtCore.so.4
#10 0xb70c1497 in QApplication::exec () from /usr/share/qt4/lib/libQtGui.so.4
#11 0x080fe8e2 in main (argc=1, argv=0xbfa81494) at src/main.cpp:305
(gdb) 
```

## Consolidation

This is a workspace to organize thread consolidation efforts.

### Controllers

Currently, Mixxx starts two threads **for each active controller**:

1.  polls PortMIDI for data
2.  runs the MIDI script engine

Thanks to input from \#qt:

##### Ideal case - Callbacks/Events

A single "Controller Engine" thread with an event loop in which all
ControllerEngines run. They receive callbacks/event notifications from
the Controller back-ends containing data received, then act on the data.
If the callback occurs in a different thread, signal the target
functions with the data. (Signal in all cases for consistency.)

##### Next-best case - Blocked Polling

// This essentially implements a callback mechanism. * - Separate thread
for each controller that does nothing but polling using a blocking
method. When data is received, dispatch it via a signal to the
associated ControllerEngine and block for new data again. - A single
"Controller Engine" thread with an event loop in which all
ControllerEngines run. They receive signals from the Controller polling
threads containing data received and act on the data. *HIDAPI can use
this method//

##### Third-best case - Non-blocked Polling

A single "Controller Manager" thread that runs a Qt event loop (standard
run()) but sets up a (1ms) timer that sequentially polls all active
controllers for data, operating on any new data by invoking the
respective ControllerEngine. The upside of this method is simplicity: no
locking is required anywhere in the Controller subsystem and the
back-ends need not be thread-safe since only this one thread will
communicate with them.

*Note that if an API is not thread-safe (i.e. there should be at most
one thread executing a call to the API at any point in time,) you have
to use this method, or you will not be able to send data to the
controller asynchronously (data will first have to be received to
release the block.) PortMIDI is in this camp.* :(

#### Plan

Set up a hybrid system whereby we can use the best method available for
each API: Have a ControllerManager::register() function that allows each
Controller to register the method it API requires.
