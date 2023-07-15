from PySide2.QtCore import QRegExp
from PySide2.QtGui import QPalette, QColor, Qt, QRegExpValidator
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, \
    QDoubleSpinBox


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
        line_edit.setClearButtonEnabled(True)

        pattern = QRegExp("^-?[0-9]+[./]?[0-9]+$")
        input_validator = QRegExpValidator(pattern, line_edit)
        line_edit.setValidator(input_validator)

    def get_input(self):
        return float(self.widget.text())


class FunctionField(Field):
    def __init__(self, label: QLabel, line_edit: QLineEdit, parent=None):
        super(FunctionField, self).__init__(label, line_edit, parent)
        line_edit.setPlaceholderText("5*x^3 + 2*x")
        line_edit.setClearButtonEnabled(True)

        pattern = QRegExp("^[*x^0-9+-/]+$")
        input_validator = QRegExpValidator(pattern, line_edit)
        line_edit.setValidator(input_validator)





# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     window = QMainWindow()
#     window.setWindowTitle("My App")
#     window.setStyleSheet("background-color: white")
#     widget = FieldFactory.create_field(FieldFactory(), "TEXT", QLabel("Enter your text"), QLineEdit())
#     window.setCentralWidget(widget)
#     window.show()
#     app.exec_()
