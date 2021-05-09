from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class PlayerInfoView(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        label = QLabel()
        label.setText('Player info')

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
