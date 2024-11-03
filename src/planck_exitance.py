import numpy as np

class Planck:
    """
    A class for calculating blackbody radiation using Planck's law.
    """

    def __init__(self):
        """
        Initialize the Planck object with physical constants.
        """
        self.h = 6.62607015e-34  # Planck's constant
        self.c = 299792458  # Speed of light
        self.k = 1.380649e-23  # Boltzmann constant

    def exitance(self, wavelength, temperature):
        """
        Calculate the exitance of a blackbody.

        Parameters:
        wavelength: Wavelength in micrometers.
        temperature: Temperature in Kelvin.

        Returns:
        Exitance in W/m^2/sr/µm.
        """
        wavelength = wavelength * 1e-6  # Convert wavelength to meters
        c1 = 2 * np.pi * self.h * self.c**2
        c2 = self.h * self.c / (self.k * temperature * wavelength)
        numerator = c1
        denominator = wavelength**5 * (np.exp(c2) - 1)
        return (numerator / denominator) * 10e-7

planck_calculator = Planck()
exitance = planck_calculator.exitance(8, 200)