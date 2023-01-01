# libs
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt6 import uic

# module
from src.pyqt.app_ui import Ui_MainWindow

def main():

  class MainWindow(QMainWindow):
    
    main_ui: Ui_MainWindow

    def __init__(self) -> None:
      super().__init__()
      self.main_ui = Ui_MainWindow()
      self.main_ui.setupUi(self)

      self.main_ui.configBtn_4.clicked.connect(self.on_click_download)
      self.main_ui.configBtn_2.clicked.connect(self.on_click_info)
      self.main_ui.configBtn_3.clicked.connect(self.on_click_save)

    # collbacl-handlers-action
    def on_click_info(self, *args) -> None:
      print('click on_click_info', args)

    def on_click_download(self, *args) -> None:
      print('click on_click_download', args)

    def on_click_save(self, *args) -> None:
      print('click on_click_save', args)

    
  app = QApplication([])
  main_window = MainWindow()

  main_window.show()
  app.exec()

if __name__ == '__main__':
  main()

 