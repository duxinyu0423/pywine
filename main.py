import sys

from PyQt5.QtWidgets import QApplication
from tools.tools import Pywine

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    # 启动程序
    app = QApplication(sys.argv)
    main = Pywine()
    # 系统退出
    sys.exit(app.exec_())
