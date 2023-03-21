import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QFileDialog
import getTextByWord
import getTextByPdf
import getTextByTxt
import design
import os
import shutil
import tts


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #self.pushButton.clicked.connect(self.printButtonPressed)
        self.comboBox.currentTextChanged.connect(self.cboxValChanged)
        self.loadFileBtnDocs.clicked.connect(self.getTextFromFile)
        self.ClearBtnDocs.clicked.connect(self.cleanText)
        self.playAudioBtnDocs.clicked.connect(self.playAudio)
        self.stopAudioBtnDocs.clicked.connect(self.stopAudio)
        self.saveAudioBtnDocs.clicked.connect(self.saveAudio)
        self.plainTextEdit.textChanged.connect(self.textAreaChanged)

        self.loadingTimer = QTimer()
        self.loadingTimer.setInterval(10)
        self.loadingTimer.timeout.connect(self.dialSpin)
        self.loadingTimer.start()

        self.dialCw = True
        self.dial.setEnabled(False)

        self.isAudioLoaded = False

    def dialSpin(self):

        if (self.dialCw):
            if (self.dial.value() != 99):
                self.dial.setValue(self.dial.value() + 1)
            else:
                self.dialCw = False
        else:
            if (self.dial.value() != 1):
                self.dial.setValue(self.dial.value() - 1)
            else:
                self.dialCw = True



    def textAreaChanged(self):
        self.isAudioLoaded = False
        tts.stop()
        tts.flushTemps()

    def getTextFromFile(self):
        self.cleanText()
        try:
            fileLocation = QFileDialog.getOpenFileName(self, "Открыть файл", filter="Text files (*.docx *.pdf *.txt)")
            file_name, file_extension = os.path.splitext(fileLocation[0])
            if (file_extension == ".docx"):
                self.plainTextEdit.setPlainText(getTextByWord.getText(fileLocation[0]))

            elif (file_extension == ".txt"):
                self.plainTextEdit.setPlainText(getTextByTxt.getTextFromTxt(fileLocation[0]))

            elif (file_extension == ".pdf"):
                self.plainTextEdit.setPlainText(getTextByPdf.getTextFromPdf(fileLocation[0]))
        except:
            pass


    def cleanText(self):
        self.plainTextEdit.clear()
        tts.stop()
        tts.flushTemps()
        self.isAudioLoaded = False


    def resizeEvent(self, event):
        self.page.resize(self.size().width() - 22, self.plainTextEdit.size().height())
        QtWidgets.QMainWindow.resizeEvent(self, event)

    def closeEvent(self, event):
        tts.stop()
        tts.flushTemps()



    def cboxValChanged(self):
        alert = QtWidgets.QMessageBox()
        alert.setText(self.comboBox.currentText())
        alert.exec_()

    def playAudio(self):
        if (self.isAudioLoaded == False):
            tts.stop()
            if (self.plainTextEdit.toPlainText() != ""):
                self.worker = self.WavGenerationThread(self.plainTextEdit.toPlainText())
                self.worker.start()
                self.stackedWidget.setCurrentIndex(2)
                self.worker.finished.connect(self.threadFinishedEvent)
            else:
                pass
        else:
            tts.unpause()




    def stopAudio(self):
        if (self.isAudioLoaded == True):
            tts.pause()
        else:
            tts.stop()



    class WavGenerationThread(QThread):
        def __init__(self, text):
            super().__init__()
            self.text = text
        def run(self):

            tts.generateAudioFile(self.text)

    def threadFinishedEvent(self):
        self.stackedWidget.setCurrentIndex(0)
        tts.play()
        self.isAudioLoaded = True

    def saveAudio(self):
        try:
            if os.path.exists("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin())):
                self.stopAudio()
                file = str(QFileDialog.getExistingDirectory(self, "Сохранить в"))
                shutil.copy("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin()), file)
                alert = QtWidgets.QMessageBox()
                alert.setWindowTitle("Успешно")
                alert.setText("Файл data.wav сохранен в {0}".format(file))
                alert.exec_()
            else:
                alert = QtWidgets.QMessageBox()
                alert.setWindowTitle("Ошибка")
                alert.setText("Сгенерированные файлы не найдены")
                alert.exec_()
        except:
            pass










    """def printButtonPressed(self):
        alert = QtWidgets.QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()"""




app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec_()