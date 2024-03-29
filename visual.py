import numpy as np
import matplotlib.pyplot as plt

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

for f in ['', '_noimaging', '_noray_dust', '_noray_sour']:
    # Read in the model
    m = ModelOutput('tutorial_model' + f + '.rtout')

    # Extract the quantities
    g = m.get_quantities()

    # Get the wall positions in pc
    xw, yw = g.x_wall / pc, g.y_wall / pc

    # Make a 2-d grid of the wall positions (used by pcolormesh)
    X, Y = np.meshgrid(xw, yw)

    # Calculate the density-weighted temperature
    weighted_temperature =  np.sum(g['temperature'][0].array \
                               * g['density'][0].array, axis=2)\
                        / np.sum(g['density'][0].array, axis=2)

    # Make the plot
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    c = ax.pcolormesh(X, Y, weighted_temperature)
    ax.set_xlim(xw[0], xw[-1])
    ax.set_xlim(yw[0], yw[-1])
    ax.set_xlabel('x (pc)')
    ax.set_ylabel('y (pc)')
    cb = fig.colorbar(c)
    cb.set_label('Temperature (K)')
    fig.savefig('weighted_temperature_cartesian' + f + '.png', bbox_inches='tight')