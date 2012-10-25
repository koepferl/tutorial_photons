import numpy as np

from hyperion.model import Model
from hyperion.util.constants import pc, lsun

# Initialize model
m = Model()

# Set one-cell cartesian grid
w = np.linspace(-pc, pc, 32)
m.set_cartesian_grid(w, w, w)

# Add density grid with constant density
m.add_density_grid(np.ones(m.grid.shape) * 4.e-20, 'kmh_lite.hdf5')

# Add a point source in the center
s = m.add_point_source()
s.luminosity = 1000 * lsun
s.temperature = 6000.

# Add 10 SEDs for different viewing angles
image = m.add_peeled_images(sed=True, image=False)
image.set_wavelength_range(250, 0.01, 5000.)
image.set_viewing_angles(np.linspace(0., 90., 10), np.repeat(20., 10))
image.set_track_origin('basic')

# Add multi-wavelength image for a single viewing angle
image = m.add_peeled_images(sed=False, image=True)
image.set_wavelength_range(30, 1., 1000.)
image.set_viewing_angles([30.], [20.])
image.set_image_size(200, 200)
image.set_image_limits(-1.5 * pc, 1.5 * pc, -1.5 * pc, 1.5 * pc)

# Add a fly-around at 500 microns
image = m.add_peeled_images(sed=False, image=True)
image.set_wavelength_range(1, 499., 501.)
image.set_viewing_angles(np.repeat(45., 36), np.linspace(5., 355., 36))
image.set_image_size(200, 200)
image.set_image_limits(-1.5 * pc, 1.5 * pc, -1.5 * pc, 1.5 * pc)

# Set runtime parameters
m.set_n_initial_iterations(5)
m.set_raytracing(True)
m.set_n_photons(initial=1e6, imaging=1e7,
                raytracing_sources=0, raytracing_dust=1e6)

# Write out input file
m.write('tutorial_model.rtin')