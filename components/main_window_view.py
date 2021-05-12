from PyQt5.QtWidgets import QWidget, QGridLayout
from pymitter import EventEmitter

# from components.main_content.main_content_view import MainContentView
# from components.player_info.player_info_view import PlayerInfoView

from player import Player
from components.options.options_view import OptionsView
from components.playlist.playlist_view import PlaylistView


class MainWindowView(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        event_emitter = EventEmitter()
        player = Player()

        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        # layout.addWidget(MainContentView(), 11)
        # layout.addWidget(PlayerInfoView(), 1)
        # layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(OptionsView(event_emitter, player), 0, 0)
        layout.addWidget(PlaylistView(event_emitter, player), 0, 1)
        self.setLayout(layout)
