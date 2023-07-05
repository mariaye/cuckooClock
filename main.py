import os.path
import sys
from datetime import datetime

from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtGui import QCursor, QDesktopServices
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow

from need.cuckooClock import Ui_MainWindow
from need.notes import Ui_NoteWindow
from need.setting import Ui_SettingWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.halfHour = True
        self.theHour = True
        self.volume = 100
        self.media_player = QMediaPlayer()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.update_text()
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.save_note)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.enterEvent = self.setting_enter_event
        self.pushButton_4.leaveEvent = self.setting_leave_event
        # connect labels
        # self.label = self.findChild(QLabel, "label")
        # self.label_2 = self.findChild(QLabel, "label_2")

        # set the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.label_time)
        self.timer.timeout.connect(self.label_date)
        self.timer.timeout.connect(self.play_cuckoo)
        self.timer.start(1000)

        self.label_time()
        self.label_date()

    def label_time(self):
        time = datetime.now()
        formatted_time = time.strftime("%H:%M:%S")

        self.label_2.setText(formatted_time)

    def label_date(self):
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        time = datetime.now()
        formatted_date = time.strftime("%Y/%m/%d ") + weekdays[time.weekday()]

        self.label.setText(formatted_date)

    def save_note(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "note.txt")
        with open(file_path, 'w') as file:
            file.write(self.textEdit.toPlainText())

    def update_text(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "note.txt")
        with open(file_path, 'r') as file:
            self.textEdit.setText(file.read())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isMaximized() is False:
            self.m_flag = True
            self.m_Postition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Postition)
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def setting_enter_event(self, event):
        self.pushButton_4.setText("  Setting      ")

    def setting_leave_event(self, event):
        self.pushButton_4.setText("Cuckoo Clock")

    def init_clock(self):
        setting_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setting.txt")
        with open(setting_path, "r") as file:
            halfHour, theHour, volume = file.read().strip().split("\t")
            self.halfHour = bool(int(halfHour))
            self.theHour = bool(int(theHour))
            self.volume = int(volume)
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sound/cuckooSound.mp3")
        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setVolume(self.volume)
        self.media_player.setMedia(media_content)

    def play_cuckoo(self):
        time = datetime.now().time()
        # print(time.minute, time.second)
        if self.theHour and time.minute == 0 and time.second == 0:
            self.media_player.play()
        if self.halfHour and time.minute == 30 and time.second == 0:
            self.media_player.play()

        # if time.second == 0:
        #     self.media_player.play()


class NoteWindow(QMainWindow, Ui_NoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def Open(self):
        self.show()

    def update_text(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "note.txt")
        with open(file_path, 'r') as file:
            self.textEdit.setText(file.read())

    def save_note(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "note.txt")
        with open(file_path, 'w') as file:
            file.write(self.textEdit.toPlainText())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isMaximized() is False:
            self.m_flag = True
            self.m_Postition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Postition)
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class SettingWindow(QMainWindow, Ui_SettingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label_3.linkActivated.connect(self.open_link)
        self.pushButton.clicked.connect(self.close)
        self.verticalSlider.valueChanged.connect(self.update_volume)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def Open(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setting.txt")
        if os.path.exists("setting.txt"):
            with open(file_path, 'r') as file:
                halfHour, theHour, volume = file.read().strip().split("\t")
                # print(halfHour, theHour, volume)
                self.checkBox.setChecked(bool(int(halfHour)))
                self.checkBox_2.setChecked(bool(int(theHour)))
                self.verticalSlider.setValue(int(volume))
        else:
            setting = "1" + "\t" + "1" + "\t" + "100"
            with open(file_path, 'w') as file:
                file.write(setting)
                self.checkBox.setChecked(True)
                self.checkBox_2.setChecked(True)
                self.verticalSlider.setValue(100)
        self.show()

    def update_volume(self, value):
        self.label_4.setText(f'{value}%')

    def close_save(self):
        setting = str(int(self.checkBox.isChecked())) + "\t" \
                  + str(int(self.checkBox_2.isChecked())) + "\t" \
                  + str(self.verticalSlider.value())
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setting.txt")
        with open(file_path, 'w') as file:
            file.write(setting)
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isMaximized() is False:
            self.m_flag = True
            self.m_Postition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Postition)
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    settingWindow = SettingWindow()

    window = MainWindow()
    window.show()
    window.init_clock()

    noteWindow = NoteWindow()

    window.pushButton_2.clicked.connect(window.close)
    window.pushButton_2.clicked.connect(window.save_note)
    window.pushButton_2.clicked.connect(noteWindow.Open)
    window.pushButton_2.clicked.connect(noteWindow.update_text)

    noteWindow.pushButton.clicked.connect(noteWindow.close)
    noteWindow.pushButton.clicked.connect(noteWindow.save_note)
    noteWindow.pushButton.clicked.connect(window.show)
    noteWindow.pushButton.clicked.connect(window.update_text)

    window.pushButton_4.clicked.connect(settingWindow.Open)

    settingWindow.pushButton_2.clicked.connect(settingWindow.close_save)
    settingWindow.pushButton_2.clicked.connect(window.init_clock)

    window.save_note()
    sys.exit(app.exec_())
