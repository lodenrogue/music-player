class PlayerCallback:

    def __init__(self, event_emitter):
        self.event_emitter = event_emitter


    def on_downloading_song(self, song):
        self.event_emitter.emit('downloading_song', song)

    def on_song_started(self, song):
        self.event_emitter.emit('song_started', song)
