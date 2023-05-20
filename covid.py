from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import pickle
from skimage.feature import hog
import cv2
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 151, 71))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pix = QtWidgets.QLabel(self.centralwidget)
        self.pix.setGeometry(QtCore.QRect(230, 120, 271, 251))
        self.pix.setText("")
        self.pix.setObjectName("pix")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 410, 171, 51))
        self.pushButton.setStyleSheet("color: rgb(0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 500, 171, 51))
        self.pushButton_2.setStyleSheet("color: rgb(0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 30, 151, 71))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.dt = QtWidgets.QLabel(self.centralwidget)
        self.dt.setGeometry(QtCore.QRect(710, 150, 181, 51))
        self.dt.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.dt.setObjectName("dt")
        self.knn = QtWidgets.QLabel(self.centralwidget)
        self.knn.setGeometry(QtCore.QRect(740, 280, 121, 51))
        self.knn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.knn.setObjectName("knn")
        self.svm = QtWidgets.QLabel(self.centralwidget)
        self.svm.setGeometry(QtCore.QRect(740, 450, 121, 51))
        self.svm.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.svm.setObjectName("svm")
        self.dt_2 = QtWidgets.QLabel(self.centralwidget)
        self.dt_2.setGeometry(QtCore.QRect(910, 150, 161, 41))
        self.dt_2.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.dt_2.setText("")
        self.dt_2.setObjectName("dt_2")
        self.knn_2 = QtWidgets.QLabel(self.centralwidget)
        self.knn_2.setGeometry(QtCore.QRect(910, 280, 161, 41))
        self.knn_2.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.knn_2.setText("")
        self.knn_2.setObjectName("knn_2")
        self.svm_2 = QtWidgets.QLabel(self.centralwidget)
        self.svm_2.setGeometry(QtCore.QRect(920, 450, 161, 41))
        self.svm_2.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.svm_2.setText("")
        self.svm_2.setObjectName("svm_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 230, 221, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 380, 221, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(870, 530, 221, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        # self.pix.hide()
        self.pushButton.clicked.connect(self.covid)
        self.pushButton_2.clicked.connect(self.result)
    def covid(self):
        fname = QFileDialog.getOpenFileName(None, 'Open File', 'c\\' 'Image files ')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.pix.setPixmap(QPixmap(pixmap))
        print(fname[0])
        img = cv2.imread(fname[0])   
        # fileName='COVID-1.png'
        # print(fileName)
        # self.pix.show()
        
        # img = cv2.imread(fileName)
        print(img)
        img = cv2.resize(img,(256,128))
        fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), 
                        cells_per_block=(2, 2), visualize=True, multichannel=True)
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pickled_model_svm = pickle.load(open('finalized_dt.pkl', 'rb'))
        predicted_KNN = pickled_model_svm.predict([fd])
        print(predicted_KNN)
        
        if predicted_KNN==0:
                self.dt_2.setText("Normal")
                self.dt_2.hide()
                
                
        else:
                 self.dt_2.setText("COVID")
                 self.dt_2.hide()
        
    def result(self,predicted_KNN):    
        self.dt_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "View Result"))
        self.label_2.setText(_translate("MainWindow", "Results"))
        self.dt.setText(_translate("MainWindow", "Decision Tress:"))
        self.knn.setText(_translate("MainWindow", "KNN:"))
        self.svm.setText(_translate("MainWindow", "SVM:"))
        self.label_3.setText(_translate("MainWindow", "Accuracy is : 85%"))
        self.label_4.setText(_translate("MainWindow", "Accuracy is : 95%"))
        self.label_5.setText(_translate("MainWindow", "Accuracy is : 90%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
