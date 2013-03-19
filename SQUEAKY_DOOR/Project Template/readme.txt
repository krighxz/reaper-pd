REAPER template for SQUEAKY_DOOR.pd

Tracks 2-5 send variant parameters to PD patch:
Track 2: Hinge 1
Track 3: Hinge 2
Track 4: Noise source
Track 5: Resonator

NB: do *NOT* change track order or messages won't be sent correctly (track
re-ordering functionality might be implemented one day, but this is somewhat
complicated and needs to be handled on the client (pd) side - I think)

Rename Track 1 to preset name to be loaded into PD everytime track is renamed,
PD loads corresponding preset.

For easy navigation in REAPER:
-go to Actions -> Show action list...
-filter 'Envelope: Toggle display all visible envelopes in lanes for tracks'
-add shortcut to action (e.g. [E] or [shift]+[T], etc.)
This allows you to expand and collapse envelopes for selected track.

Also add empty items to each track (at least as long as sample being matched).
This makes it possible to select all items and drag them along the timeline to
move multiple envelopes at once.

REAPER outputs following OSC messages (using squeakydoor.ReaperOSC):

/track/#/fx/#/fxparam/#/value [value]	//whenever a parameter changes
/track/#/name [name]			//whenever track is renamed
/track/#/mute [0/1]			//whenver track is (un)muted
/time [time in seconds]			//whenever marker moves
