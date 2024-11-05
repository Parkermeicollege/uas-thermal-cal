from src.cam_reader import CamReader

#Filepath to thermal images
filepath = '/Users/parkermei/Projects/Github/uas-thermal-cal/data/images/FLIR_70C/raw_0.hdr'

# Create Cam Reader Instance and name it
reader = CamReader("test")

# Img is the thermal image 
img = reader.read(filepath)

#Print the shape of the thermal image
print(img.shape)
