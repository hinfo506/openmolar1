# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/qt-designer/saveMemo.ui'
#
# Created: Wed Jun 17 13:09:17 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 236)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 4)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.noExpire_radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.noExpire_radioButton.setChecked(True)
        self.noExpire_radioButton.setObjectName("noExpire_radioButton")
        self.gridLayout.addWidget(self.noExpire_radioButton, 0, 0, 1, 1)
        self.dateExpire_radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.dateExpire_radioButton.setObjectName("dateExpire_radioButton")
        self.gridLayout.addWidget(self.dateExpire_radioButton, 1, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewAll_radioButton = QtGui.QRadioButton(self.groupBox_3)
        self.viewAll_radioButton.setChecked(True)
        self.viewAll_radioButton.setObjectName("viewAll_radioButton")
        self.verticalLayout.addWidget(self.viewAll_radioButton)
        self.viewSurgery_radioButton = QtGui.QRadioButton(self.groupBox_3)
        self.viewSurgery_radioButton.setObjectName("viewSurgery_radioButton")
        self.verticalLayout.addWidget(self.viewSurgery_radioButton)
        self.viewReception_radioButton = QtGui.QRadioButton(self.groupBox_3)
        self.viewReception_radioButton.setObjectName("viewReception_radioButton")
        self.verticalLayout.addWidget(self.viewReception_radioButton)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 2, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.author_comboBox = QtGui.QComboBox(self.groupBox)
        self.author_comboBox.setObjectName("author_comboBox")
        self.verticalLayout_2.addWidget(self.author_comboBox)
        self.gridLayout_2.addWidget(self.groupBox, 1, 2, 1, 1)
        self.phraseBook_pushButton = QtGui.QPushButton(Dialog)
        self.phraseBook_pushButton.setObjectName("phraseBook_pushButton")
        self.gridLayout_2.addWidget(self.phraseBook_pushButton, 1, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 2, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Post a memo about this Patient", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Expiry Policy", None, QtGui.QApplication.UnicodeUTF8))
        self.noExpire_radioButton.setText(QtGui.QApplication.translate("Dialog", "Do Not Expire", None, QtGui.QApplication.UnicodeUTF8))
        self.dateExpire_radioButton.setText(QtGui.QApplication.translate("Dialog", "Expire on this date", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Viewable by", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAll_radioButton.setText(QtGui.QApplication.translate("Dialog", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.viewSurgery_radioButton.setText(QtGui.QApplication.translate("Dialog", "Surgery Machines", None, QtGui.QApplication.UnicodeUTF8))
        self.viewReception_radioButton.setText(QtGui.QApplication.translate("Dialog", "Reception Machines", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.phraseBook_pushButton.setText(QtGui.QApplication.translate("Dialog", "PhraseBook", None, QtGui.QApplication.UnicodeUTF8))
