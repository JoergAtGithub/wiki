# Broadcasting your Mixxx over the Internet

Hello, all\! It's thread here with a quick description of how I have
Mixxx stream out to dnbradio.com's shoutcast servers every Tuesday.

I run mixxx under the Ubuntu-based linux distribution, Crunchbang Linux.
Using Jack, I feed Mixxx's main L/R outputs to the simple, console-based
edcast (<http://www.oddsock.org/tools/edcast_jack/>), which is then able
to encode the audio to mp3 in realtime and feed it up to the remote
server.

I fire up Jack using the very simple frontend, qjackctl. Then I start
Mixxx and set it to output its audio via Jack. After some
straightforward editing of the edcast configuration file, I launch it,
specifying the configuration file and the jack sockets to stream from,
with something like this:

`~/apps/edcast$ bin/edcast -c etc/edcast.conf portaudio-0 portaudio-1`

And if all goes well, edcast will start telling you how many kilobits
were sent up every second, until it is killed with ctrl+c.
