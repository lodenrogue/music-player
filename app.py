from PyQt5.QtWidgets import QApplication
from components.main_window_view import MainWindowView
import sys

app = QApplication([])
window = MainWindowView()
window.showMaximized()
window.show()
sys.exit(app.exec_())
