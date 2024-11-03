import numpy as np
import pandas as pd

from src.Blackbody import Blackbody


blackbody = Blackbody()

Wavelength = 8  # Wavelength in micrometers
Temperature = 200  # Temperature in Kelvin
exitance = blackbody.planck_exitance(Wavelength, Temperature)
print(f"Exitance: {exitance} W/m^2/sr/µm")

Wavelength = 8  # Wavelength in micrometers
Temperature = 200  # Temperature in Kelvin
radiance = blackbody.planck_radiance(Wavelength, Temperature)
print(f"Radiance: {radiance} W/m^2/sr/µm")

#Enter CSV Path of the RSR File
csv_path = '/Users/parkermei/Projects/Github/uas-thermal-cal/data/cam_sheets/flir_rsr.csv'
#Convert the csv into a pandas dataframe
Datasheet = pd.read_csv(csv_path, sep=',', header=0)

#Convert wavelengths into np array
wavelength = Datasheet['Wavelength (µm)']
wavelengths = wavelength.to_numpy()
#Convert rsr into np array
rsr = Datasheet['Relative response']
rsr = rsr.to_numpy()

Temperature = 32  # Temperature in Celsius
band_radiance = blackbody.band_radiance(wavelengths, rsr, Temperature)
print(f"Band Radiance: {band_radiance} W/m^2/sr")