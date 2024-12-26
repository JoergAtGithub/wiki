Hello,

As you know from the last report, the implementation for button type
effect parameters was in need of a refactoring, because of code
duplication inside ***EffectParameterSlot*** and
***EffectButtonParameterSlot***. I introduced a base class for those two
(***EffectParameterSlotBase***) which packs the common code.

The final step was displaying labels for button parameters too.
***legacyskinparser.cpp*** is in charge of parsing and creating the
necessary QLabels. It has a special method for parsing
***EffectParameterName*** nodes which was instantiating a
***WEffectParameter***. I had to create another method for parsing
***EffectButtonParameterName*** nodes which had to instantiate a
***WEffectButtonParameter***. Because the code for these was similar I
created a base class for both of them which stores a pointer to an
***EffectParameterSlotBase*** which had been introduced earlier and it
provides access to the name and description of the parameter, regardless
its nature (button or knob). This base class has a pure virtual
***setup()*** method which allowed me to use it inside the parsing
methods. I did a pull request\[1\] for this feature and I am now waiting
for review.

I stated in the last report that the best way of controlling the EQ
Effect Rack and maintaining compatibility with skins and controllers was
adding support for control aliasing. It was a misunderstanding about
this feature and it made me lose precious time. I thought the aliases
must be registered at the beginning of Mixxx, before the original
controls were created. The only way of doing this was not optimal,
because two hash look ups were necessary each time a control was
requested. The correct way of using aliases is to create them after the
controls to which they are pointing have been instantiated. This leads
to two possible ways of registering aliases. Either you create an alias
right after the original control has been created or you put the desired
aliases inside ***MixxxMainWindow::createCOAliases*** method which I
have introduced. It gets called just before loading the skin and before
initializing the controllers.

After control aliasing, it was time for configuring the newly added
***EffectRack*** from preferences. These are the steps taken towards the
final implementation:

  - Static implementation: I hard coded 4 check boxes which were
    responsible of selecting between 2 effects for each deck.
  - Add a new slot (***slodLoadEffectOnChainSlot***) which is
    responsible for loading a certain effect on a given
    ***EffectChainSlot*** and ***EffectSlot***.
  - Use combo boxes instead of check boxes to allow selecting between
    multiple effects
  - Dynamically create the desired number of drop down lists based on
    how many decks are available
  - I achieved this by connecting the "\[Master\],num\_decks" control to
    a slot inside ***dlgprefeq.cpp*** which adds the correct number of
    combo boxes.
  - Avoid duplicate code for slots by using ***sender()*** method
    provided by Qt to check which combo box was modified and emit the
    correct signal for effect change.
  - Add labels next to each drop down list which display the deck
    affected by that combo box.
  - Make the user's preferences persistent
  - Use ***m\_pConfig*** to store the current configuration of the
    EffectRack. Upon the first effect instantiations look up if the user
    has a configuration for the rack. If not, use the default equalizer.

I also spotted two bugs this week. One of them is about the parameter
knobs which are not properly updating when an effect is loaded onto an
effect slot. Fortunately, Daniel opened a pull request\[2\] which fixes
this bug.

The other bug is IMHO critical and it should be fixed as soon as
possible. Mixxx is crashing due to a 'bad\_alloc' error if we cycle
through a lot of effects (on my laptop I roughly counted about 140
effect changes until I got the error). I stumbled upon this bug in my
first implementation of the EQ Rack preferences. I got around it by
storing the instantiated effects inside the class which used them. When
an effect is loaded onto a slot, a new effect instantiation is occurring
and the previous effect is not freed (or at least I have not found the
code for freeing the previously loaded effect upon loading the new one).
My intuition tells me that we might run out of heap memory.

I had a fun week because I learned a couple of interesting things and I
got the chance to experiment with GUI elements and how they communicate
through signal and slots with the back end. A nice Qt thing is
***QComboBox::addItems()*** which is taking a list of QStrings and adds
those strings as separate options of the drop down list. Before finding
this method I added each entry manually inside a ***foreach*** loop.

Playing with initialization lists in C++ I got a -Wreorder warning at
compile time. It is informing you that you are initializing members in
another order than their order of declaration. At first I thought this
is an useless warning, but after doing a quick research I found out that
serious and hardly detectable bugs can emerge by overlooking this
warning. For example I have inside ***DlgPrefEq*** class two members:
one (lets call it ***A***) which is initialized with a value got as an
argument, and the other one (lets call it ***B***) is initialized by
calling a method on the previous member. Naturally, inside the
initialization list I'll initialize ***A*** and then ***B***. But, if
inside my class ***B*** is declared before ***A***, it is initialized
first (this is the way C++ is doing: initializing members in their order
of declaration). Because it is depending on ***A*** (which is not
initialized for the moment), our program will crash.

Another interesting thing I learned this week is the ***-p*** command
line argument passed to ***git commit***. I tend to make a lot of
modifications to the code before deciding to make a commit. By
committing with ***-p*** argument I can cycle through modifications and
select which ones I want to stage for the next commit. It is better for
code review and for debugging if I break my work into smaller commits.

Stay tuned for next week's report\!

Cheers,  
Nicu Badescu

\[1\] - <https://github.com/mixxxdj/mixxx/pull/281/>  
\[2\] - <https://github.com/mixxxdj/mixxx/pull/279/>  
[Back to the main page\!](extending_the_effects_engine)
