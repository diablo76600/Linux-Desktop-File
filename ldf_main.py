# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 15:17:22.

"""This script initializes the QApplication 
        and the LinuxDesktopFileManager,
        and starts the application event loop."""

import sys
from typing import NoReturn

from PyQt6.QtWidgets import QApplication

from ldf_controller import LinuxDesktopFileController as LdfController
from ldf_tools import LinuxDesktopFileTools as LdfTools
from ldf_ui_categories_view import LinuxDesktopFileCategoriesView as LdfCategoriesView
from ldf_ui_view import LinuxDesktopFileView as LdfView


class LinuxDesktopFileManager:
    """Manage the Linux Desktop File Manager.

    This class is responsible for managing the Linux Desktop File Manager.

    Attributes:
        ldf_view: The view component for the Linux Desktop File.
        ldf_categories_view: The categories view component for the Linux Desktop File.
        ldf_controller: The controller component for the Linux Desktop File.
        ldf_tools: The model component for the Linux Desktop File.
    """
    
    def __init__(self) -> None:
        self.ldf_view = LdfView()
        self.ldf_categories_view = LdfCategoriesView()
        self.ldf_tools = LdfTools()
        self.ldf_controller = LdfController(
            app, self.ldf_view, self.ldf_categories_view, self.ldf_tools
        )
        self.ldf_controller.connect_signals()

    @staticmethod
    def run() -> NoReturn:
        """Exit the application event loop."""
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = LinuxDesktopFileManager()
    manager.run()
