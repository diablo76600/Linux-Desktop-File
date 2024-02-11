# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 17:56:19.


import sys

from PyQt6.QtWidgets import QApplication
from udf_manager import UbuntuDesktopFileManager


if __name__ == "__main__":
    '''This script initializes the QApplication 
        and the UbuntuDesktopFileManager, 
        and starts the application event loop.'''
    app = QApplication(sys.argv)
    manager = UbuntuDesktopFileManager(app)
    sys.exit(app.exec())
