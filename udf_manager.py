# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 15:17:22.


from udf_ui_view import UbuntuDesktopFileView
from udf_ui_categories_view import UbuntuDesktopFileCategoriesView
from udf_controller import UbuntuDesktopFileController
from udf_model import UbuntuDesktopFileModel

from PyQt6.QtWidgets import QApplication


class UbuntuDesktopFileManager:
    '''Manage the Ubuntu Desktop File Manager.

This class is responsible for managing the Ubuntu Desktop File Manager. 
It initializes the necessary components and connects signals to their respective slots.

Attributes:
    udf_view: The view component for the Ubuntu Desktop File.
    udf_categories_view: The categories view component for the Ubuntu Desktop File.
    udf_controller: The controller component for the Ubuntu Desktop File.
    udf_model: The model component for the Ubuntu Desktop File.
'''

    def __init__(self, app: QApplication):
        self.app = app
        self.udf_view = UbuntuDesktopFileView()
        self.udf_categories_view = UbuntuDesktopFileCategoriesView()
        self.udf_model = UbuntuDesktopFileModel()
        self.udf_controller = UbuntuDesktopFileController(
            self.udf_view, self.udf_categories_view, self.udf_model
        )
        self.connect_signals()


    def connect_signals(self):
        '''Connect signals to their respective slots.'''
        signal_connections = {
            self.udf_view.pushButton_exec: self.udf_controller.select_executable_or_python_file,
            self.udf_view.pushButton_icon: self.udf_controller.set_icon,
            self.udf_view.pushButton_save: self.udf_controller.save_desktop_file,
            self.udf_view.pushButton_quit: self.app.exit,
            self.udf_view.pushButton_categories: self.udf_categories_view.exec,
            self.udf_view.checkBox_terminal: self.udf_controller.update_checkbox_text,
            self.udf_view.checkBox_startup: self.udf_controller.update_checkbox_text,
            self.udf_view.checkBox_directory: self.udf_controller.set_path_directory,
            self.udf_view.checkBox_python: self.udf_controller.update_python_label,
        }
        for signal, slot in signal_connections.items():
            signal.clicked.connect(slot)