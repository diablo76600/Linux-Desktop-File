# -*- Coding: utf-8 -*-
# Created by Diablo76 on 06/01/2024 -- 10:23:10.


from PyQt6.QtCore import QRect, Qt, QRectF
from PyQt6.QtGui import QIcon, QPainter, QFontMetrics, QPalette, QPen, QBrush, QColor, QResizeEvent
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QApplication
)

__version__: str = "1.0.9"



class LinuxDesktopFileView(QMainWindow):
    """Manage the Linux Desktop File View.

    This class represents the main window for the Ubuntu Desktop File.
    It provides various widgets for entering and displaying information related to the desktop file."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Linux Desktop File"
        self.setWindowTitle(f"{self.title} {__version__}")
        button_icon = QIcon("Assets/Images/loupe.png")
        button_categories = QIcon("Assets/Images/directory_icon.png")
        self.resize(842, 390)
        self.setWindowIcon(QIcon("Assets/Images/Linux.png"))
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
        self.lineEdit_exec = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_exec.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_exec, 3, 1)
        self.pushButton_exec = QPushButton(self.gridLayoutWidget)
        self.pushButton_exec.setIcon(button_icon)
        self.pushButton_exec.setFixedSize(24, 24)
        self.gridLayout.addWidget(self.pushButton_exec, 3, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        # Widgets Icon
        self.label_icon = QLabel(self.gridLayoutWidget)
        self.label_icon.setText("Icon :")
        self.gridLayout.addWidget(self.label_icon, 4, 0)
        self.lineEdit_icon = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_icon.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_icon, 4, 1)
        self.pushButton_icon = QPushButton(self.gridLayoutWidget)
        self.pushButton_icon.setIcon(button_icon)
        self.pushButton_icon.setFixedSize(24, 24)
        self.gridLayout.addWidget(self.pushButton_icon, 4, 2, alignment=Qt.AlignmentFlag.AlignCenter)
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
        self.lineEdit_categories = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_categories.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_categories, 7, 1)
        self.pushButton_categories = QPushButton(self.gridLayoutWidget)
        self.pushButton_categories.setIcon(button_categories)
        self.pushButton_categories.setFixedSize(24, 24)
        self.gridLayout.addWidget(self.pushButton_categories, 7, 2, alignment=Qt.AlignmentFlag.AlignCenter)
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
        self.label_icon_application.setFixedSize(60, 60)
        self.label_icon_application.setScaledContents(True)
        self.gridLayout.addWidget(self.label_icon_application, 0, 2, 2, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        # Widget Save
        self.pushButton_save = QPushButton(self)
        self.pushButton_save.setText("Save")
        self.pushButton_save.setFixedSize(68, 32)
        self.gridLayout.addWidget(self.pushButton_save, 12, 1, alignment=Qt.AlignmentFlag.AlignRight)
        # Widget Quit
        self.pushButton_quit = QPushButton(self)
        self.pushButton_quit.setText("Quit")
        self.pushButton_quit.setFixedSize(68, 32)
        self.gridLayout.addWidget(self.pushButton_quit, 12, 2)
        self.setCentralWidget(self.gridLayoutWidget)
        # Show Ui
        self.show()

    def resizeEvent(self, event) -> None:
        elide_mode = Qt.TextElideMode.ElideMiddle
        for line_edit in self.gridLayoutWidget.findChildren(QLineEdit):
            if line_edit.property("original_text"):
                fm = QFontMetrics(line_edit.font())
                elided_text = fm.elidedText(line_edit.property("original_text"), elide_mode, line_edit.width())
                line_edit.setText(elided_text)

