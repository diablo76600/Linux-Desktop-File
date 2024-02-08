# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 15:17:22.


import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QFileDialog


class UbuntuDesktopFileManager:
    def __init__(self, udf_view, udf_controller, udf_categories_view):
        self.udf_view = udf_view
        self.udf_controller = udf_controller
        self.udf_categories_view = udf_categories_view
        self.udf_view.lineEdit_exec.textChanged.connect(self.update_application_name)
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
                self.udf_view.checkBox_python: self.launch_with_python,
            }
        )

    def _connect_signals(self, widgets: dict) -> None:
        # Connect widgets using the mapping
        for widget, slot in widgets.items():
            widget.clicked.connect(slot)

    def update_application_name(self) -> None:
        # Update the application name based on the entered executable path
        application_name: str = self.udf_controller.get_application_name(
            self.udf_view.lineEdit_exec.text()
        )
        self.udf_view.lineEdit_name.setText(application_name)

    def save_desktop_file(self) -> None:
        # Save the desktop file with the entered data
        if not self.check_widgets():
            return
        if destination := QFileDialog.getSaveFileName(
            self.udf_view, "Save Desktop file", f"{self.udf_view.lineEdit_name.text()}.desktop"
        )[0]:
            desktop_file_data = self.udf_controller.generate_desktop_file_data(
                self.get_all_data()
            )
            state, message = self.udf_controller.write_desktop_file(destination, desktop_file_data)
            if state:
                self.udf_controller.display_message(
                    self.udf_view.title, message, "information"
                )
            else:
                self.udf_controller.display_message(
                    self.udf_view.title, message, "warning"
                )

    def check_widgets(self) -> bool:
        # Check if all required widgets have valid values
        if not self.udf_view.lineEdit_name.text():
            self.udf_controller.display_message(
                self.udf_view.title, "Please enter an Application Name.", "information"
            )
            return False
        if not self.udf_view.lineEdit_exec.text():
            message = (
                "Please select Python file."
                if self.udf_view.checkBox_python.isChecked()
                else "Please select Executable file."
            )
            self.udf_controller.display_message(self.udf_view.title, message, "information")
            return False
        return True

    def update_checkbox_text(self) -> None:
        # Update the text of the checkbox based on its state
        checkbox = self.udf_view.sender()
        if checkbox == self.udf_view.checkBox_directory:
            checkbox.setText(
                os.path.dirname(self.udf_view.lineEdit_exec.text())
                if checkbox.isChecked()
                else ""
            )
        else:
            checkbox.setText(str(checkbox.isChecked()))

    def get_all_data(self) -> dict:
        # Get all the entered data from the widgets
        return {
            "Categories": self.udf_view.lineEdit_categories.text(),
            "Comment": self.udf_view.lineEdit_comment.text(),
            "Exec": self.udf_view.lineEdit_exec.text(),
            "GenericName": self.udf_view.lineEdit_generic_name.text(),
            "Icon": self.udf_view.lineEdit_icon.text(),
            "Name": self.udf_view.lineEdit_name.text(),
            "Path": (
                os.path.dirname(self.udf_view.lineEdit_exec.text())
                if self.udf_view.checkBox_directory.isChecked()
                else ""
            ),
            "StartupNotify": str(self.udf_view.checkBox_startup.isChecked()).lower(),
            "Terminal": str(self.udf_view.checkBox_terminal.isChecked()).lower(),
            "Type": self.udf_view.lineEdit_type.text(),
            "Version": self.udf_view.lineEdit_version.text(),
        }

    def set_path_directory(self) -> None:
        # Set the text of the directory checkbox based on its state
        self.udf_view.checkBox_directory.setText(
            os.path.dirname(self.udf_view.lineEdit_exec.text())
            if self.udf_view.checkBox_directory.isChecked()
            else ""
        )

    def select_exec_or_python_file(self) -> None:
        # Select the executable or Python file based on the checkbox state
        if self.udf_view.checkBox_python.isChecked():
            self.get_exec_file(python=True)
        else:
            self.get_exec_file(python=False)
        self.set_path_directory()

    def get_exec_file(self, python: bool) -> None:
        # Open a file dialog to select the executable or Python file
        title = (
            "Select a Python file."
            if python
            else "Select an Executable file."
        )
        file_filter = "*.py" if python else ""
        if file := QFileDialog.getOpenFileName(self.udf_view, title, filter=file_filter)[0]:
            if not python and os.access(file, os.X_OK):
                self.udf_view.lineEdit_exec.setText(file)
            elif python:
                self.udf_view.lineEdit_exec.setText(file)
            else:
                self.udf_controller.display_message(
                    self.udf_view.title,
                    f"{file} <font color='red'>is not executable</font>.",
                    "information",
                )
        else:
            self.udf_view.lineEdit_exec.clear()

    def set_icon(self) -> None:
        # Open a file dialog to select the icon file
        if icon_file := QFileDialog.getOpenFileName(self.udf_view, "Select Icon file.")[0]:
            pixmap = QPixmap(icon_file)
            if pixmap.isNull():
                self.udf_controller.display_message(
                    self.udf_view.title,
                    f"{icon_file} <font color='red'>is not recognized</font>.",
                    "information",
                )
                self.udf_view.lineEdit_icon.clear()
            else:
                self.udf_view.lineEdit_icon.setText(icon_file)
                self.udf_view.label_icon_application.setPixmap(pixmap)

    def exec_categories(self) -> None:
        # Execute the categories view
        self.udf_categories_view.exec()

    def launch_with_python(self) -> None:
        # Update the label and style based on the Python checkbox state
        if self.udf_view.checkBox_python.isChecked():
            self.udf_view.label_exec.setText("Python File :")
            self.udf_view.label_exec.setStyleSheet("color : red;")
        else:
            self.udf_view.label_exec.setText("Exec :")
            self.udf_view.label_exec.setStyleSheet("color : None;")