import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

for f in ['', '_noimaging', '_noray_dust', '_noray_sour', '_fewinitials']:
    print f
    m = ModelOutput('tutorial_model' + f + '.rtout')

    fig = plt.figure()
    plt.title((f))
    ax = fig.add_subplot(1, 1, 1)
    

    # Direct stellar photons
    if f in ['', '_noimaging', '_noray_dust', '_fewinitials']:
        wav, nufnu = m.get_sed(inclination='all', aperture=-1, distance=300 * pc,
                       component='source_emit')

        # Plot SED for each inclination
        for i in range(nufnu.shape[0]):
            ax.loglog(wav, nufnu[i, :], color='blue')

    # Scattered stellar photons
    wav, nufnu = m.get_sed(inclination='all', aperture=-1, distance=300 * pc,
                       component='source_scat')
    # Plot SED for each inclination
    for i in range(nufnu.shape[0]):
        ax.loglog(wav, nufnu[i, :], color='teal')

    # Direct dust photons
    wav, nufnu = m.get_sed(inclination='all', aperture=-1, distance=300 * pc,
                       component='dust_emit')
    # Plot SED for each inclination
    for i in range(nufnu.shape[0]):
        ax.loglog(wav, nufnu[i, :], color='red')

    # Scattered dust photons
    wav, nufnu = m.get_sed(inclination='all', aperture=-1, distance=300 * pc,
                       component='dust_scat')
    # Plot SED for each inclination
    for i in range(nufnu.shape[0]):
        ax.loglog(wav, nufnu[i, :], color='orange')
        


    # Direct stellar photon
    if f in ['', '_noimaging', '_noray_dust']:
        wav, nufnu = m.get_sed(inclination=0, aperture=-1, distance=300 * pc,
                       component='source_emit')
        ax.loglog(wav, nufnu, color='blue', label='Direct stellar photons')

    # Scattered stellar photons
    wav, nufnu = m.get_sed(inclination=0, aperture=-1, distance=300 * pc,
                       component='source_scat')
    ax.loglog(wav, nufnu, color='teal', label='Scattered stellar photons')

    # Direct dust photons
    wav, nufnu = m.get_sed(inclination=0, aperture=-1, distance=300 * pc,
                       component='dust_emit')
    ax.loglog(wav, nufnu, color='red', label='Direct dust photons')

    # Scattered dust photons
    wav, nufnu = m.get_sed(inclination=0, aperture=-1, distance=300 * pc,
                       component='dust_scat')
    ax.loglog(wav, nufnu, color='orange', label='Scattered dust photons')



    ax.set_xlabel(r'$\lambda$ [$\mu$m]')
    ax.set_ylabel(r'$\lambda F_\lambda$ [ergs/s/cm$^2$]')
    ax.set_xlim(0.1, 5000.)
    ax.set_ylim(1.e-12, 2.e-5)
    ax.legend(loc='upper left')
    fig.savefig('sed_all_origin' + f +'.png')