import os

from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from data.constant import BASE_DIR
from gen.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon(os.path.join(BASE_DIR, 'ui/icons/demo.png')))
        self.btnPath.clicked.connect(self._on_btn_path_clicked)
        self.btnOk.clicked.connect(self._on_ok_clicked)
        self.de_time.setDateTime(QDateTime.currentDateTime())

    def _on_btn_path_clicked(self):
        path = QFileDialog.getOpenFileName(self, '选择文件路径')
        if len(path) == 0:
            return
        self.te_path.setText(path[0])

    def _on_ok_clicked(self):
        print("路径:", self.te_path.text())
        print("名字1:", self.te_name1.text())
        print("名字2:", self.te_name2.text())

        QMessageBox.information(self, '提示',
                                f'路径:{self.te_path.text()}\n名字1:{self.te_name1.text()}\n名字2:{self.te_name2.text()}')
