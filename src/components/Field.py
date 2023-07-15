from PySide2.QtCore import QRegExp
from PySide2.QtGui import QPalette, QColor, Qt, QRegExpValidator
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, \
    QDoubleSpinBox
from src.Utils import allowed_names

class Field(QWidget):
    def __init__(self, label: QLabel, w: QWidget, parent=None):
        super(Field, self).__init__(parent)
        layout = QHBoxLayout()

        self.label = label
        self.widget = w

        layout.addWidget(self.label)
        layout.addWidget(self.widget)

        self.setLayout(layout)

    def get_input(self):
        return self.widget.text()


class NumberField(Field):
    def __init__(self, label: QLabel, line_edit: QLineEdit, parent=None):
        super(NumberField, self).__init__(label, line_edit, parent)
        line_edit.setPlaceholderText("-10 or 3/4 \U0001D6D1")

        pattern = QRegExp("^-?[0-9]+[./]?[0-9]+$")
        input_validator = QRegExpValidator(pattern, line_edit)
        line_edit.setValidator(input_validator)


class FunctionField(Field):
    def __init__(self, label: QLabel, line_edit: QLineEdit, parent=None):
        super(FunctionField, self).__init__(label, line_edit, parent)
        self.line_edit = line_edit
        line_edit.setPlaceholderText("5*x^3 + 2*x")
        line_edit.setClearButtonEnabled(True)
        # pattern = QRegExp(f"^[*x^0-9+-/()\se]+$")
        # self.input_validator = QRegExpValidator(pattern, line_edit)
        # line_edit.setValidator(self.input_validator)

    def get(self) -> str:
        return self.line_edit.text()

    def append(self, text):
        self.line_edit.setText(self.line_edit.text() + text)

    def setFocus(self):
        self.line_edit.setFocus()
        self.line_edit.setCursorPosition(len(self.line_edit.text()))
