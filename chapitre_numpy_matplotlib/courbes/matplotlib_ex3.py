import numpy
import matplotlib.pyplot

x = numpy.arange(-numpy.pi, numpy.pi, 0.1)
x.shape = (x.shape[0], 1)
y = numpy.hstack((numpy.sin(x), numpy.sin(2*x)))
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
courbe = ax.plot(x, y, markersize=6, linewidth=2)
courbe[0].set_marker('+')
courbe[0].set_color('green')
courbe[1].set_marker('o')
courbe[1].set_color('cyan')
ax.grid(True)
ax.set_xlabel('temps(s)')
ax.set_ylabel('tension(V)')
ax.set_title('Graphique avec matplot')
ax.legend(['sin(x)', 'sin(2x)'], loc='lower center')
matplotlib.pyplot.show()
