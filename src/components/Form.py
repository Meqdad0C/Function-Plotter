from src.components.FieldFactory import FieldFactory
from PySide2.QtWidgets import QLabel, QLineEdit, QGroupBox, QVBoxLayout, QHBoxLayout


class Form(QGroupBox):
    def __init__(self, parent=None) -> QGroupBox:
        super(Form, self).__init__(parent)

        self.setTitle("Function Input")
        self.setContentsMargins(10, 10, 10, 10)

        field_layout = QVBoxLayout()
        min_max_layout = QHBoxLayout()
        self.field_factory = FieldFactory()

        self.function_field = self.field_factory.create_function_field("function_field", QLabel("Function of x:"),
                                                                       QLineEdit())
        self.min_field = self.field_factory.create_number_field("min_val", QLabel("Min value of x:"), QLineEdit())
        self.max_field = self.field_factory.create_number_field("max_val", QLabel("Max value of x:"), QLineEdit())

        min_max_layout.addWidget(self.min_field)
        min_max_layout.addWidget(self.max_field)

        field_layout.addWidget(self.function_field)
        field_layout.addLayout(min_max_layout)

        self.setLayout(field_layout)

        self.setStyleSheet("QGroupBox { border: 1px solid red; border-radius: 3px; margin-top: 0.5em; }")


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    window = QMainWindow()
    form = Form()
    window.setCentralWidget(form)
    window.show()
    sys.exit(app.exec_())
