from funcs import download_audio, download_video
from PyQt5 import QtWidgets 


def start_button_click(self):
    if len(self.video_link.text()) > 5:
        if self.File_path != None:
            link = self.video_link.text()
            path = self.File_path.text()
            if self.radioButton_video.isChecked():
                download_video(link, path)
            else:
                download_audio(link, path)
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Вы не выбрали папку для сохранения!")
    else:
        QtWidgets.QMessageBox.warning(self, "Ошибка!", "Укажите ссылку на видео!")

def button_directorie_click(self):
    directorie_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Choose directorie: ', 'C:\Users\User\Desktop')
    self.File_path.text(directorie_path)