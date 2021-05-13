from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QListWidget

from components.options.options_controller import OptionsController


class OptionsView(QWidget):

    def __init__(self, event_emitter, player):
        QWidget.__init__(self)
        self.listWidget = self._create_list_widget()

        layout = QGridLayout()
        layout.addWidget(self.listWidget)
        self.setLayout(layout)

        self.controller = OptionsController(self, event_emitter, player)

    def initialize_options(self, playlists):
        for i, playlist in enumerate(playlists):
            self.listWidget.insertItem(i, playlist)

    def _select_playlist(self, _):
        item = self.listWidget.currentItem()
        self.controller.select_playlist(item.text())

    def _create_list_widget(self):
        listWidget = QListWidget()
        listWidget.setObjectName("options")
        listWidget.clicked.connect(self._select_playlist)
        return listWidget
