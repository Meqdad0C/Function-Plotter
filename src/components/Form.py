from PySide2.QtGui import Qt

from src.components.FieldFactory import FieldFactory
from PySide2.QtWidgets import QLabel, QLineEdit, QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton
from src.Utils import parse_function


class Form(QGroupBox):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setTitle("Function Input")
        self.setContentsMargins(10, 10, 10, 10)

        field_layout = QVBoxLayout()
        field_layout.setAlignment(Qt.AlignTop)
        min_max_layout = QHBoxLayout()
        self.field_factory = FieldFactory()

        self.function_field = self.field_factory.create_function_field("function_field", QLabel("Function of x:"),
                                                                       QLineEdit())
        self.min_field = self.field_factory.create_number_field("min_val", QLabel("Min value of x:"), QLineEdit())
        self.max_field = self.field_factory.create_number_field("max_val", QLabel("Max value of x:"), QLineEdit())

        radio_layout = QHBoxLayout()
        radio_layout.setAlignment(Qt.AlignLeft)
        self.angle_label = QLabel("Angle:")
        self.angle = "radian"

        self.radian_radio = QRadioButton("Radian")
        self.degree_radio = QRadioButton("Degree")
        self.radian_radio.setChecked(True)
        self.radian_radio.toggled.connect(self.toggle_angle)
        radio_layout.addWidget(self.angle_label)
        radio_layout.addWidget(self.radian_radio)
        radio_layout.addWidget(self.degree_radio)

        self.plot_button = QPushButton("Plot")
        self.plot_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px;")
        self.plot_button.clicked.connect(parent.plot_function)

        min_max_layout.addWidget(self.min_field)
        min_max_layout.addWidget(self.max_field)

        field_layout.addWidget(self.function_field)
        field_layout.addLayout(min_max_layout)
        field_layout.addLayout(radio_layout)
        field_layout.addWidget(self.plot_button)

        self.setLayout(field_layout)
        self.setStyleSheet("QGroupBox { border: 1px solid red; border-radius: 3px; margin-top: 0.5em; }")

    def get_inputs(self):
        func, x_min, x_max = self.function_field.get_input(), self.min_field.get_input(), self.max_field.get_input()
        func = parse_function(func, self.angle)
        return func, x_min, x_max

    def toggle_angle(self):
        if self.angle == "radian":
            self.angle = "degree"
        else:
            self.angle = "radian"
        print(self.angle)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    window = QMainWindow()
    form = Form()
    window.setCentralWidget(form)
    window.show()
    sys.exit(app.exec_())
