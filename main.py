import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
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
        tts.stop()
        if (self.plainTextEdit.toPlainText() != ""):
            self.worker = self.WavGenerationThread(self.plainTextEdit.toPlainText())
            self.worker.start()
            self.stackedWidget.setCurrentIndex(1)
            self.worker.finished.connect(self.threadFinishedEvent)



    def stopAudio(self):
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

    def saveAudio(self):
        if os.path.exists("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin())):
            file = str(QFileDialog.getExistingDirectory(self, "Сохранить в"))
            shutil.copy("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin()), file)
        else:
            alert = QtWidgets.QMessageBox()
            alert.setText("Сгенерированные файлы не найдены")
            alert.exec_()









    """def printButtonPressed(self):
        alert = QtWidgets.QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()"""




app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec_()
