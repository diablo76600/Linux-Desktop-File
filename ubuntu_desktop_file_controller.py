# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 12:23:10.


import os

from PyQt6.QtWidgets import QMessageBox


class UbuntuDesktopFileController:
    def __init__(self, udf_view, udf_categories_view) -> None:
        self.udf_view = udf_view
        udf_categories_view.categories_selected.connect(self.update_categories)

    def update_categories(self, list_categories: list) -> None:
        # Update the categories in the view based on the selected categories
        self.udf_view.lineEdit_categories.setText(";".join(list_categories))

    def generate_desktop_file_data(self, data: dict) -> str:
        # Generate the data for the desktop file based on the provided data dictionary
        if self.udf_view.checkBox_python.isChecked():
            data["Exec"] = f"python3 {data['Exec']}"
        return "[Desktop Entry]\n" + "\n".join(
            f"{key}={value}" for key, value in data.items()
        )

    @staticmethod
    def write_desktop_file(destination: str, desktop_data: str) -> tuple:
        # Write the desktop file to the specified destination
        try:
            with open(destination, "w", encoding="utf-8") as desktop_file:
                desktop_file.write(desktop_data)
                return True, f"File {destination} saved."
        except IOError as error:
            return False, f"<font color='red'>Unable to create file !! {error}</font>"

    @staticmethod
    def display_message(title: str, text: str, type: str) -> None:
        # Display a message box with the specified title, text, and type
        if type == "warning":
            QMessageBox.warning(None, title, text)
        else:
            QMessageBox.information(None, title, text)

    @staticmethod
    def get_application_name(exec_path: str) -> str:
        # Extract the application name from the provided executable path
        return os.path.splitext(os.path.basename(exec_path))[0]