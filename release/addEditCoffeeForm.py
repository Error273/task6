# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 277)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(352, 240, 141, 28))
        self.btn.setObjectName("btn")
        self.output = QtWidgets.QLabel(Form)
        self.output.setGeometry(QtCore.QRect(10, 240, 331, 31))
        self.output.setText("")
        self.output.setObjectName("output")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 501, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sort_name_edit = QtWidgets.QLineEdit(self.widget)
        self.sort_name_edit.setObjectName("sort_name_edit")
        self.gridLayout.addWidget(self.sort_name_edit, 0, 2, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 2, 2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 2, 1)
        self.type_edit = QtWidgets.QLineEdit(self.widget)
        self.type_edit.setObjectName("type_edit")
        self.gridLayout.addWidget(self.type_edit, 3, 2, 1, 1)
        self.degree_of_roasting_edit = QtWidgets.QLineEdit(self.widget)
        self.degree_of_roasting_edit.setObjectName("degree_of_roasting_edit")
        self.gridLayout.addWidget(self.degree_of_roasting_edit, 2, 2, 1, 1)
        self.volume_edit = QtWidgets.QLineEdit(self.widget)
        self.volume_edit.setObjectName("volume_edit")
        self.gridLayout.addWidget(self.volume_edit, 10, 2, 1, 1)
        self.taste_description_edit = QtWidgets.QLineEdit(self.widget)
        self.taste_description_edit.setObjectName("taste_description_edit")
        self.gridLayout.addWidget(self.taste_description_edit, 5, 2, 1, 1)
        self.cost_edit = QtWidgets.QLineEdit(self.widget)
        self.cost_edit.setObjectName("cost_edit")
        self.gridLayout.addWidget(self.cost_edit, 8, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление/изменение записи"))
        self.btn.setText(_translate("Form", "Добавить/изменить"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Молотый/в зернах"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
