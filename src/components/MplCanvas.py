import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

    def plot_function(self, func, x_min, x_max, num_points=1000, type='normal'):
        if type == 'normal':
            x = np.linspace(x_min, x_max, num_points)
            y = func(x)
            if np.shape(y) != np.shape(x):
                y = np.linspace(y, y, num_points)
            self.axes.plot(x, y, 'r')
        elif type == 'pi':
            x = np.linspace(-2 * np.pi, np.pi * 2, num_points)
            y = func(x)
            if np.shape(y) != np.shape(x):
                y = np.linspace(y, y, num_points)
            radian_multiples = [-2, -3 / 2, -1, -1 / 2, 0, 1 / 2, 1, 3 / 2, 2]
            radians = [n * np.pi for n in radian_multiples]
            radian_labels = ['$-2\pi$', '$-3\pi/2$', '$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
            self.axes.set_xticks(radians, radian_labels)
            self.axes.plot(x, y, 'r')
        self.draw()
