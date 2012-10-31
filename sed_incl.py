import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

for f in ['', '_noimaging', '_noray_dust', '_noray_sour', '_fewinitials']:

    m = ModelOutput('tutorial_model' + f + '.rtout')

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Extract all SEDs
    wav, nufnu = m.get_sed(inclination='all', aperture=-1, distance=300 * pc)

    # Plot SED for each inclination
    for i in range(nufnu.shape[0]):
        ax.loglog(wav, nufnu[i, :], color='black')

    ax.set_xlabel(r'$\lambda$ [$\mu$m]')
    ax.set_ylabel(r'$\lambda F_\lambda$ [ergs/s/cm$^2$]')
    ax.set_xlim(0.1, 5000.)
    ax.set_ylim(1.e-12, 2.e-6)
    fig.savefig('sed' + f + '.png')