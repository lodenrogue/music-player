from PyQt5.QtWidgets import QWidget, QGridLayout
from pymitter import EventEmitter

# from components.main_content.main_content_view import MainContentView
# from components.player_info.player_info_view import PlayerInfoView

from player import Player
from components.options.options_view import OptionsView
from components.playlist.playlist_view import PlaylistView
from components.player_info.player_info_view import PlayerInfoView


class MainWindowView(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        event_emitter = EventEmitter()
        player = Player()

        content = self._create_content_layout(event_emitter, player)
        
        layout = QGridLayout()
        layout.addLayout(content, 0, 0)
        layout.addWidget(PlayerInfoView(event_emitter, player), 1, 0)

        layout.setRowStretch(0, 10)
        layout.setRowStretch(1, 1)
        self.setLayout(layout)

    def _create_content_layout(self, event_emitter, player):
        content = QGridLayout()
        content.setColumnStretch(0, 1)
        content.setColumnStretch(1, 6)
        content.addWidget(OptionsView(event_emitter, player), 0, 0)
        content.addWidget(PlaylistView(event_emitter, player), 0, 1)
        return content
