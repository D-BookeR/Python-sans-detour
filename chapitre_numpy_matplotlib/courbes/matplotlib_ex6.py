import numpy
import matplotlib.pyplot

x = numpy.arange(-numpy.pi, numpy.pi, 0.1)
freq = numpy.array([[1.1], [2.1], [3.1], [4.1], [5.1]])
y = numpy.sin(freq * x)
fig, ax = matplotlib.pyplot.subplots(nrows=2, ncols=3)
for ind, val_freq in enumerate(freq):
    ind_lig = ind // 3
    ind_col = ind % 3
    ax[ind_lig, ind_col].plot(x, y[ind, :],
                              marker='+',
                              label='y=sin(' + str(val_freq[0]) + 'x)')
    ax[ind_lig, ind_col].grid(True)
    ax[ind_lig, ind_col].set_xlabel('temps(s)')
    ax[ind_lig, ind_col].set_ylabel('tension(V)')
    lig_col = '(' + str(ind_lig) + ', ' + str(ind_col) + ')'
    ax[ind_lig, ind_col].set_title('Graphique index ' + lig_col)
    ax[ind_lig, ind_col].legend(loc='lower right')
fig.suptitle("Plusieurs graphiques")
fig.delaxes(ax[1, 2])
matplotlib.pyplot.show()
