from player import Player
from threading import Thread

class MenuController:

    def __init__(self, view):
        self.player = Player()
        playlists = self.player.list_playlists()

        view.initialize_menu(playlists)

    def clicked(self, playlist):
        thread = Thread(target=self.player.play, args=(playlist,))
        thread.start()
