from PySide2.QtGui import Qt
from PySide2.QtWidgets import QToolBar, QAction, QVBoxLayout, QWidget, QPushButton, QGridLayout
from src.Utils import allowed_names


class SideBar(QWidget):
    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)
        layout = QGridLayout()
        self.function_field = parent.function_form.function_field

        row = 0
        for i, name in enumerate(allowed_names):
            button_action = QPushButton(name)
            button_action.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px;")
            button_action.setFixedSize(60, 30)
            button_action.clicked.connect(self.onMyToolBarButtonClick)
            layout.addWidget(button_action, row, i % 3)
            if i % 3 == 2:
                row += 1

        self.setLayout(layout)

    def onMyToolBarButtonClick(self):
        self.function_field.append(self.sender().text())
        print("click", self.sender().text())

