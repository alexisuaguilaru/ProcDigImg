from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_images_dataset():
    """
    Función para cargar/leer las imágenes del dataset del proyecto. 
    Se cargan usando OpenCV y convertidas al formato RGB.

    Devuelve dos listas, una con las imágenes cargadas y otra 
    con los nombres de las imágenes.
    """

    base_path = Path("./dataset")
    images = []
    filenames =  []
    for path in base_path.iterdir():
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images.append(image)
        filenames.append(path.name[-5])
    return images, filenames

def initial_description(image: np.ndarray, filename: str) -> plt.Figure:
    """
    Función para graficar la imagen inicial. 
    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    axes.imshow(image, "gray")
    axes.set_title(f"Imagen {filename}")

    return fig