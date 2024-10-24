# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from Common.Threads import ThreadSep
import time
from utils import *



class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        try:
            configs = read_json(path="./configs.json")
        except:
            pass

        self.resize(600, 605)
        self.setWindowTitle("Tool Sep")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 300))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.groupBox.setTitle("Cấu hình chung")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.gridLayout_groupbox = QGridLayout(self.groupBox)
        self.gridLayout_groupbox.setObjectName(u"gridLayout_groupbox")

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText("Loại trình duyệt:")
        self.gridLayout_groupbox.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_type_browser = QComboBox(self.groupBox)
        self.comboBox_type_browser.addItems(["Chrome", "Gologin"])
        try:
            self.comboBox_type_browser.setCurrentText(configs["type_browser"])
        except:
            pass
        self.gridLayout_groupbox.addWidget(self.comboBox_type_browser, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText("Api trình duyệt:")
        self.gridLayout_groupbox.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_api_browser = QLineEdit(self.groupBox)
        self.lineEdit_api_browser.setObjectName(u"lineEdit_api_browser")
        try:
            self.lineEdit_api_browser.setText(configs["api_key"])
        except:
            pass
        self.gridLayout_groupbox.addWidget(self.lineEdit_api_browser, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText("Đường dẫn profile:")
        self.gridLayout_groupbox.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_path_browser = QLineEdit(self.groupBox)
        self.lineEdit_path_browser.setObjectName(u"lineEdit_path_browser")
        self.gridLayout_groupbox.addWidget(self.lineEdit_path_browser, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText("Phiển bản trình duyệt:")
        self.gridLayout_groupbox.addWidget(self.label, 3, 0, 1, 1)

        self.comboBox_version_browser = QComboBox(self.groupBox)
        self.comboBox_version_browser.addItems(["121", "122", "123", "124"])
        self.gridLayout_groupbox.addWidget(self.comboBox_version_browser, 3, 1, 1, 1)

        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setMinimumSize(QSize(0, 300))
        self.groupBox1.setMaximumSize(QSize(300, 16777215))
        self.groupBox1.setTitle("Cấu hình chạy")
        self.gridLayout.addWidget(self.groupBox1, 0, 1, 1, 1)

        self.gridLayout_groupbox1 = QGridLayout(self.groupBox1)
        self.gridLayout_groupbox1.setObjectName(u"gridLayout_groupbox1")

        self.label = QLabel(self.groupBox1)
        self.label.setObjectName(u"label")
        self.label.setText("Danh sách profile:")
        self.gridLayout_groupbox1.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        try:
            self.plainTextEdit.setPlainText(configs["list_profile_id"])
        except:
            pass
        self.gridLayout_groupbox1.addWidget(self.plainTextEdit, 0, 1, 1, 1)


        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setText("Chạy")
        self.gridLayout.addWidget(self.pushButton_run, 1, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setText("Dừng")
        self.gridLayout.addWidget(self.pushButton_stop, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["STT", "email", "status"])
        # Set sao cho cột cuối cùng vừa khít với size giao diện
        # Điều chỉnh cho cột vừa khít với kích thước bảng
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)

        self.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(self)

        # Kết nối
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_stop.clicked.connect(self.stop)
    
    def run(self):
        list_profile_id = self.plainTextEdit.toPlainText()
        type_browser = self.comboBox_type_browser.currentText()
        api_key = self.lineEdit_api_browser.text()

        configs = {
                    "type_browser": type_browser,
                    "api_key": api_key,
                    "list_profile_id": list_profile_id
                    }
        write_json(path="./configs.json", data=configs)

        self.list_thread = {}

        list_profile_id = list_profile_id.split("\n")

        for i in range(len(list_profile_id)):
            # Tạo luồng
            self.list_thread["luồng thứ " + str(i)] = ThreadSep(
                                                                index_thread=i, 
                                                                id_profile=list_profile_id[i], 
                                                                type_browser=type_browser, 
                                                                api_key=api_key
                                                                )
            # Khởi chạy
            self.list_thread["luồng thứ " + str(i)].start()
            self.list_thread["luồng thứ " + str(i)].signal_update.connect(self.update_row_table)
            # Tạo mới hàng vào bảng
            self.insert_row_table(data=[i, "", f"Đang khởi tạo trình duyệt của luồng {i}..."])
    
    def stop(self):
        for thread in self.list_thread :
            self.list_thread[thread].stop()

    def insert_row_table(self, data):
        # Tạo 1 hàng mới vào table
        # Lấy số lượng hàng hiện tại
        row_position = self.tableWidget.rowCount()
        # Tạo một hàng mới ở vị trí cuối
        self.tableWidget.insertRow(row_position)
        # Thêm giá trị vào hàng vừa tạo
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(data[0])))    
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(data[1])))   
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(data[2])))   
    
    def update_row_table(self, index_row, data):
        self.tableWidget.setItem(index_row, 0, QTableWidgetItem(str(data[0])))    
        self.tableWidget.setItem(index_row, 1, QTableWidgetItem(str(data[1])))   
        self.tableWidget.setItem(index_row, 2, QTableWidgetItem(str(data[2])))   


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())