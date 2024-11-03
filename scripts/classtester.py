from src.Blackbody import Blackbody
import numpy as np

blackbody = Blackbody()

wavelength = 8  # Wavelength in micrometers
temperature = 200  # Temperature in Kelvin
exitance = blackbody.planck_exitance(wavelength, temperature)
print(f"Exitance: {exitance} W/m^2/sr/µm")

wavelength = 8  # Wavelength in micrometers
temperature = 200  # Temperature in Kelvin
radiance = blackbody.planck_radiance(wavelength, temperature)
print(f"Radiance: {radiance} W/m^2/sr/µm")

wavelengths = np.array([7, 8, 9, 10])  # Array of wavelengths in micrometers
rsr = np.array([0.1, 0.8, 0.5, 0.2])  # Array of relative spectral responses
temperature = 32  # Temperature in Celsius
band_radiance = blackbody.band_radiance(wavelengths, rsr, temperature)
print(f"Band Radiance: {band_radiance} W/m^2/sr")