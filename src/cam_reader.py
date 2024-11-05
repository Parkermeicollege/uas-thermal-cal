#Parker Mei pmm46300@rit.edu
import os
import numpy as np
import spectral.io.envi as envi
#spectral python is a library that can read in ENVI format headers and fiels

class CamReader:
    """
    Class for reading and processing Thermal Images from ENVI Files.
    """    
    def __init__(self, name: str) -> None:
        """
        Initialize the CamReader instance.
        
        Args:
            name (str): Identifier for the camera/reader instance
        
        Raises:
            ValueError: If name is empty or not a string
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")           
        self.name = name.strip()
        self.last_filepath = None
        self.metadata = None

    def validate_file(self, filepath: str) -> bool:
        """
        Validate if the file exists and has the correct format.
        
        Args:
            filepath (str): Path to the ENVI file
            
        Returns:
            bool: True if file is valid, False otherwise
            
        Raises:
            ValueError: If filepath is empty or not a string
        """
        if not isinstance(filepath, str) or not filepath.strip():
            raise ValueError("Filepath must be a non-empty string")           
        # Check if file exists
        if not os.path.exists(filepath):
            return False           
        # Check for accompanying .hdr file
        hdr_file = os.path.splitext(filepath)[0] + '.hdr'
        if not os.path.exists(hdr_file):
            return False            
        return True

    def read(self, filepath: str, validate: bool = True) -> np.ndarray:
        """
        Read thermal image from ENVI file and convert it into a numpy array.
        
        Args:
            filepath (str): Path to the ENVI file
            validate (bool): Whether to validate the file before reading
                            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file validation fails
            Exception: For other reading errors
        """
        try:
            if validate and not self.validate_file(filepath):
                raise ValueError(f"Invalid or missing file: {filepath}")                
            image = envi.open(filepath)
            self.last_filepath = filepath            
            # Convert to numpy array and ensure proper orientation
            data = image.load()            
            return data            
        except Exception as e:
            raise Exception(f"Error reading file {filepath}: {str(e)}")
#End of File