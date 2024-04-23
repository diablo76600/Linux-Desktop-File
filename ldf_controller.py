# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 12:23:10.


import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtCore import QEvent

from ldf_tools import LinuxDesktopFileTools as LdfTools
from ldf_ui_categories_view import LinuxDesktopFileCategoriesView as LdfCategoriesView
from ldf_ui_view import LinuxDesktopFileView as LdfView


class LinuxDesktopFileController:
    """Controller class for managing the Linux Desktop File.

    This class provides methods for handling user interactions
    and managing the data flow between the view
    and model components of the Linux Desktop File application.

    Args:
        ldf_view: The view component for the Linux Desktop File.
        ldf_categories_view: The view component for the Linux Desktop File Categories.
        ldf_tools: The model component for the Linux Desktop File."""

    def __init__(self, app, ldf_view: LdfView, ldf_categories_view: LdfCategoriesView, ldf_tools: LdfTools) -> None:
        self.app = app
        self.ldf_view = ldf_view
        self.ldf_categories_view = ldf_categories_view
        self.ldf_tools = ldf_tools
        self.ldf_categories_view.categories_selected.connect(self.update_categories)
        self.ldf_view.lineEdit_exec.textChanged.connect(self.update_application_name)

    def connect_signals(self):
        """Connect signals to their respective slots."""
        signal_connections = {
            self.ldf_view.pushButton_exec: self.select_executable_or_python_file,
            self.ldf_view.pushButton_icon: self.set_icon,
            self.ldf_view.pushButton_save: self.save_desktop_file,
            self.ldf_view.pushButton_quit: self.app.exit,
            self.ldf_view.pushButton_categories: self.ldf_categories_view.exec,
            self.ldf_view.checkBox_directory: self.update_checkbox_text,
            self.ldf_view.checkBox_terminal: self.update_checkbox_text,
            self.ldf_view.checkBox_startup: self.update_checkbox_text,
            self.ldf_view.checkBox_python: self.update_python_label,
        }
        for signal, slot in signal_connections.items():
            signal.clicked.connect(slot)
        self.ldf_view.lineEdit_exec.textChanged.connect(
            self.update_checkbox_label_directory
        )

    def get_entered_data(self) -> dict:
        """Get all the entered data from the widgets."""
        return {
            "Categories": self.ldf_view.lineEdit_categories.text(),
            "Comment": self.ldf_view.lineEdit_comment.text(),
            "Exec": self.ldf_view.lineEdit_exec.text(),
            "GenericName": self.ldf_view.lineEdit_generic_name.text(),
            "Icon": self.ldf_view.lineEdit_icon.text(),
            "Name": self.ldf_view.lineEdit_name.text(),
            "Path": (
                os.path.dirname(self.ldf_view.lineEdit_exec.text())
                if self.ldf_view.checkBox_directory.isChecked()
                else ""
            ),
            "StartupNotify": str(self.ldf_view.checkBox_startup.isChecked()).lower(),
            "Terminal": str(self.ldf_view.checkBox_terminal.isChecked()).lower(),
            "Type": self.ldf_view.lineEdit_type.text(),
            "Version": self.ldf_view.lineEdit_version.text(),
        }

    def update_categories(self, list_categories: list) -> None:
        """Update the categories in the view based on the selected categories."""
        self.ldf_view.lineEdit_categories.setText(";".join(list_categories))

    @staticmethod
    def get_application_name(exec_path: str) -> str:
        """Extract the application name from the provided executable path."""
        return os.path.splitext(os.path.basename(exec_path))[0]

    def update_application_name(self) -> None:
        """Update the application name based on the entered executable path."""
        if self.ldf_view.lineEdit_name.text():
            return
        application_name: str = self.get_application_name(
            self.ldf_view.lineEdit_exec.text()
        )
        self.ldf_view.lineEdit_name.setText(application_name)

    def check_widgets(self) -> bool:
        """Check if all required widgets have valid values."""
        if not self.ldf_view.lineEdit_name.text():
            self.display_message(
                self.ldf_view.title, "Please enter an Application Name.", "information"
            )
            return False
        if not self.ldf_view.lineEdit_exec.text():
            message = (
                "Please select Python file."
                if self.ldf_view.checkBox_python.isChecked()
                else "Please select Executable file."
            )
            self.display_message(self.ldf_view.title, message, "information")
            return False
        return True

    def update_checkbox_text(self) -> None:
        """Update the text of the checkbox based on its state."""
        checkbox = self.ldf_view.sender()
        if checkbox == self.ldf_view.checkBox_directory:
            checkbox.setText(
                os.path.dirname(self.ldf_view.lineEdit_exec.text())
                if checkbox.isChecked()
                else ""
            )
        else:
            checkbox.setText(str(checkbox.isChecked()))

    def select_file_dialog(self, caption: str, filter: str) -> str | None:
        """Open a file dialog to select a file."""
        if file := QFileDialog.getOpenFileName(parent=self.ldf_view, caption=caption, filter=filter)[0]:
            return file
        return None

    def select_executable_or_python_file(self) -> None:
        """Open a file dialog to select the executable or Python file."""
        self.ldf_view.lineEdit_exec.clear()
        if is_python := self.ldf_view.checkBox_python.isChecked():
            caption = "Select a Python file."
            file_ext = "*.py"
        else:
            caption = "Select an Executable file."
            file_ext = ""
        if file_path := self.select_file_dialog(caption=caption, filter=file_ext):
            if not is_python and not os.access(file_path, os.X_OK):
                self.display_message(
                    self.ldf_view.title,
                    f"{file_path} <font color='red'>is not executable</font>.",
                    "information",
                )
            else:
                self.ldf_view.lineEdit_exec.setText(file_path)

    def update_checkbox_label_directory(self):
        if self.ldf_view.checkBox_directory.isChecked():
            self.ldf_view.checkBox_directory.setText(os.path.dirname(self.ldf_view.lineEdit_exec.text()))

    def set_icon(self) -> None:
        """Open a file dialog to select the icon file and display it."""
        if icon_file := self.select_file_dialog(caption="Select Icon file.", filter=""):
            pixmap = QPixmap(icon_file)
            if pixmap.isNull():
                self.display_message(
                    self.ldf_view.title,
                    f"{icon_file} <font color='red'>is not recognized</font>.",
                    "information",
                )
                self.ldf_view.lineEdit_icon.clear()
            else:
                self.ldf_view.lineEdit_icon.setText(icon_file)
                self.ldf_view.label_icon_application.setPixmap(pixmap)

    def exec_categories(self) -> None:
        """Execute the categories view."""
        self.ldf_categories_view.exec()

    def save_desktop_file(self) -> None:
        """Save the desktop file with the entered data."""
        if not self.check_widgets():
            return
        dict_data = self.get_entered_data()
        self.modify_exec_value(dict_data)
        if destination := self.choose_destination():
            desktop_file_data = self.ldf_tools.generate_desktop_file_data(dict_data)
            state, message = self.ldf_tools.write_desktop_file(destination, desktop_file_data)
            message_type = "information" if state else "warning"
            self.display_message(self.ldf_view.title, message, message_type)

    def modify_exec_value(self, data: dict) -> None:
        """Modify the 'Exec' value in the data dictionary if the checkbox is checked."""
        if self.ldf_view.checkBox_python.isChecked():
            data["Exec"] = f"python3 {data['Exec']}"

    def choose_destination(self) -> str:
        """Prompt the user to choose a destination to save the file."""
        file_name = f"{self.ldf_view.lineEdit_name.text()}.desktop"
        destination, _ = QFileDialog.getSaveFileName(
            self.ldf_view,
            "Save Desktop file",
            file_name
        )
        return destination

    def update_python_label(self) -> None:
        """Update the label and style based on the Python checkbox state."""
        self.ldf_view.lineEdit_exec.clear()
        if self.ldf_view.checkBox_python.isChecked():
            self.ldf_view.label_exec.setText("Python File :")
            self.ldf_view.label_exec.setStyleSheet("color : red;")
        else:
            self.ldf_view.label_exec.setText("Exec :")
            self.ldf_view.label_exec.setStyleSheet("color : None;")

    @staticmethod
    def display_message(title: str, text: str, type_message: str) -> None:
        """Display a message box with the specified title, text, and type.
        """
        if type_message == "warning":
            QMessageBox.warning(None, title, text)
        else:
            QMessageBox.information(None, title, text)
