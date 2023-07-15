import sys

import matplotlib
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from components.Form import Form as FunctionForm
from components.MplCanvas import MplCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Function Plotter")

        layout = QVBoxLayout()
        self.function_form = FunctionForm(self)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.canvas, self)

        layout.addWidget(self.function_form)
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def plot_function(self):
        func, x_min, x_max = self.function_form.get_inputs()
        print(func, x_min, x_max)
        func = eval(f'lambda x: {func}')
        print(func)
        self.canvas.axes.clear()
        self.canvas.plot_function(func, x_min, x_max)


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
