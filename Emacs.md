# Setting up Emacs for Mixxx developement

[Emacs](https://www.gnu.org/software/emacs/) is a powerful text editor
that can be heavily customised to serve as a modern IDE.

With the correct configuration you'll be able to

  - edit C/C++, xml, javascript, python and more
  - auto completion
  - smart navigation
  - compile the project
  - debug the poject
  - interface with git

all without the need to ever exit or close emacs.

## Warning

Emacs is an old piece of software (first release at 1976) and a lot of
terminology used is different than what most people are used to.

For the first many hours of usage your productivity will be extremely
low, since you have to remember a bunch of keybindings and commands just
to be able to save a document or open a new file. But after spending
some time in it you'll find that the commands become muscle memory and
you never think about them any more, just like touch-typing.

It is not recommended to start developing with emacs if you don't
already have at least some familiarity with it.

That said, even after 42 years there is a big and active community of
developers and users around Emacs and it is safe to say that it keeps
growing. If you want to learn emacs there are a lot of guides out there.
I'll list some below.

## Guides

[Here](https://tuhdo.github.io/index.html) you can find one of the best
collections of tutorials I've found online written by
[tuhdo](https://github.com/tuhdo). He has written many widely used emacs
packages. Start by reading the [Emacs mini manual
part 1](https://tuhdo.github.io/emacs-tutor.html) and then proceed to
[this](https://tuhdo.github.io/c-ide.html) to learn about the packages
you'll need for an IDE experience and how to configure them.

## Details & Packages

In order for the editor to provide smart assistance with the code (auto
completion, code navigation etc.) there has to be a list of the compiler
commands so the selected backend can use it to find out where each
function is and how it is related to one another. CMake can do this
easily with `cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`. To get the same
results with SCons you need to use an external program called
[bear](https://github.com/rizsotto/Bear) (Build EAR).

### Irony

One popular backed is [irony](https://github.com/Sarcasm/irony-mode).
Using this and [company-irony](https://github.com/Sarcasm/company-irony)
for auto completion along with
[flycheck-irony](https://github.com/Sarcasm/flycheck-irony) for on the
fly syntax checking has you covered for everything except code
navigation.

### RTags

Code navigation is what [RTags](https://github.com/Andersbakken/rtags)
does best. It provides functions to jump to definition or to
declaration, and many many others. You can also use it with company-mode
for auto completion.

### ymcd

[ymcd](https://github.com/abingham/emacs-ycmd) is another package that
has support for many languages besides C/C++.
[Here](https://onze.io/emacs/c++/2017/03/16/emacs-cpp.html) is a guide
for a setup using this tool.

### cquery

[cquery](https://github.com/cquery-project/cquery) is really easy to set
up and provides everything: syntax checker, auto-completion, navigation,
documentation. It's developed for and tested with huge codebases. It can
also work without a `compiler_commands.json` making it even greater for
mixxx since with scons generating the json can be quite hard. Everything
you need to install it can be found in the repo's wiki.

### magit

[magit](https://magit.vc/) is considered to be one of the best packaged
out there. Rumours say that some open emacs just for this (even vim
users). It is a git interface that is extremely fast and intuitive and
makes almost every task in git easier. One minor issue is that it can't
handle big merges, since it will take forever to load each commit. This
is still best done via terminal.

### Debugging

Emacs has a build in interface for GnuDebugger (gdb). You can find the
details of how to set it up in tuhdo's guide I mentioned above.

## Conclusion

> Most people don't treat configuration files as software. I do.
> 
> \- Emacs user

Emacs is all about trying new stuff and having fun. I hope this
collection of links and tools can help anyone who might need them.
