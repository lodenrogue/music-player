from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5 import Qt


class ContentView(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        label = QLabel()
        label.setText('Content')

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        self.setAttribute(Qt.Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "* {background: qlineargradient( x1:0.5 y1:-0.5, x2:1 y2:0, stop:0 rgb(25, 24, 38), stop:1 rgb(25, 24, 38));}")
