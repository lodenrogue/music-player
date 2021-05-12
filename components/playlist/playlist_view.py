from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QListWidget
from PyQt5.QtWidgets import QAbstractItemView

from components.playlist.playlist_controller import PlaylistController

class PlaylistView(QWidget):

    def __init__(self, event_emitter, player):
        QWidget.__init__(self)
        self.listWidget = QListWidget()
        self.listWidget.clicked.connect(self._song_selected)

        layout = QGridLayout()
        layout.addWidget(self.listWidget)
        self.setLayout(layout)

        self.controller = PlaylistController(self, event_emitter, player)

    def show_songs(self, songs):
        self.listWidget.clear()

        for i, song in enumerate(songs):
            self.listWidget.insertItem(i, song)

    def _song_selected(self, _):
        item = self.listWidget.currentItem()
        self.controller.select_song(item.text())
