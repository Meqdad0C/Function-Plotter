import sys

import matplotlib
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QGridLayout, QMessageBox
from src.components.Form import Form as FunctionForm
from src.components.MplCanvas import MplCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from src.Utils import eval_function, validate_function
from src.components.SideBar import SideBar

matplotlib.use('Qt5Agg')


def show_error(message):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(f"Invalid input{message}")
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Function Plotter")

        layout = QVBoxLayout()
        H_layout = QHBoxLayout()

        self.function_form = FunctionForm(self)
        H_layout.addWidget(self.function_form)
        H_layout.addWidget(SideBar(self))
        H_layout.setAlignment(Qt.AlignTop)

        V_layout = QVBoxLayout()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.canvas, self)
        V_layout.addWidget(toolbar)
        V_layout.addWidget(self.canvas)

        layout.addLayout(H_layout)
        layout.addLayout(V_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def plot_function(self):
        try:
            func, x_min, x_max = self.function_form.get_inputs()
            func, x_min, x_max = validate_function(func, x_min, x_max)
        except BaseException as e:
            show_error(e)
            return
        self.canvas.axes.clear()
        self.canvas.plot_function(func, x_min, x_max)


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
