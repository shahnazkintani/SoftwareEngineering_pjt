# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setSizeGripEnabled(False)
        self.ButtonBox_Confirm = QtWidgets.QDialogButtonBox(Dialog)
        self.ButtonBox_Confirm.setGeometry(QtCore.QRect(300, 460, 481, 41))
        self.ButtonBox_Confirm.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox_Confirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ButtonBox_Confirm.setObjectName("ButtonBox_Confirm")
        self.PB_Load = QtWidgets.QPushButton(Dialog)
        self.PB_Load.setGeometry(QtCore.QRect(60, 40, 91, 31))
        self.PB_Load.setObjectName("PB_Load")
        self.PB_Info = QtWidgets.QPushButton(Dialog)
        self.PB_Info.setGeometry(QtCore.QRect(200, 40, 91, 31))
        self.PB_Info.setObjectName("PB_Info")
        self.PB_BLSetting = QtWidgets.QPushButton(Dialog)
        self.PB_BLSetting.setGeometry(QtCore.QRect(360, 40, 91, 31))
        self.PB_BLSetting.setObjectName("PB_BLSetting")
        self.PB_All = QtWidgets.QPushButton(Dialog)
        self.PB_All.setGeometry(QtCore.QRect(520, 40, 91, 31))
        self.PB_All.setObjectName("PB_All")
        self.PB_Quit = QtWidgets.QPushButton(Dialog)
        self.PB_Quit.setGeometry(QtCore.QRect(670, 40, 91, 31))
        self.PB_Quit.setObjectName("PB_Quit")
        self.CB_Marker = QtWidgets.QCheckBox(Dialog)
        self.CB_Marker.setGeometry(QtCore.QRect(580, 180, 151, 31))
        self.CB_Marker.setMinimumSize(QtCore.QSize(62, 0))
        self.CB_Marker.setObjectName("CB_Marker")
        self.CB_Line = QtWidgets.QCheckBox(Dialog)
        self.CB_Line.setGeometry(QtCore.QRect(580, 230, 151, 31))
        self.CB_Line.setMinimumSize(QtCore.QSize(62, 0))
        self.CB_Line.setObjectName("CB_Line")
        self.CB_HM = QtWidgets.QCheckBox(Dialog)
        self.CB_HM.setGeometry(QtCore.QRect(580, 280, 151, 31))
        self.CB_HM.setMinimumSize(QtCore.QSize(62, 0))
        self.CB_HM.setObjectName("CB_HM")
        self.CB_Another = QtWidgets.QCheckBox(Dialog)
        self.CB_Another.setGeometry(QtCore.QRect(580, 330, 151, 31))
        self.CB_Another.setMinimumSize(QtCore.QSize(61, 0))
        self.CB_Another.setObjectName("CB_Another")
        self.label_TrackID = QtWidgets.QLabel(Dialog)
        self.label_TrackID.setGeometry(QtCore.QRect(100, 110, 171, 31))
        self.label_TrackID.setObjectName("label_TrackID")
        self.ComboB_TID = QtWidgets.QComboBox(Dialog)
        self.ComboB_TID.setGeometry(QtCore.QRect(120, 150, 281, 41))
        self.ComboB_TID.setObjectName("ComboB_TID")
        self.ComboB_TID.addItem("")
        self.ComboB_TID.addItem("")
        self.ComboB_TID.addItem("")
        self.ComboB_TID.addItem("")

        self.retranslateUi(Dialog)
        self.ButtonBox_Confirm.accepted.connect(Dialog.accept)
        self.ButtonBox_Confirm.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MAP"))
        self.PB_Load.setText(_translate("Dialog", "Load Data"))
        self.PB_Load.clicked.connect(self.PB_Load)
        self.PB_Info.setText(_translate("Dialog", "Data Info"))
        self.PB_BLSetting.setText(_translate("Dialog", "BL Setting"))
        self.PB_All.setText(_translate("Dialog", "Plot All"))
        self.PB_Quit.setText(_translate("Dialog", "Quit"))
        self.CB_Marker.setText(_translate("Dialog", "Plot Marker"))
        self.CB_Line.setText(_translate("Dialog", "Plot Line"))
        self.CB_HM.setText(_translate("Dialog", "Plot Heatmap"))
        self.CB_Another.setText(_translate("Dialog", "Select Another"))
        self.label_TrackID.setText(_translate("Dialog", "Track ID:"))
        self.ComboB_TID.setItemText(0, _translate("Dialog", "1"))
        self.ComboB_TID.setItemText(1, _translate("Dialog", "2"))
        self.ComboB_TID.setItemText(2, _translate("Dialog", "3"))
        self.ComboB_TID.setItemText(3, _translate("Dialog", "..."))
    
    def PB_Load(self):
        # read data from csv file (Ask for file location)
        print("Reading Data From File...")
        data_name = pd.read_csv("C:\\Users\\AyG\\Desktop\\Git\\SoftwareEngineering_pjt\\data\\25_car.csv")
        print("Framing Data...")
        dataframed_data = pd.DataFrame(data_name)

        display_Data_Info(data_name)
        specify_map_attr()
        m = creat_map(DEF_LON,DEF_LAT)
        print("Basic Layer Creation successful!")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

