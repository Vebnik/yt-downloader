# libs
from PyQt6.QtWidgets import QMainWindow, QApplication

# module
from src.pyqt.app import MainWindow


def main():
    
  app = QApplication([])
  main_window = MainWindow()

  main_window.show()
  app.exec()

if __name__ == '__main__':
  main()

 