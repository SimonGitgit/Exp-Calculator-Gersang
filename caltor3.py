from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import math
import os
import base64
import sys
import DataFile 
import ExpTable


def write_file(data, route):
    get_file = base64.b64decode(data)		# 将base64数据进行解析

    with open(route, 'wb') as f_Obj:		# 输出文件到指定位置
        f_Obj.write(get_file)

def get_exp_diff(before, after):
    return (ExpTable.expCheck[0][str(after)] - ExpTable.expCheck[0][str(before)])

class Ui_MainWindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(670, 530)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")

        #author's name
        self.textEdit_0 = QtWidgets.QLabel(self.centralwidget)
        self.textEdit_0.setGeometry(QtCore.QRect(550, 10, 70, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit_0.setFont(font)
        self.textEdit_0.setObjectName("textEdit_0")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(102, 320, 71, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(102, 350, 71, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(102, 380, 71, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(102, 410, 71, 31))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 320, 60, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(170, 410, 48, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(5)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 350, 60, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(170, 380, 60, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(232, 320, 71, 31))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(232, 350, 71, 31))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(232, 410, 71, 31))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(232, 380, 71, 31))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(300, 320, 84, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(300, 350, 84, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(300, 380, 84, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(300, 410, 84, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")


        

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 380, 71, 35))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 410, 71, 35))
        self.label_9.setObjectName("label_9")
        
        #pushbutton
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 86, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setIconSize(QtCore.QSize(16, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 350, 86, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(385, 320, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_1.setGeometry(QtCore.QRect(385, 380, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setMouseTracking(True)
        self.pushButton_3_1.setAutoFillBackground(False)
        self.pushButton_3_1.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_3_1.setCheckable(True)
        self.pushButton_3_1.setChecked(False)
        self.pushButton_3_1.setObjectName("pushButton_3_1")


        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 410, 86, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 440, 86, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(425, 320, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 470, 86, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setMouseTracking(True)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setObjectName("pushButton_7")
        
        
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 30, 801, 481))
        self.label_11.setText("")
        
        #set background
        write_file(DataFile.picture, "./backgroundimage.png")
        self.label_11.setPixmap(QtGui.QPixmap("./backgroundimage.png"))

        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(472, 320, 71, 31))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(472, 350, 71, 31))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(472, 380, 71, 31))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_14.setLineWidth(0)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(472, 410, 71, 31))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("background-color:  rgba(255, 255, 255,150);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.textEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(540, 320, 104, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy)
        self.textEdit_8.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(540, 350, 104, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(540, 380, 104, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(540, 410, 104, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setReadOnly(True)
        self.textEdit_11.setObjectName("textEdit_11")

        #text init
        self.textEdit.setText("210000")
        self.textEdit_2.setText("10")
        self.textEdit_3.setText("100")

        self.textEdit_8.setText("1")
        self.textEdit_9.setText("250")
        self.textEdit_10.setText("15")
        
        self.label_11.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.spinBox.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_3_1.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.textEdit_7.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.textEdit_8.raise_()
        self.textEdit_9.raise_()
        self.textEdit_10.raise_()
        self.textEdit_11.raise_()
        Mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Mainwindow.setStatusBar(self.statusbar)
        # set on clicked event
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton_2.clicked.connect(self.clicked)
        self.pushButton_3.clicked.connect(self.clicked)
        self.pushButton_3_1.clicked.connect(self.clicked)
        self.pushButton_4.clicked.connect(self.clicked)
        self.pushButton_5.clicked.connect(self.clicked)
        self.pushButton_7.clicked.connect(self.clicked)
        self.main_kill_counter = 0
        self.pushButton_6.clicked.connect(self.hit_pressed)
        # set integer protection
        self.textEdit.setValidator(QIntValidator())
        self.textEdit_2.setValidator(QIntValidator())
        self.textEdit_3.setValidator(QIntValidator())
        self.textEdit_4.setValidator(QIntValidator())
        self.textEdit_5.setValidator(QIntValidator())
        self.textEdit_6.setValidator(QIntValidator())
        self.textEdit_7.setValidator(QIntValidator())
        self.textEdit_8.setValidator(QIntValidator())
        self.textEdit_9.setValidator(QIntValidator())
        self.textEdit_10.setValidator(QIntValidator())

        # set style sheet
        self.pushButton.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: #d98a5f;"
            "border: 0px solid #743c1e;"
            "}"  
                                    )
        self.pushButton_2.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(108,202,225);"
            "border: 0px solid rgb(108,202,225);"
            "}"  
                                    )
        self.pushButton_3.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(176,206,194);"
            "border: 0px solid rgb(176,206,194);"
            "}"  
                                    )
        self.pushButton_3_1.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(176,206,194);"
            "border: 0px solid rgb(176,206,194);"
            "}"  
                                    )

        self.pushButton_4.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(164,156,132);"
            "border: 0px solid rgb(164,156,132);"
            "}"  
                                    )
        self.pushButton_5.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(252,229,168);"
            "border: 0px solid rgb(252,229,168);"
            "}"  
                                    )
        self.pushButton_7.setStyleSheet(
            "QPushButton::checked"
            "{"
            "background-color: rgb(87,87,142);"
            "border: 0px solid rgb(87,87,142);"
            "}"  
                                    )

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "巨商經驗值計算機"))
        self.label.setText(_translate("Mainwindow", "怪物經驗"))
        self.label_2.setText(_translate("Mainwindow", "怪物總數"))
        self.label_3.setText(_translate("Mainwindow", "倍經活動"))
        self.label_4.setText(_translate("Mainwindow", "商團技能"))
        self.pushButton_6.setText(_translate("Mainwindow", "打手"))
        self.label_5.setText(_translate("Mainwindow", "主角經驗"))
        self.label_6.setText(_translate("Mainwindow", "兵將經驗"))
        self.label_7.setText(_translate("Mainwindow", "總經檢查"))
        self.label_8.setText(_translate("Mainwindow", "%"))
        self.label_9.setText(_translate("Mainwindow", "%"))
        self.pushButton.setText(_translate("Mainwindow", "七福御膳"))
        self.pushButton_4.setText(_translate("Mainwindow", "據點佔領"))
        self.pushButton_2.setText(_translate("Mainwindow", "日積月累"))
        self.pushButton_3.setText(_translate("Mainwindow", "變身"))
        self.pushButton_3_1.setText(_translate("Mainwindow", "壇鏡"))
        self.pushButton_5.setText(_translate("Mainwindow", "商團宴會"))
        self.pushButton_7.setText(_translate("Mainwindow", "翅膀裝飾"))
        self.label_10.setText(_translate("Mainwindow", "壇鏡兵將"))
        self.label_12.setText(_translate("Mainwindow", "現在等級"))
        self.label_13.setText(_translate("Mainwindow", "目標等級"))
        self.label_14.setText(_translate("Mainwindow", "一場需時"))
        self.label_15.setText(_translate("Mainwindow", "完成時間"))
        self.textEdit_0.setText(_translate("Mainwindow", "大肥豬 @2022"))
        

    def clicked(self):
        self.update()

    #update calculation
    def update(self):
        self.exp_obj = Experience(int((self.textEdit.text())), #exp_each
                                int((self.textEdit_2.text())), #no_of_monster
                                self.pushButton.isChecked(), #七福御膳
                                self.pushButton_2.isChecked(), #日積月累
                                self.pushButton_3.isChecked(), #變身
                                self.pushButton_3_1.isChecked(),#壇鏡
                                self.pushButton_4.isChecked(), #據點佔領
                                self.pushButton_5.isChecked(), #商團宴會 
                                self.main_kill_counter, #主角打手
                                self.pushButton_7.isChecked(), #翅膀裝飾
                                int((self.textEdit_3.text())), #倍經
                                int(self.spinBox.value()) #商團技能
                                )    
        self.exp_obj.basicExp()
        
        self.textEdit_4.setText(str(self.exp_obj.composition()[0]))
        self.textEdit_5.setText(str(self.exp_obj.composition()[1]))
        self.textEdit_6.setText(str(self.exp_obj.composition()[2]))
        self.textEdit_7.setText(str(self.exp_obj.composition()[3]))
        exp_required = int(get_exp_diff(self.textEdit_8.text(),self.textEdit_9.text()))
        
        self.textEdit_11.setText("") # clear previous output string
        self.textEdit_11.append("主角"+str(math.ceil(exp_required * int(self.textEdit_10.text()) / int(self.exp_obj.composition()[0]) /3600))+"hr")
        self.textEdit_11.append("無鏡"+str(math.ceil(exp_required * int(self.textEdit_10.text()) / int(self.exp_obj.composition()[1]) /3600))+"hr")
        self.textEdit_11.append("有鏡"+str(math.ceil(exp_required * int(self.textEdit_10.text()) / int(self.exp_obj.composition()[2]) /3600))+"hr")

    #changed whom kill
    def hit_pressed(self):
        if (self.main_kill_counter == 0):
            self.main_kill_counter = 1
            self.pushButton_6.setText("打手")
            self.pushButton_6.setGeometry(425, 350, 40, 31)
        elif(self.main_kill_counter == 1):
            self.main_kill_counter = 2
            self.pushButton_6.setText("打手")
            self.pushButton_6.setGeometry(425, 380, 40, 31)
        elif(self.main_kill_counter == 2):
            self.main_kill_counter = 0
            self.pushButton_6.setText("打手")
            self.pushButton_6.setGeometry(425, 320, 40, 31)
        self.update()

#Experience calculation algorithm
class Experience:
    def __init__(self, exp_each, 
                        no_of_monster, 
                        seven, 
                        collect, 
                        changed,
                        mirror,
                        victory, 
                        banquet, 
                        mainkill, 
                        wing,
                        fest, 
                        team):
        self.basic_experience = 0
        self._number = no_of_monster
        self._experience = exp_each

        self._seven = seven
        self._collect = collect
        self._changed = changed
        self._mirror = mirror
        self._victory = victory
        self._wing = wing
        self._mainkill = int(mainkill)
        self._banquet = banquet
        self._skill = team #%
        self._server = fest # %

    def basicExp(self):
        if (self._seven):
            self.basic_experience = int(1.5 * self._number * self._experience)
        else:
            self.basic_experience = int(1 * self._number * self._experience)
    
    def composition(self):
        self.proportion_basic = math.floor(self.basic_experience/10) #基礎經驗
        self.proportion_collect =  math.floor(self.basic_experience/10) if (self._collect) else 0 #日積月累
        self.proportion_changed =  math.floor(self.basic_experience/10) if (self._changed) else 0 #變身
        self.proportion_mirror =  math.floor(self.basic_experience/10) if (self._mirror) else 0 #壇鏡
        self.proportion_victory =  math.floor(self.basic_experience/20) if (self._victory) else 0 #據點佔領
        self.proportion_wing =  math.floor(self.basic_experience/20) if (self._wing) else 0 #翅膀裝飾
        self.proportion_banquet =  math.floor(self.basic_experience * 0.35) if (self._banquet) else 0 #商團宴會
        self.proportion_skill = math.floor(self.basic_experience * self._skill / 100) #商團技能
        self.proportion_server = math.floor(self.basic_experience * self._server / 100) #活動倍經

        # print(self.proportion_basic) 
        # print(self.proportion_collect)
        # print(self.proportion_changed)
        # print(self.proportion_mirror)
        # print(self.proportion_victory)
        # print(self.proportion_wing )
        # print(self.proportion_banquet)
        # print(self.proportion_skill )
        # print(self.proportion_server)
        main_char_exp = self.proportion_basic + self.proportion_collect + self.proportion_changed + self.proportion_victory + self.proportion_wing + self.proportion_banquet + self.proportion_skill
        soldier_exp = self.proportion_basic + self.proportion_collect + self.proportion_banquet 
        soldier_mirror = self.proportion_basic + self.proportion_collect + self.proportion_mirror + self.proportion_banquet 
        

        if (self._mainkill == 0):
            main_char_exp += self.proportion_server
            check_sum = main_char_exp + 10 * (soldier_exp) + soldier_mirror 
        elif(self._mainkill == 1):
            soldier_exp += self.proportion_server
            check_sum = main_char_exp + 10 * (soldier_exp-self.proportion_server) + soldier_mirror + self.proportion_server
        elif(self._mainkill == 2):
            soldier_mirror +=self.proportion_server
            check_sum = main_char_exp + 10 * (soldier_exp) + soldier_mirror 
            
        
        return main_char_exp, soldier_exp, soldier_mirror, check_sum

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    os.remove("./backgroundimage.png")
    sys.exit(app.exec_())