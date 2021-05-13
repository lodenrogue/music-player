class PlayerInfoController:

    def __init__(self, view, event_emitter, player):
        self.view = view
        self.event_emitter = event_emitter

        self.event_emitter.on('downloading_song', self._on_downloading_song)
        self.event_emitter.on('song_started', self._on_song_started)

    def _on_downloading_song(self, song):
        self.view.update_info(f'Downloading {song}')

    def _on_song_started(self, song):
        self.view.update_info(f'Playing {song}')
