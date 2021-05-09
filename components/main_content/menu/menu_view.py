from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt5 import Qt

from components.main_content.menu.menu_controller import MenuController


class MenuView(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.controller = MenuController(self)

        self.setAttribute(Qt.Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "* {background: qlineargradient( x1:1 y1:-0.5, x2:1 y2:0.5, stop:0 rgb(25, 24, 38), stop:1 rgb(48, 48, 64));}")

    def initialize_menu(self, playlists):
        layout = QVBoxLayout()
        self.listwidget = self._create_list(playlists)

        layout.addWidget(self.listwidget)
        self.setLayout(layout)

    def _create_list(self, playlists):
        listwidget = QListWidget()

        for i, playlist in enumerate(playlists):
            listwidget.insertItem(i, playlist)

        listwidget.clicked.connect(self._clicked)
        return listwidget

    def _clicked(self, index):
        playlist = self.listwidget.currentItem().text()
        self.controller.clicked(playlist)
