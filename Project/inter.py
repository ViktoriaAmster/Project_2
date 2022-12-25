
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(343, 413)
        Form.setWindowTitle("")
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 411))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(68,56,72);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 311, 368))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(124, 113, 116);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.534, y1:0.483, x2:1, y2:0, stop:0 rgba(0, 93, 57, 255), stop:0.988636 rgba(20, 255, 216, 255))\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.video_link = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 56, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 130, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.video_link.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.video_link.setFont(font)
        self.video_link.setMouseTracking(True)
        self.video_link.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.video_link.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.video_link.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.video_link.setAutoFillBackground(False)
        self.video_link.setStyleSheet("QTextBrowser {\n"
"    font: 75 10pt \"Segoe Script\";\n"
"    color: rgb(0, 255, 130);\n"
"}")
        self.video_link.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.video_link.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.video_link.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.video_link.setUndoRedoEnabled(False)
        self.video_link.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.video_link.setReadOnly(False)
        self.video_link.setOverwriteMode(False)
        self.video_link.setAcceptRichText(False)
        self.video_link.setObjectName("video_link")
        self.verticalLayout.addWidget(self.video_link)
        self.radioButton_video = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton_video.setFont(font)
        self.radioButton_video.setStyleSheet("QRadioButton {\n"
"    color: rgb(0, 255, 130);\n"
"    font: 75 10pt \"Segoe Script\";\n"
"}")
        self.radioButton_video.setObjectName("radioButton_video")
        self.radioButton_video.setChecked(True)
        self.verticalLayout.addWidget(self.radioButton_video)
        self.radioButton_audio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_audio.setStyleSheet("QRadioButton {\n"
"    color: rgb(0, 255, 130);\n"
"    font: 75 10pt \"Segoe Script\";\n"
"}\n"
"\n"
"")
        self.radioButton_audio.setObjectName("radioButton_audio")
        self.verticalLayout.addWidget(self.radioButton_audio)
        self.Start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Start_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Start_button.setFont(font)
        self.Start_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Start_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Start_button.setAutoFillBackground(False)
        self.Start_button.setStyleSheet("QPushButton {\n"
"    color: rgb(0,255, 130);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.Start_button.setObjectName("Start_button")
        self.verticalLayout.addWidget(self.Start_button)
        self.File_path = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.File_path.setFont(font)
        self.File_path.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.File_path.setAcceptDrops(False)
        self.File_path.setStyleSheet("QTextBrowser {\n"
"    color: rgb(0, 255, 130);\n"
"    font: 75 10pt \"Segoe Script\";\n"
"}")
        self.File_path.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.File_path.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.File_path.setTabChangesFocus(True)
        self.File_path.setDocumentTitle("")
        self.File_path.setReadOnly(False)
        self.File_path.setAcceptRichText(False)
        self.File_path.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.File_path.setObjectName("File_path")
        self.verticalLayout.addWidget(self.File_path)
        self.Directorie_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Directorie_button.setFont(font)
        self.Directorie_button.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 255, 130);\n"
"    border-radius: 10px;\n"
"    background-color:rgb(0, 0, 0);\n"
"}")
        self.Directorie_button.setObjectName("Directorie_button")
        self.verticalLayout.addWidget(self.Directorie_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.video_link.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe Script\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#00ff82;\">Video link</span></p></body></html>"))
        self.radioButton_video.setText(_translate("Form", "Download video"))
        self.radioButton_audio.setText(_translate("Form", "Download audio"))
        self.Start_button.setText(_translate("Form", "Start!!!"))
        self.File_path.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe Script\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#00ff82;\">File path</span></p></body></html>"))
        self.Directorie_button.setText(_translate("Form", "Choose directorie"))
