# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 12:23:10.


import os

from udf_ui_view import UbuntuDesktopFileView
from udf_ui_categories_view import UbuntuDesktopFileCategoriesView

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog


class UbuntuDesktopFileController:
    '''Manage the Ubuntu Desktop File Controller.

This class is responsible for managing the Ubuntu Desktop File Controller.
It handles the logic and coordination between the view, categories view,
and model components.

Attributes:
    udf_view: The view component for the Ubuntu Desktop File.
    udf_categories_view: The categories view component for the Ubuntu Desktop File.'''

    def __init__(self, udf_view: UbuntuDesktopFileView, udf_categories_view: UbuntuDesktopFileCategoriesView) -> None:
        self.udf_view = udf_view
        self.udf_categories_view = udf_categories_view
        self.udf_categories_view.categories_selected.connect(self.update_categories)
        self.udf_view.lineEdit_exec.textChanged.connect(self.update_application_name)

    def update_categories(self, list_categories: list) -> None:
        '''Update the categories in the view based on the selected categories.'''
        self.udf_view.lineEdit_categories.setText(";".join(list_categories))

    @staticmethod
    def display_message(title: str, text: str, type: str) -> None:
        '''Display a message box with the specified title, text, and type.'''
        if type == "warning":
            QMessageBox.warning(None, title, text)
        else:
            QMessageBox.information(None, title, text)

    @staticmethod
    def get_application_name(exec_path: str) -> str:
        '''Extract the application name from the provided executable path.'''
        return os.path.splitext(os.path.basename(exec_path))[0]
    
    def update_application_name(self) -> None:
        '''Update the application name based on the entered executable path.'''
        application_name: str = self.get_application_name(
            self.udf_view.lineEdit_exec.text()
        )
        self.udf_view.lineEdit_name.setText(application_name)

    def check_widgets(self) -> bool:
        '''Check if all required widgets have valid values.'''
        if not self.udf_view.lineEdit_name.text():
            self.display_message(
                self.udf_view.title, "Please enter an Application Name.", "information"
            )
            return False
        if not self.udf_view.lineEdit_exec.text():
            message = (
                "Please select Python file."
                if self.udf_view.checkBox_python.isChecked()
                else "Please select Executable file."
            )
            self.display_message(self.udf_view.title, message, "information")
            return False
        return True

    def update_checkbox_text(self) -> None:
        '''Update the text of the checkbox based on its state.'''
        checkbox = self.udf_view.sender()
        if checkbox == self.udf_view.checkBox_directory:
            checkbox.setText(
                os.path.dirname(self.udf_view.lineEdit_exec.text())
                if checkbox.isChecked()
                else ""
            )
        else:
            checkbox.setText(str(checkbox.isChecked()))

    def set_path_directory(self) -> None:
        '''Set the text of the directory checkbox based on its state.'''
        self.udf_view.checkBox_directory.setText(
            os.path.dirname(self.udf_view.lineEdit_exec.text())
            if self.udf_view.checkBox_directory.isChecked()
            else ""
        )

    def select_file_dialog(self, caption: str, filter: str) -> str|None:
        '''Open a file dialog to select a file.'''
        if file := QFileDialog.getOpenFileName(parent=self.udf_view, caption=caption, filter=filter)[0]:
            return file
        return None

    def select_exec_or_python_file(self) -> None:
        '''Select the executable or Python file based on the checkbox state.'''
        if self.udf_view.checkBox_python.isChecked():
            self.get_exec_file(python=True)
        else:
            self.get_exec_file(python=False)
        self.set_path_directory()

    def get_exec_file(self, python: bool) -> None:
        '''Open a file dialog to select the executable or Python file.'''
        caption = (
            "Select a Python file."
            if python
            else "Select an Executable file."
        )
        py_filter = "*.py" if python else ""
        if file := self.select_file_dialog(caption=caption, filter=py_filter):
            if not python and os.access(file, os.X_OK):
                self.udf_view.lineEdit_exec.setText(file)
            elif python:
                self.udf_view.lineEdit_exec.setText(file)
            else:
                self.display_message(
                    self.udf_view.title,
                    f"{file} <font color='red'>is not executable</font>.",
                    "information",
                )
        else:
            self.udf_view.lineEdit_exec.clear()

    def set_icon(self) -> None:
        '''Open a file dialog to select the icon file.'''
        if icon_file := self.select_file_dialog(caption="Select Icon file.", filter=""):
            pixmap = QPixmap(icon_file)
            if pixmap.isNull():
                self.display_message(
                    self.udf_view.title,
                    f"{icon_file} <font color='red'>is not recognized</font>.",
                    "information",
                )
                self.udf_view.lineEdit_icon.clear()
            else:
                self.udf_view.lineEdit_icon.setText(icon_file)
                self.udf_view.label_icon_application.setPixmap(pixmap)

    def exec_categories(self) -> None:
        '''Execute the categories view.'''
        self.udf_categories_view.exec()

    def update_python_label(self) -> None:
        '''Update the label and style based on the Python checkbox state.'''
        self.udf_view.lineEdit_exec.clear()
        if self.udf_view.checkBox_python.isChecked():
            self.udf_view.label_exec.setText("Python File :")
            self.udf_view.label_exec.setStyleSheet("color : red;")
        else:
            self.udf_view.label_exec.setText("Exec :")
            self.udf_view.label_exec.setStyleSheet("color : None;")
