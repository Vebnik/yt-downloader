# libs
import pprint as pp, os, threading
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QErrorMessage

# module
from src.pyqt.ui.app_ui_new import Ui_MainWindow
from src.ytdl.Ytdl import Ytdl
from src.models.ytdl import Video


# main app
class MainWindow(QMainWindow):
  
  main_ui: Ui_MainWindow

  def __init__(self) -> None:
    super().__init__()

    # init ui
    self.main_ui = Ui_MainWindow()
    self.main_ui.setupUi(self)

    # add connect and callback
    CreateConnect.link_callback(self)


# logic Handlers
class Handlers:

  app_instance: MainWindow
  video: Video = None

  @staticmethod
  def on_click_info(*args) -> None:
    video_url = Handlers.app_instance.main_ui.videoUrl.text()

    if not video_url:
      Utils.error('Not valid video'); return

    with Ytdl(hooks=Handlers.on_progress) as ytdl:
      Handlers.video = ytdl.get_info(video_url)

      Handlers.app_instance.main_ui.lineEdit_4.setText(f'{round(Handlers.video.duration/60, 2)} min')
      Handlers.app_instance.main_ui.lineEdit_2.setText(Handlers.video.title)
      Handlers.app_instance.main_ui.lineEdit_3.setText(Handlers.video.channel)

      for format in Handlers.video.formats:
        Handlers.app_instance.main_ui.comboBox.addItem([*format.keys()][0], [*format.values()][0])

  @staticmethod
  def on_click_download(*args) -> None:
    if not Handlers.video:
      Utils.error('Not valid video'); return

    video_url = Handlers.app_instance.main_ui.videoUrl.text()
    current_url = Handlers.app_instance.main_ui.comboBox.currentData()
    save_path = QFileDialog.getExistingDirectory(parent=Handlers.app_instance)

    with Ytdl(hooks=Handlers.on_progress) as ytdl:
      thread = threading.Thread(target=ytdl.download, args=([video_url],))
      thread.start()

  @staticmethod
  def on_progress(progress_data: dict) -> None:
    try:
      value = float(progress_data.get('_percent_str').replace('%', ''))
      Handlers.app_instance.main_ui.progressBar.setValue(round(value))
    except Exception as ex:
      print(ex)


# logic connect
class CreateConnect:
  @staticmethod
  def link_callback(self: MainWindow) -> None:
    Handlers.app_instance = self
    
    self.main_ui.configBtn_4.clicked.connect(Handlers.on_click_download)
    self.main_ui.configBtn_2.clicked.connect(Handlers.on_click_info)


class Utils:
  @staticmethod
  def error(msg: str) -> None:
    QErrorMessage(Handlers.app_instance).showMessage(msg)