from src.cam_reader import CamReader

filepath = '/Users/parkermei/Projects/Github/uas-thermal-cal/data/images/FLIR_70C/raw_0.hdr'

reader = CamReader("test")

img = reader.read(filepath)

print(img.shape)
