from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class PlaylistMenuOptionView(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Icon"))
        layout.addWidget(QLabel("Playlists"))
        self.setLayout(layout)

        self.mouseReleaseEvent = self._clicked

        self.setStyleSheet(
            "* { background: rgba(0, 0, 0, 0); }")

    def _clicked(self, index):
        print("clicked playlist")
