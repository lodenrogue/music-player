from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from components.player_info.player_info_controller import PlayerInfoController


class PlayerInfoView(QWidget):

    def __init__(self, event_emitter, player):
        QWidget.__init__(self)

        self.label = QLabel()
        self.label.setText('Player info')
        self.label.setObjectName('player-info')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.controller = PlayerInfoController(self, event_emitter, player)

    def update_info(self, message):
        self.label.setText(message)
