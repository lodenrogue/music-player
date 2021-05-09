from PyQt5.QtWidgets import QWidget, QVBoxLayout

from components.main_content.main_content_view import MainContentView
from components.player_info.player_info_view import PlayerInfoView


class MainWindowView(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        layout.addWidget(MainContentView(), 11)
        layout.addWidget(PlayerInfoView(), 1)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
