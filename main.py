# libs
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication
import youtube_dl, json

# module
from src.pyqt.app_ui import Ui_MainWindow

def main():

  class MainWindow(QMainWindow):
    
    main_ui: Ui_MainWindow

    def __init__(self) -> None:
      super().__init__()
      self.main_ui = Ui_MainWindow()
      self.main_ui.setupUi(self)

      # TODO декомпозировать нвешивание хендлеров
      self.main_ui.configBtn_4.clicked.connect(self.on_click_download)
      self.main_ui.configBtn_2.clicked.connect(self.on_click_info)
      self.main_ui.configBtn_3.clicked.connect(self.on_click_save)

    # TODO вынести хендлеры в отдельный класс
    # collbacl-handlers-action
    def on_click_info(self, *args) -> None:
      video_url = self.main_ui.videoUrl.text()

      if video_url:
        # TODO для ytdl придумать враппер-логику
        with youtube_dl.YoutubeDL() as ytdl:
          info = ytdl.extract_info(video_url, download=False)

          self.main_ui.lineEdit_2.setText(info.get('title'))
          self.main_ui.lineEdit_4.setText(str(info.get('duration')))
          self.main_ui.lineEdit_3.setText(info.get('channel'))

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

 