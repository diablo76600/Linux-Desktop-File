# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 10:23:10.


from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QIcon, QFontMetrics, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QFrame,
)
from ldf_tools import LinuxDesktopFileTools as ldft

__version__: str = "1.0.9"


class ElideLineEdit(QLineEdit):
    """
    A custom QLineEdit widget that elides text to fit within its width.

    Args:
        a0: The text to set on the widget.
    """

    def __init__(self, parent=None, *args, **kwargs):
        """Initializes the ElideLineEdit widget."""
        super().__init__(parent, *args, **kwargs)
        self.elide_mode = Qt.TextElideMode.ElideMiddle
        self._original_text = ""

    def elide_text(self) -> str:
        """Elides the text to fit within the widget's width."""
        fm = QFontMetrics(self.font())
        return fm.elidedText(self._original_text, self.elide_mode, self.width())

    def setText(self, a0: str) -> None:
        """Sets the text on the widget, eliding it if necessary."""
        self._original_text = a0  # Directly set the original text
        self._update_text()

    def text(self):
        """Returns the original (non-elided) text."""
        return self._original_text

    def resizeEvent(self, event) -> None:
        """Handles the resize event of the widget by eliding and setting the text."""
        self._update_text()
        super().resizeEvent(event)

    def _update_text(self):
        """Updates the displayed text with an elided version if necessary."""
        text_elided = self.elide_text()
        super().setText(text_elided)


class LinuxDesktopFileView(QMainWindow):
    """Manage the Linux Desktop File View.

    This class represents the main window for the Ubuntu Desktop File.
    It provides various widgets for entering and displaying information related to the desktop file.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Linux Desktop File"
        self.resize(842, 390)
        self.setWindowTitle(f"{self.title} {__version__}")
        button_icon = QIcon(ldft.resource_path("Assets/Images/loupe.png"))
        button_categories = QIcon(
            ldft.resource_path("Assets/Images/directory_icon.png")
        )
        no_icon = QPixmap(ldft.resource_path("Assets/Images/No_icon.png"))
        self.setWindowIcon(QIcon(ldft.resource_path("Assets/Images/Linux.png")))
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 842, 390))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # Widgets Name
        self.label_name = QLabel(self.gridLayoutWidget)
        self.label_name.setText("Application Name :")
        self.gridLayout.addWidget(self.label_name, 0, 0)
        self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1)
        # Widgets Generic Name
        self.label_generic_name = QLabel(self.gridLayoutWidget)
        self.label_generic_name.setText("Generic Name :")
        self.gridLayout.addWidget(self.label_generic_name, 1, 0)
        self.lineEdit_generic_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_generic_name.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_generic_name, 1, 1)
        # Widgets Comment
        self.label_comment = QLabel(self.gridLayoutWidget)
        self.label_comment.setText("Comment :")
        self.gridLayout.addWidget(self.label_comment, 2, 0)
        self.lineEdit_comment = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_comment.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_comment, 2, 1)
        # Widgets Exec
        self.label_exec = QLabel(self.gridLayoutWidget)
        self.label_exec.setText("Exec :")
        self.gridLayout.addWidget(self.label_exec, 3, 0)
        self.lineEdit_exec = ElideLineEdit(self.gridLayoutWidget)
        self.lineEdit_exec.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_exec, 3, 1)
        self.pushButton_exec = QPushButton(self.gridLayoutWidget)
        self.pushButton_exec.setIcon(button_icon)
        self.pushButton_exec.setFixedSize(24, 24)
        self.gridLayout.addWidget(
            self.pushButton_exec, 3, 2, 
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        # Widgets Icon
        self.label_icon = QLabel(self.gridLayoutWidget)
        self.label_icon.setText("Icon :")
        self.gridLayout.addWidget(self.label_icon, 4, 0)
        self.lineEdit_icon = ElideLineEdit(self.gridLayoutWidget)
        self.lineEdit_icon.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_icon, 4, 1)
        self.pushButton_icon = QPushButton(self.gridLayoutWidget)
        self.pushButton_icon.setIcon(button_icon)
        self.pushButton_icon.setFixedSize(24, 24)
        self.gridLayout.addWidget(
            self.pushButton_icon, 4, 2, 
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        # Widgets Type
        self.label_type = QLabel(self.gridLayoutWidget)
        self.label_type.setText("Type :")
        self.gridLayout.addWidget(self.label_type, 5, 0, 1, 1)
        self.lineEdit_type = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_type.setText("Application")
        self.lineEdit_type.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_type, 5, 1, 1, 1)
        # Widgets Version
        self.label_version = QLabel(self.gridLayoutWidget)
        self.label_version.setText("Version :")
        self.gridLayout.addWidget(self.label_version, 6, 0)
        self.lineEdit_version = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_version.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_version, 6, 1)
        # Widgets Categories
        self.label_categories = QLabel(self.gridLayoutWidget)
        self.label_categories.setText("Categories :")
        self.gridLayout.addWidget(self.label_categories, 7, 0)
        self.lineEdit_categories = ElideLineEdit(self.gridLayoutWidget)
        self.lineEdit_categories.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_categories, 7, 1)
        self.pushButton_categories = QPushButton(self.gridLayoutWidget)
        self.pushButton_categories.setIcon(button_categories)
        self.pushButton_categories.setFixedSize(24, 24)
        self.gridLayout.addWidget(
            self.pushButton_categories, 7, 2, 
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        # Widgets Teminal
        self.label_terminal = QLabel(self.gridLayoutWidget)
        self.label_terminal.setText("Terminal :")
        self.gridLayout.addWidget(self.label_terminal, 8, 0)
        self.checkBox_terminal = QCheckBox(self.gridLayoutWidget)
        self.checkBox_terminal.setText("False")
        self.checkBox_terminal.setStyleSheet("color: gray")
        self.gridLayout.addWidget(self.checkBox_terminal, 8, 1)
        # Widgets Directory
        self.label_directory = QLabel(self.gridLayoutWidget)
        self.label_directory.setText("Path Directory :")
        self.gridLayout.addWidget(self.label_directory, 9, 0)
        self.checkBox_directory = QCheckBox(self.gridLayoutWidget)
        self.checkBox_directory.setStyleSheet("color: gray")
        self.gridLayout.addWidget(self.checkBox_directory, 9, 1)
        # Widgets Startup
        self.label_startup = QLabel(self.gridLayoutWidget)
        self.label_startup.setText("Startup Notify :")
        self.gridLayout.addWidget(self.label_startup, 10, 0)
        self.checkBox_startup = QCheckBox(self.gridLayoutWidget)
        self.checkBox_startup.setText("False")
        self.checkBox_startup.setStyleSheet("color: gray")
        self.gridLayout.addWidget(self.checkBox_startup, 10, 1)
        # Widget Python
        self.label_python = QLabel(self.gridLayoutWidget)
        self.label_python.setText("Launch with Python : ")
        self.gridLayout.addWidget(self.label_python, 11, 0)
        self.checkBox_python = QCheckBox(self.gridLayoutWidget)
        self.checkBox_python.setStyleSheet("color: gray")
        self.gridLayout.addWidget(self.checkBox_python, 11, 1)
        # Widget Label_icon
        self.label_icon_application = QLabel(self)
        self.label_icon_application.setFrameShape(QFrame.Shape.Panel)
        self.label_icon_application.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_icon_application.setFixedSize(60, 60)
        self.label_icon_application.setScaledContents(True)
        self.label_icon_application.setPixmap(no_icon)
        self.gridLayout.addWidget(
            self.label_icon_application, 0, 2, 2, 2,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )
        # Widget Save
        self.pushButton_save = QPushButton(self)
        self.pushButton_save.setText("Save")
        self.pushButton_save.setFixedSize(68, 32)
        self.gridLayout.addWidget(
            self.pushButton_save, 12, 1, 
            alignment=Qt.AlignmentFlag.AlignRight
        )
        # Widget Quit
        self.pushButton_quit = QPushButton(self)
        self.pushButton_quit.setText("Quit")
        self.pushButton_quit.setFixedSize(68, 32)
        self.gridLayout.addWidget(self.pushButton_quit, 12, 2)
        self.setCentralWidget(self.gridLayoutWidget)
        # Show Ui
        self.show()
