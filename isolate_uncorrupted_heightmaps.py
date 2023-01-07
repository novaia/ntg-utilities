import os
import keras
import cv2
import numpy as np

input_directory = 'C:/Users/Hayden/Desktop/split_heightmaps/'
output_directory = 'C:/Users/Hayden/Desktop/uncorrupted_heightmaps/'
batch_size = 32
image_size = 360

model = keras.models.load_model('data/corrupted_heightmap_discriminator.h5')

file_list = os.listdir(input_directory)

for i in range(int(len(file_list) / 32)):
    batch = []
    for k in range(batch_size):
        image = cv2.imread(input_directory + file_list[i + k], 0)
        image = cv2.resize(image, dsize = (image_size, image_size), interpolation = cv2.INTER_AREA)
        batch.append(image)

    batch = np.asarray(batch)
    output = model.predict(batch)

    for k in range(len(output)):
        if(output[k][1] > output[k][0]):
            cv2.imwrite(output_directory + file_list[i + k] + '.png', batch[k])
            print('Saving ' + file_list[i + k])