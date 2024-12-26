Virtual DJ stores its entire library in a XML file called database.xml.
The default location under Windows is at
C:\\Users\\\<username\>\\Documents\\VirtualDJ. The file format is pretty
self-explanatory where each track or sample has the following structure:

    <?xml version="1.0" encoding="UTF-8"?>
    <VirtualDJ_Database Version="8.2">
    
    <Song FilePath="C:\Users\ntmusic\Music\beatmatch\beatmatch1.wav" FileSize="25724840">
      <Tags Author="NTMusic" Flag="1" />
      <Infos SongLength="72.915782" FirstSeen="1518996996" Bitrate="2822" Cover="34" />
      <Scan Version="801" Bpm="0.507959" AltBpm="0.380975" Volume="0.246516" Key="A#" Flag="32768" />
      <Tags Author="NTMusic" Flag="1" />
      <Infos SongLength="72.915782" FirstSeen="1518996996" Bitrate="2822" Cover="34" />
      <Scan Version="801" Bpm="0.507959" AltBpm="0.380975" Volume="0.246516" Key="A#" Flag="32768" />
      <Poi Pos="3.721451" Type="beatgrid" />
      <Poi Pos="3.723900" Type="automix" Point="realStart" />
      <Poi Pos="72.872925" Type="automix" Point="realEnd" />
      <Poi Pos="3.723900" Type="automix" Point="fadeStart" />
      <Poi Pos="72.300000" Type="automix" Point="fadeEnd" />
      <Poi Pos="5.194014" Type="automix" Point="cutStart" />
      <Poi Pos="70.210612" Type="automix" Point="cutEnd" />
      <Poi Name="Cue 1" Pos="15.912449" Num="1" />
      <Poi Name="Cue 2" Pos="17.436327" Num="2" />
      <Poi Name="Cue 3" Pos="18.960204" Num="3" />
      <Poi Name="Cue 4" Pos="19.976122" Num="4" />
     </Song> 
     
     </VirtualDJ_Database>

All cue points are available as part of the POIs collection.
