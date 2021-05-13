from threading import Thread

from components.playlist.player_callback import PlayerCallback


class PlaylistController:

    def __init__(self, view, event_emitter, player):
        self.view = view
        self.player = player
        self.player_callback = PlayerCallback(event_emitter)

        self.event_emitter = event_emitter
        self.event_emitter.on("playlist_selected", self._on_playlist_selected)

    def _on_playlist_selected(self, playlist):
        self.playlist = playlist
        self.songs = self.player.list_songs(self.playlist)
        self.view.show_songs(self.songs)

    def select_song(self, song):
        index = self.songs.index(song)

        thread = (Thread(
            target=self.player.play,
            args=(self.playlist, self.player_callback, index)))

        thread.start()
