from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import pickle
from skimage.feature import hog
import cv2
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Setting Up main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 600)

        # Setting Up icon for the main window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        # Adding a central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Adding a Upload Button
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(10, 490, 351, 61))
        self.uploadButton.setObjectName("uploadButton")

        # Connecting the button to openFile function
        self.uploadButton.clicked.connect(self.openFile)

        # Configuring vertical and horizontal dividers
        self.verticalDivider = QtWidgets.QFrame(self.centralwidget)
        self.verticalDivider.setGeometry(QtCore.QRect(360, 0, 31, 571))
        self.verticalDivider.setLineWidth(2)
        self.verticalDivider.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalDivider.setObjectName("verticalDivider")
        self.horizontalDivider = QtWidgets.QFrame(self.centralwidget)
        self.horizontalDivider.setGeometry(QtCore.QRect(-3, 470, 371, 20))
        self.horizontalDivider.setLineWidth(2)
        self.horizontalDivider.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalDivider.setObjectName("horizontalDivider")

        # Setting up text area, so results from ML model will display here
        self.textArea = QtWidgets.QTextEdit(self.centralwidget)
        self.textArea.setGeometry(QtCore.QRect(390, 30, 321, 521))
        self.textArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textArea.setObjectName("textArea")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(120, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily(".Hiragino Sans GB Interface")
        font.setPointSize(17)
        font.setItalic(True)
        font.setWeight(50)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.RecogTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.RecogTextLabel.setGeometry(QtCore.QRect(490, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RecogTextLabel.setFont(font)
        self.RecogTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RecogTextLabel.setObjectName("RecogTextLabel")
        self.imageArea = QtWidgets.QLabel(self.centralwidget)
        self.imageArea.setGeometry(QtCore.QRect(10, 40, 351, 421))
        self.imageArea.setSizeIncrement(QtCore.QSize(0, 0))
        self.imageArea.setText("Your Image Will Display here")
        self.imageArea.setPixmap(QtGui.QPixmap(""))
        self.imageArea.setScaledContents(True)
        self.imageArea.setAlignment(QtCore.Qt.AlignCenter)
        self.imageArea.setWordWrap(False)
        self.imageArea.setIndent(-3)
        self.imageArea.setObjectName("imageArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid Detection"))
        self.uploadButton.setText(_translate("MainWindow", "Select Image to Check"))
        self.ImageLabel.setText(_translate("MainWindow", "Image"))
        self.RecogTextLabel.setText(_translate("MainWindow", "Result"))

    def openFile(self):
        fname = QFileDialog.getOpenFileName(None, 'Open File', 'c\\' 'Image files ')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.imageArea.setPixmap(QPixmap(pixmap))
        print(fname[0])
    
        img = cv2.imread(fname[0],0)
        img = cv2.resize(img,(256,128))
        fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), 
                        cells_per_block=(2, 2), visualize=True, multichannel=True)
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        
        
        print(fd.shape)
      
        np_img = np.array(grayscale)
        # classes = model.predict_classes(img)
        pickled_model_svm = pickle.load(open('finalized_dt.pkl', 'rb'))
        
        predicted_KNN = pickled_model_svm.predict([fd])
        print(predicted_KNN)
        
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
