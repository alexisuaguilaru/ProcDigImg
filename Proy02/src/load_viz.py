from pathlib import Path
from typing import Callable, Literal

import cv2
import numpy as np
import matplotlib.pyplot as plt

from .filters import TypeFilters

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
        filenames.append(path.name[-5])
    return images, filenames

def save_plot(
        create_plot: Callable[[np.ndarray, str], tuple[plt.Figure, str | None]]
    ) -> Callable:
    """
    Función para guardar un plot diseñado o 
    creado. Se espera que la función decorada 
    devuelva el objeto Figure y el nombre de 
    la figura.

    Devuelve el plot creado.
    """

    def saver(image: np.ndarray, *args, **kwargs) -> plt.Figure:
        fig, fig_name = create_plot(image, *args, **kwargs)
        if fig_name: fig.savefig(f"./results/{fig_name}.jpg", dpi=300, bbox_inches="tight")
        return fig
    
    return saver

@save_plot
def visual_describe_plot(image: np.ndarray, filename: str) -> tuple[plt.Figure, str]:
    """
    Función para describir visualmente una imagen 
    mostrando su versión original y a escala de grises.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 3),
    )

    axes[0].imshow(image)
    axes[1].imshow(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), "gray")

    fig.suptitle(f"Imagen Original y a Escala de Grises de la Imagen {filename.replace("_", " ")}")

    return fig, f"describe_{filename}"

@save_plot
def orientation_borders_plot(
        image: np.ndarray, 
        filename: str, 
        type_filter: Literal["prewitt", "sobel", "laplacian_1", "laplacian_2", "laplacian_gaussian"],
    ) -> tuple[plt.Figure, str]:
    """
    Función para mostrar la orientación 
    de los bordes presentes en una 
    imagen. Se puede escoger el tipo de 
    filtro que se empleará para calcular 
    los gradientes direccionales.

    Devuelve el plot diseñado.
    """
    filter_horizontal, filter_vertical = TypeFilters.get_filter(type_filter)

    gradient_x = cv2.filter2D(image.astype(float), -1, filter_horizontal, borderType=0)
    gradient_y = cv2.filter2D(image.astype(float), -1, filter_vertical, borderType=0)
    magnitude = np.sqrt(gradient_x**2+gradient_y**2+1e-32)
    gradient_x /= magnitude
    gradient_y /= magnitude

    meshgrid_x = np.linspace(0, image.shape[1]-1, image.shape[1], dtype=int)
    meshgrid_y = np.linspace(image.shape[0]-1, 0, image.shape[0], dtype=int)
    meshgrid_x, meshgrid_y = np.meshgrid(meshgrid_x, meshgrid_y)

    fig, axes = plt.subplots(
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (5, 4),
    )

    axes.quiver(meshgrid_x, meshgrid_y, gradient_x, gradient_y)

    fig.suptitle(f"Orientación de los bordes de la Imagen {filename.replace("_", " ")}")

    return fig, f"orientation_{filename}"

@save_plot
def compare_filter_plot(
        image: np.ndarray, 
        filename: str, 
        type_filter: Literal["prewitt", "sobel", "laplacian_1", "laplacian_2", "laplacian_gaussian"] | Callable[[np.ndarray], np.ndarray],
        color: Literal["gray", None] = None,
    ) -> tuple[plt.Figure, str]:
    """
    Función para comparar la variante 
    vertical y horizontal de un cierto 
    filtro en una imagen.

    Devuelve el plot diseñado. 
    """

    if color:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    if isinstance(type_filter, str):
        function_filters = TypeFilters.get_functions(type_filter)
        
        if len(function_filters) == 2:
            fig, axes = plt.subplots(
                ncols = 2,
                subplot_kw = {
                    "yticks": [],
                    "xticks": [],
                },
                figsize = (8, 2.5),
            )

            filter_horizontal, filter_vertical = function_filters
            
            axes[0].imshow(filter_horizontal(image), color)
            axes[0].set_title("Versión Horizontal")
            
            axes[1].imshow(filter_vertical(image), color)
            axes[1].set_title("Versión Vertical")

        else:
            fig, axes = plt.subplots(
                ncols = 1,
                subplot_kw = {
                    "yticks": [],
                    "xticks": [],
                },
                figsize = (8, 2.5),
            )

            function_filter = function_filters[0]
            axes.imshow(function_filter(image), color)

        fig.suptitle(f"Comparación del Filtro {TypeFilters.get_name(type_filter)} de la Imagen {filename.replace("_", " ")}")
        
        return fig, f"filter_{type_filter}_{filename}"
    
    else:
        fig, axes = plt.subplots(
            ncols = 1,
            subplot_kw = {
                "yticks": [],
                "xticks": [],
            },
            figsize = (8, 2.5),
        )

        axes.imshow(type_filter(image), color)

        fig.suptitle(f"Comparación del Filtro Canny de la Imagen {filename.replace("_", " ")}")
        
        return fig, f"filter_canny_{filename}"