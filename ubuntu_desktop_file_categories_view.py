# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.

from PyQt6.QtCore import QRect, pyqtSignal
from PyQt6.QtWidgets import QCheckBox, QDialog, QGridLayout, QPushButton, QWidget


class UbuntuDesktopFileCategories(QDialog):
    # Signal emitted when categories are selected
    categories_selected = pyqtSignal(list)

    # Predefined categories
    CATEGORIES = [
        "AudioVideo",
        "Audio",
        "Building",
        "DesktopSettings",
        "Development",
        "Education",
        "Game",
        "Graphics",
        "Network",
        "Office",
        "Qt",
        "Settings",
        "System",
        "TextEditor",
        "Utility",
    ]

    def __init__(self) -> None:
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Select your categories")
        self.setFixedSize(602, 207)

        # Create a grid layout to hold the checkboxes
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(8, 8, 585, 165))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Add checkboxes for each category to the grid layout
        for index, category in enumerate(self.CATEGORIES):
            row, col = divmod(index, 5)
            checkbox = QCheckBox(self.gridLayoutWidget)
            checkbox.setText(category)
            self.gridLayout.addWidget(checkbox, row, col, 1, 1)

        # Create an "Ok" button and connect its clicked signal to the get_type_categories method
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Ok")
        self.pushButton.setGeometry(QRect(int((self.width() / 2) - 34), 168, 68, 32))
        self.pushButton.clicked.connect(self.get_type_categories)

    def get_type_categories(self) -> None:
        # Retrieve the selected categories from the checkboxes
        list_categories = [
            check_box.text()
            for check_box in self.gridLayoutWidget.findChildren(QCheckBox)
            if check_box.isChecked()
        ]

        # Emit the selected categories as a signal
        self.categories_selected.emit(list_categories)

        # Close the dialog window
        self.close()
