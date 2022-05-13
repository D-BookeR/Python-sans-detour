import numpy
import matplotlib.pyplot

x = numpy.arange(-numpy.pi, numpy.pi, 0.1)
y = numpy.sin(x)
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
ax.plot(x, y, marker='+', markersize=6, color='green', linewidth=2, label='y=sin(x)')
ax.grid(True)
ax.set_xlabel('temps(s)')
ax.set_ylabel('tension(V)')
ax.set_title('Graphique avec matplot')
ax.legend(loc='lower right')
matplotlib.pyplot.show()
