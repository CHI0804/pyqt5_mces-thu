import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from dashboard import *  # 导入我们刚转换的ui


class MyWindows(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

my_windows = MyWindows()  # 实例化对象
my_windows.show()  # 显示窗口

sys.exit(app.exec_())
