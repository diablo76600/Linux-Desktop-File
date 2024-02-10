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

    def __init__(self):
        self.udf_view = UbuntuDesktopFileView()
        self.udf_categories_view = UbuntuDesktopFileCategoriesView()
        self.udf_controller = UbuntuDesktopFileController(
            self.udf_view, self.udf_categories_view
        )
        self.udf_model = UbuntuDesktopFileModel(self.udf_view, self.udf_controller)
        self._connect_signals(
            {
                self.udf_view.pushButton_exec: self.select_exec_or_python_file,
                self.udf_view.pushButton_icon: self.set_icon,
                self.udf_view.pushButton_save: self.save_desktop_file,
                self.udf_view.pushButton_quit: QApplication.exit,
                self.udf_view.pushButton_categories: self.exec_categories,
                self.udf_view.checkBox_terminal: self.update_checkbox_text,
                self.udf_view.checkBox_startup: self.update_checkbox_text,
                self.udf_view.checkBox_directory: self.set_path_directory,
                self.udf_view.checkBox_python: self.update_python_label,
            }
        )

    def _connect_signals(self, widgets: dict) -> None:
        '''Connect widgets using the mapping.'''
        for widget, slot in widgets.items():
            widget.clicked.connect(slot)

    def select_exec_or_python_file(self):
        '''Select the executable or Python file based on the checkbox state.'''
        self.udf_controller.select_exec_or_python_file()

    def set_icon(self):
        '''This method is responsible for setting the icon.'''
        self.udf_controller.set_icon()

    def save_desktop_file(self):
        '''This method is responsible for saving the desktop file.'''
        self.udf_model.save_desktop_file()

    def exec_categories(self):
        '''This method is responsible for executing the categories.'''
        self.udf_controller.exec_categories()

    def update_checkbox_text(self):
        '''This method is responsible for updating the text of the checkbox based on its state.'''
        self.udf_controller.update_checkbox_text()

    def set_path_directory(self):
        '''This method is responsible for setting the path directory.'''
        self.udf_controller.set_path_directory()

    def update_python_label(self):
        '''Update the label and style based on the Python checkbox state.'''
        self.udf_controller.update_python_label()