from player import Player


class OptionsController:

    def __init__(self, view, event_emitter, player):
        self.view = view
        self.event_emitter = event_emitter
        self.player = player
        self.view.initialize_options(self.player.list_playlists())

    def select_playlist(self, playlist):
        self.event_emitter.emit("playlist_selected", playlist)
