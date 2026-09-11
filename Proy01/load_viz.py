from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt

map_channels_name = {
    "R": "Rojo",
    "G": "Verde",
    "B": "Azul"
}

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
    presentarla en el formato RGB (original), a escala de grises 
    y la visualización de los diferentes canales de color (
    descomposición en canales).

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplot_mosaic(
        ".CCSS.\n"\
        "RRBBGG",
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 6),
    )
    fig.suptitle(f"Imagen Original, a Escala de Grises y Canales de la Imagen {filename[-5]}")

    axes["C"].imshow(image)
    axes["C"].set_title("Original")

    axes["S"].imshow(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), "gray")
    axes["S"].set_title("Escala de grises")

    for channel, (color, name) in enumerate(map_channels_name.items()):
        image_channel = np.zeros_like(image)
        image_channel[:, :, channel] = image[:, :, channel]
        axes[color].imshow(image_channel)
        axes[color].set_title(f"Canal {color} ({name})")

    return fig

def channels_histograms(image: np.ndarray, filename: str) -> plt.Figure:
    """
    Función para generar el plot con los histogramas 
    por cada canal de color de la imagen original. 

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        ncols = 3,
        subplot_kw = {
            "xlim": (0, 255),
        },
        figsize = (14, 4),
    )

    fig.suptitle(f"Histograma por Canales de la Imagen {filename[-5]} de Tamaño {image.shape[1]}px por {image.shape[0]}px (Ancho por Alto)")

    for channel, (color, name) in enumerate(map_channels_name.items()):
        intensities = image[:, :, channel].reshape(-1)
        axes[channel].hist(intensities, bins=256, color=color.lower())
        axes[channel].set_title(f"Canal {color} ({name})")

    return fig