import rasterio
import matplotlib.pyplot as plt

image_name = 'n00_w058_1arc_v3'
image = rasterio.open(image_name + '.tif')
plt.imsave(image_name + '.png', image.read(1), cmap='gray')