# Mixxx User Experience Design Philosophy

This is a proposal to provide guiding principals for the design of
Mixxx.

1.  **The answer is not more options.** If you feel compelled to add a
    preference that's exposed to the user, it's very possible you've
    made a wrong turn somewhere. (Copied from
    [Signal](https://github.com/WhisperSystems/Signal-Android/blob/master/CONTRIBUTING.md#development-ideology).)
2.  **Live performance is the focus.**
    1.  Features that are meant to be used while mixing must be easily
        accessible with a minimum of steps (clicks, button presses, or
        other interactions) required to use them. Features whose use is
        not time sensitive do not need to be as easily accessible.
    2.  Discoverability matters, but being intuitive and easy to use
        while performing is more important.
    3.  Minimize mutable state, because the more moving parts a user has
        to keep track of, the more likely it is they will do something
        accidentally.
3.  **"Works for me" is not good enough.** It must work for everyone.
    People use Mixxx with a wide variety of hardware with a wide variety
    of music for a wide variety of purposes. Your changes should not
    interfere with how other people use Mixxx. Minimize assumptions
    about how people use Mixxx.
4.  **Everyone can be a power user.** Everyone should be able to use and
    understand all features of Mixxx. If they cannot, the design and/or
    documentation are not good enough.
