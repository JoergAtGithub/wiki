# Broadcasting your Mixxx over the Internet

We are working on including direct Shoutcast/Icecast support in Mixxx.
It currently has [some
problems](http://mixxx.org/wiki/doku.php/1.8.0_to_do_list#shoutcast)
that are serious enough to prevent us from turning it on by default.
However, the more adventurous among you are free to build Mixxx v1.7.x
or later with the `shoutcast=1` flag to give it a try.

In the meantime, please use the following method that has worked well
for one of our users for years.

## Linux via JACK and edcast

Hello, all\! It's **thread** here with a quick description of how I have
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

`~/apps/edcast$ bin/edcast -c etc/edcast.conf PortAudio:out_0
PortAudio:out_1`

And if all goes well, edcast will start telling you how many kilobits
were sent up every second, until it is killed with ctrl+c.
