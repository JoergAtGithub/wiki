# Ctlra Support

This page introduces the reader to the proposed work to integrate the
[Ctlra library](http://openavproductions.com/doc/ctlra.html) with Mixxx.
The main advantage to doing this is hotplug support for USB HID devices.
The Ctlra library is written in plain C, and developed/tested on Linux.
The library currently supports a range of USB HID devices that are not
supported by ALSA/Linux-kernel.

Please see the following 1 hour talk on Ctlra, presented at the Linux
Audio Conference '17. [OpenAV Ctrla: A library for Tight Integration of
Controllers - Harry Van
Haaren](https://www.youtube.com/watch?v=-bwynA7HRow)

### Code / Plan

The Ctlra library is a plain C library, so integrating it is not
particularly difficult from a Code point of view. Integrating it at the
correct abstraction is more difficult - Ctlra does not provide an
"instance" of each controller, as doing so would make hotplug very
difficult to support transparently to the application.

In initial prototyping, the Ctlra library was instantiated as a derived
class of a Mixxx "Controller". This is \*not\* the correct abstraction,
given that one Ctlra instance can support multiple devices.

Given this fact, it seems best to have the Ctlra instance in the
ControllerManager class, and for each device that is "known" to Ctlra,
we can instantiate a "Controller" class instance to represent it. Surely
there will be something else that becomes more difficult by moving the
main controller instance up a level, but this is the correct level of
abstraction (from experience of attempting integration).

##### Threading

The Ctlra library itself doesn't create any threads. It uses the libUSB
library to access USB devices, and uses the async() mode for all
transfers to not block any threads. The HIDUSB library was concidered,
but due to its tendency to toy with thread creation/joining it was not
used. As a result, the Ctlra library must be polled, which means that
every X ms, a thread must call ctlra\_poll() function.

This thread is created once at a the Ctlra instance level, and the same
thread is used to poll all controllers using async() USB callbacks.
Events are transmitted to a provided callback - more details further,
keep reading\!

### Events Callbacks

In Ctlra, all actions (physical modification of a control surface)
result in "events" being sent to an application specified callback
function. This callback function performs a switch() based on the event,
and can perform a particular action. The callback function can be
implemented in C, or cast to a C++ class using the available void\* for
userdata.

##### Handling Input

Input is handled in the user-supplied callback. Any events can trigger
ControlProxy writes, which allow controlling the Mixxx engine. Given the
callback is a C function, it must be compiled and linked into the
binary. Although inflexible, it does provide huge performance and
gauranteed results.

In order to provide a more flexible method of handling events, the
[TCC](https://bellard.org/tcc/) compiler can be used, to \*dynamically
generate and link\* C code into Mixxx, during runtime. The resulting
functions can be run using function-pointers. This has been prototyped
in the Ctlra library, \*AND\* in the Mixxx POC implementation, and works
like a dream. The TCC feature will not be in the initial PR, however it
is worth mentioning and being aware of in order to understand the
value-add of the Ctlra addition to Mixxx.

##### Handling Feedback

Feedback can be written to any controller using a few Ctlra APIs. The
APIs update the state of the LEDs and other controllable items on a
physical device. The state of the Mixxx engine is retrieved using
ControlProxy objects, and based on the state of the ControlProxy, the
feedback can be updated on the device itself.

### Contact

Harry van Haaren (OpenAV) is the contact point for this work. Please
email me ([harryhaaren@gmail.com](harryhaaren@gmail.com) ), and we can
organize a time to discuss this topic on \#mixxx IRC channel, or
somewhere else where a record of conversation is maintained.

Thanks for reading, and I hope you find the proposed Ctlra work as
interesting as I do :)
