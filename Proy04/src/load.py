from pathlib import Path

import cv2
import numpy as np

def load_images_dataset():
    """
    Función para cargar/leer las imágenes del dataset del proyecto. 
    Se cargan usando OpenCV y convertidas al formato a escala de grises.

    Devuelve tres listas, una con las imágenes cargadas, una 
    con los nombres de las imágenes y otra con el dominio 
    de frecuencias por FFT.
    """

    base_path = Path("./dataset")
    images = []
    filenames =  []
    ftts = []
    for path in base_path.iterdir():
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frequencies = np.fft.fft2(image.astype(float))
        frequencies = np.fft.fftshift(frequencies)
        images.append(image)
        filenames.append(path.name[-5])
        ftts.append(frequencies)
    return images, filenames, ftts