# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 22:45:06.


class UbuntuDesktopFileModel:
    '''Manage the Ubuntu Desktop File Model.

    This class is responsible for managing the Ubuntu Desktop File Model.
    It provides methods for getting all the entered data from the widgets,
    saving the desktop file with the entered data,
    and generating the data for the desktop file based on the provided data dictionary.

    Attributes:
        udf_view: The view component for the Ubuntu Desktop File.
        udf_controller: The controller component for the Ubuntu Desktop File.'''


    @staticmethod
    def generate_desktop_file_data(data) -> str:
        """Generate the data for the desktop file based on the provided data dictionary."""
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
