# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 17:56:19.


import sys

from PyQt6.QtWidgets import QApplication
from ubuntu_desktop_file_view import DesktopFileView
from ubuntu_desktop_file_controller import UbuntuDesktopFileController
from ubuntu_desktop_file_manager import UbuntuDesktopFileManager
from ubuntu_desktop_file_categories_view import UbuntuDesktopFileCategories


if __name__ == "__main__":
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of DesktopFileView
    udf_view = DesktopFileView()

    # Create an instance of UbuntuDesktopFileCategories
    udf_categories_view = UbuntuDesktopFileCategories()

    # Create an instance of UbuntuDesktopFileController
    udf_controller = UbuntuDesktopFileController(udf_view, udf_categories_view)

    # Create an instance of UbuntuDesktopFileManager
    udf_manager = UbuntuDesktopFileManager(udf_view, udf_controller, udf_categories_view)

    # Show the desktop file view
    udf_view.show()

    # Start the application event loop
    sys.exit(app.exec())
