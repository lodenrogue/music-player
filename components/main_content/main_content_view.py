from PyQt5.QtWidgets import (QWidget, QHBoxLayout)

from components.main_content.menu.menu_view import MenuView
from components.main_content.content.content_view import ContentView


class MainContentView(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        layout.addWidget(MenuView(), 1)
        layout.addWidget(ContentView(), 4)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
