import numpy
import matplotlib.pyplot

x = numpy.arange(-numpy.pi, numpy.pi, 0.1)
y1 = numpy.sin(x)
y2 = numpy.sin(2*x)
fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=1)
ax.plot(x, y1, marker='+', markersize=6,
        color='green', linewidth=2, label='y=sin(x)')
ax.plot(x, y2, marker='o', markersize=6,
        color='cyan', linewidth=2, label='y=sin(2x)')
ax.grid(True)
ax.set_xlabel('temps(s)')
ax.set_ylabel('tension(V)')
ax.set_title('Graphique avec matplot')
ax.legend(loc='lower center')
matplotlib.pyplot.show()
