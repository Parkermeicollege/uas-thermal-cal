import numpy as np
from typing import Tuple, Optional, Union, List
from dataclasses import dataclass

@dataclass
class PixelStats:
    """
    Data class to hold pixel statistics
    
    Attributes:
        mean (float): Average value across all channels
        std (float): Standard deviation across channels
        min (float): Minimum value across channels
        max (float): Maximum value across channels
        channel_values (np.ndarray): Values for each channel
    """
    mean: float
    std: float
    min: float
    max: float
    channel_values: np.ndarray

class ThermalImageProcessor:
    """
    Class for processing thermal image data arrays.
    
    This class provides various image processing functions specifically
    designed for multi-channel thermal image data.
    """
    
    def __init__(self, image_data: np.ndarray):
        """
        Initialize the image processor with thermal image data.
        
        Args:
            image_data (np.ndarray): 3D numpy array of thermal image data
                                   (height, width, channels)
                                   
        Raises:
            ValueError: If image_data is not a 3D numpy array
        """
        if not isinstance(image_data, np.ndarray):
            raise ValueError("Image data must be a numpy array")
        
        if len(image_data.shape) != 3:
            raise ValueError("Image data must be 3D (height, width, channels)")
            
        self.image_data = image_data
        self.shape = image_data.shape
        self.num_channels = image_data.shape[2]
    
    def get_pixel_stats(self, row: int, col: int) -> PixelStats:
        """
        Calculate statistics for a specific pixel across all channels.
        
        Args:
            row (int): Row index of the pixel
            col (int): Column index of the pixel
            
        Returns:
            PixelStats: Statistics for the specified pixel
            
        Raises:
            ValueError: If coordinates are out of bounds
        """
        if not (0 <= row < self.shape[0] and 0 <= col < self.shape[1]):
            raise ValueError(f"Coordinates ({row}, {col}) out of bounds")
            
        pixel_values = self.image_data[row, col, :]
        
        return PixelStats(
            mean=float(np.mean(pixel_values)),
            std=float(np.std(pixel_values)),
            min=float(np.min(pixel_values)),
            max=float(np.max(pixel_values)),
            channel_values=pixel_values
        )
    
    def get_channel_image(self, channel: int) -> np.ndarray:
        """
        Extract a single channel from the image.
        
        Args:
            channel (int): Channel index to extract
            
        Returns:
            np.ndarray: 2D array of the specified channel
            
        Raises:
            ValueError: If channel index is out of bounds
        """
        if not (0 <= channel < self.num_channels):
            raise ValueError(f"Channel {channel} out of bounds")
            
        return self.image_data[:, :, channel]
    
    def get_mean_image(self) -> np.ndarray:
        """
        Calculate the mean image across all channels.
        
        Returns:
            np.ndarray: 2D array of mean values
        """
        return np.mean(self.image_data, axis=2)
    
    def get_region_stats(self, row_start: int, row_end: int, 
                        col_start: int, col_end: int) -> dict:
        """
        Calculate statistics for a rectangular region of the image.
        
        Args:
            row_start (int): Starting row index
            row_end (int): Ending row index
            col_start (int): Starting column index
            col_end (int): Ending column index
            
        Returns:
            dict: Dictionary containing region statistics
            
        Raises:
            ValueError: If coordinates are out of bounds
        """
        if not (0 <= row_start < row_end <= self.shape[0] and 
                0 <= col_start < col_end <= self.shape[1]):
            raise ValueError("Invalid region coordinates")
            
        region = self.image_data[row_start:row_end, col_start:col_end, :]
        
        return {
            'mean': np.mean(region),
            'std': np.std(region),
            'min': np.min(region),
            'max': np.max(region),
            'channel_means': np.mean(region, axis=(0, 1)),
            'spatial_mean': np.mean(region, axis=2)
        }
    
    def normalize_channels(self, 
                         method: str = 'minmax') -> np.ndarray:
        """
        Normalize the image data across channels.
        
        Args:
            method (str): Normalization method ('minmax' or 'zscore')
            
        Returns:
            np.ndarray: Normalized image data
        """
        if method not in ['minmax', 'zscore']:
            raise ValueError("Method must be 'minmax' or 'zscore'")
            
        normalized = np.zeros_like(self.image_data, dtype=np.float32)
        
        for channel in range(self.num_channels):
            channel_data = self.image_data[:, :, channel]
            
            if method == 'minmax':
                min_val = np.min(channel_data)
                max_val = np.max(channel_data)
                normalized[:, :, channel] = (channel_data - min_val) / (max_val - min_val)
            else:  # zscore
                mean_val = np.mean(channel_data)
                std_val = np.std(channel_data)
                normalized[:, :, channel] = (channel_data - mean_val) / std_val
                
        return normalized
#End of file