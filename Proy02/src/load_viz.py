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
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        images.append(image)
        filenames.append(path.name)
    return images, filenames

def visual_describe_image(image: np.ndarray, filename: str) -> plt.Figure:
    """
    Genera el plot que describe visualmente una imagen al 
    presentarla en el formato RGB (original) y a escala de grises 
    
    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 3),
    )
    fig.suptitle(f"Imagen Original y a Escala de Grises Imagen {filename[-5]}")

    axes[0].imshow(image)
    axes[0].set_title("Original")

    axes[1].imshow(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), "gray")
    axes[1].set_title("Escala de grises")

    return fig