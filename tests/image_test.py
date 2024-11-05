from src.cam_reader import CamReader
from src.image_proc import ThermalImageProcessor

# First read the thermal image
reader = CamReader("ThermalCam1")
image_data = reader.read("/Users/parkermei/Projects/Github/uas-thermal-cal/data/images/FLIR_70C/raw_0.hdr")

# Create image processor instance
processor = ThermalImageProcessor(image_data)

# Get statistics for a specific pixel
pixel_stats = processor.get_pixel_stats(50, 100)
print(f"Pixel mean: {pixel_stats.mean}")
print(f"Pixel std: {pixel_stats.std}")
#print(f"Channel values: {pixel_stats.channel_values}")

print(pixel_stats.channel_values.shape)

# Get mean image
mean_image = processor.get_mean_image()

print(mean_image.shape)

# Get statistics for a region
region_stats = processor.get_region_stats(50, 100, 50, 100)

print(region_stats['mean'])


#End of File