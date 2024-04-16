# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 15:17:22.

"""This script initializes the QApplication 
        and the UbuntuDesktopFileManager, 
        and starts the application event loop."""

import sys
from typing import NoReturn

from ldf_ui_view import UbuntuDesktopFileView as UdfView
from ldf_ui_categories_view import UbuntuDesktopFileCategoriesView as UdfCategoriesView
from ldf_controller import UbuntuDesktopFileController as UdfController
from ldf_model import UbuntuDesktopFileModel as UdfModel

from PyQt6.QtWidgets import QApplication


class UbuntuDesktopFileManager:
    """Manage the Ubuntu Desktop File Manager.

    This class is responsible for managing the Ubuntu Desktop File Manager.

    Attributes:
        udf_view: The view component for the Ubuntu Desktop File.
        udf_categories_view: The categories view component for the Ubuntu Desktop File.
        udf_controller: The controller component for the Ubuntu Desktop File.
        udf_model: The model component for the Ubuntu Desktop File.
    """

    def __init__(self) -> None:
        self.udf_view = UdfView()
        self.udf_categories_view = UdfCategoriesView()
        self.udf_model = UdfModel()
        self.udf_controller = UdfController(app,
                                            self.udf_view, self.udf_categories_view, self.udf_model
                                            )
        self.udf_controller.connect_signals()

    @staticmethod
    def run() -> NoReturn:
        """Exit the application event loop."""
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = UbuntuDesktopFileManager()
    manager.run()
