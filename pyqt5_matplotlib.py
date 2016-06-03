# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:19:20 2016

@author: marioromero
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt

# a figure instance to plot on
self.figure = plt.figure()
# this is the Canvas Widget that displays the figure
# it takes the figure instance as a parameter to __init__
self.canvas = FigureCanvas(self.figure)

# create an axis
ax = self.figure.add_subplot(111)
# discards the old graph
ax.hold(False)
# plot data
ax.plot(data, "*-")
# refresh canvas
self.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()