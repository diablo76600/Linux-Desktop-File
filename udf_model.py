# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 22:45:06.

import os

from udf_ui_view import UbuntuDesktopFileView
from udf_controller import UbuntuDesktopFileController

from PyQt6.QtWidgets import QFileDialog


class UbuntuDesktopFileModel:
    '''Manage the Ubuntu Desktop File Model.

    This class is responsible for managing the Ubuntu Desktop File Model.
    It provides methods for getting all the entered data from the widgets,
    saving the desktop file with the entered data,
    and generating the data for the desktop file based on the provided data dictionary.

    Attributes:
        udf_view: The view component for the Ubuntu Desktop File.
        udf_controller: The controller component for the Ubuntu Desktop File.'''

    def __init__(
        self,
        udf_view: UbuntuDesktopFileView,
        udf_controller: UbuntuDesktopFileController,
    ):
        self.udf_view = udf_view
        self.udf_controller = udf_controller

    def get_all_data(self) -> dict:
        """Get all the entered data from the widgets."""
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

    def save_desktop_file(self) -> None:
        """Save the desktop file with the entered data."""
        if not self.udf_controller.check_widgets():
            return
        if destination := QFileDialog.getSaveFileName(
            self.udf_view,
            "Save Desktop file",
            f"{self.udf_view.lineEdit_name.text()}.desktop",
        )[0]:
            desktop_file_data = self.generate_desktop_file_data(self.get_all_data())
            state, message = self.write_desktop_file(destination, desktop_file_data)
            if state:
                self.udf_controller.display_message(
                    self.udf_view.title, message, "information"
                )
            else:
                self.udf_controller.display_message(
                    self.udf_view.title, message, "warning"
                )

    def generate_desktop_file_data(self, data: dict) -> str:
        """Generate the data for the desktop file based on the provided data dictionary."""
        if self.udf_view.checkBox_python.isChecked():
            data["Exec"] = f"python3 {data['Exec']}"
        return "[Desktop Entry]\n" + "\n".join(
            f"{key}={value}" for key, value in data.items()
        )

    @staticmethod
    def write_desktop_file(destination: str, desktop_data: str) -> tuple:
        """Write the desktop file to the specified destination."""
        try:
            with open(destination, "w", encoding="utf-8") as desktop_file:
                desktop_file.write(desktop_data)
                return True, f"File {destination} saved."
        except IOError as error:
            return False, f"<font color='red'>Unable to create file !! {error}</font>"
