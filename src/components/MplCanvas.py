import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

    def plot_function(self, func, x_min, x_max, num_points=1000):
        x = np.linspace(x_min, x_max, num_points)
        y = func(x)
        self.axes.plot(x, y)
        self.draw()
