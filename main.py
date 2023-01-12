import requests
from PyQt5 import QtCore, QtGui, QtWidgets


import Download
import updates


fresh = False
Inet = False
timeout = 1

try:
    requests.head("http://www.google.com/", timeout=timeout)
    # Do something
    print('The internet connection is active')
    Inet = True
except requests.ConnectionError:
    # Do something
    print("The internet connection is down")
    Inet = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(53, 132, 228);")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Pl = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Pl.setGeometry(QtCore.QRect(620, 520, 161, 51))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai HK")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Button_Pl.setFont(font)
        self.Button_Pl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Button_Pl.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "  border: 2px solid;\n"
                                     "  border-radius: 1px;\n"
                                     "  transition: 0.2s;")
        self.Button_Pl.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Button_Pl.setShortcut("")
        self.Button_Pl.setCheckable(False)
        self.Button_Pl.setAutoDefault(False)
        self.Button_Pl.setObjectName("Button_Pl")
        self.Whatsnew = QtWidgets.QLabel(self.centralwidget)
        self.Whatsnew.setGeometry(QtCore.QRect(0, 310, 331, 41))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        font.setItalic(True)
        self.Whatsnew.setFont(font)
        self.Whatsnew.setStyleSheet("color: rgb(255, 255, 255)")
        self.Whatsnew.setObjectName("Whatsnew")
        self.News1 = QtWidgets.QLabel(self.centralwidget)
        self.News1.setGeometry(QtCore.QRect(10, 410, 321, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        font.setItalic(True)
        self.News1.setFont(font)
        self.News1.setStyleSheet("color: rgb(255, 255, 255)")
        self.News1.setObjectName("News1")
        self.News2 = QtWidgets.QLabel(self.centralwidget)
        self.News2.setGeometry(QtCore.QRect(10, 450, 321, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        font.setItalic(True)
        self.News2.setFont(font)
        self.News2.setStyleSheet("color: rgb(255, 255, 255)")
        self.News2.setObjectName("News2")
        self.News3 = QtWidgets.QLabel(self.centralwidget)
        self.News3.setGeometry(QtCore.QRect(10, 370, 311, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        font.setItalic(True)
        self.News3.setFont(font)
        self.News3.setStyleSheet("color: rgb(255, 255, 255)")
        self.News3.setObjectName("News3")
        self.ogr = QtWidgets.QLabel(self.centralwidget)
        self.ogr.setGeometry(QtCore.QRect(710, 240, 91, 51))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(30)
        font.setItalic(True)
        self.ogr.setFont(font)
        self.ogr.setStyleSheet("color: rgb(255, 255, 255);")
        self.ogr.setTextFormat(QtCore.Qt.AutoText)
        self.ogr.setObjectName("ogr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 741, 71))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(40)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.Button_download = QtWidgets.QPushButton(self.centralwidget)
        self.Button_download.setGeometry(QtCore.QRect(460, 520, 161, 51))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai HK")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Button_download.setFont(font)
        self.Button_download.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Button_download.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "  border: 2px solid;\n"
                                           "  border-radius: 1px;\n"
                                           "  transition: 0.2s;")
        self.Button_download.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Button_download.setShortcut("")
        self.Button_download.setCheckable(False)
        self.Button_download.setAutoDefault(False)
        self.Button_download.setObjectName("Button_download")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 520, 431, 51))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лаунчер"))
        self.Button_Pl.setText(_translate("MainWindow", "Играть"))
        self.Whatsnew.setText(_translate("MainWindow", "Что нового :"))
        self.News1.setText(_translate("MainWindow", "2 - "))
        self.News2.setText(_translate("MainWindow", "3 -"))
        self.News3.setText(_translate("MainWindow", "1 - "))
        self.ogr.setText(_translate("MainWindow", "18+"))
        self.label.setText(_translate("MainWindow", "Игра судьбы"))
        self.Button_download.setText(_translate("MainWindow", "Скачать"))
        self.label_2.setText(_translate("MainWindow", "Последняя версия"))

    def add_func(self):
       #  self.Button_Pl.clicked.connect(lambda:  self.metod())

        self.Button_Pl.setStyleSheet\
                (
                "QPushButton::hover"
                "{"
                "background-color : lightgreen;"
                "}"
                 )

        self.Button_download.setStyleSheet \
            (
            "QPushButton::hover"
            "{"
            "background-color : lightgreen;"
            "}"
             )


        if Inet:
            fresh = updates.find_update()
            if fresh:
                self.Button_download.setVisible(not fresh)
                self.Button_Pl.setVisible(True)
                self.label_2.setText("Последняя версия")
            else:
                self.Button_download.setVisible(not fresh)
                self.Button_Pl.setVisible(False)
                self.label_2.setText("Требуется обновить")


        else:
            self.Button_download.setVisible(False)
            self.Button_Pl.setVisible(True)

            self.label_2.setText("Нет интернета")


        self.Button_download.clicked.connect(self.download)



    def download(self):
        self.Button_download.setVisible(False)
        self.Button_Pl.setVisible(False)

        self.label_2.setText("Загрузка файла...")
        self.downloader = Download.Downloader()
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()
        #new = QMessageBox()
        #new.setText("Загрузка завершена ...")
        #new.exec_()

    def downloadFinished(self):
        self.label_2.setText("Последняя версия")
        self.Button_Pl.setVisible(True)
        # Удаление потока после его использования.
        del self.downloader

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


