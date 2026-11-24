from typing import Callable

import numpy as np
import matplotlib.pyplot as plt

from .filters import compose_notch_butterworth_filter

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
        fig, fig_name, *other_returns = create_plot(image, *args, **kwargs)
        if fig_name: fig.savefig(f"./results/{fig_name}.jpg", dpi=300, bbox_inches="tight")
        return fig, *other_returns
    
    return saver

@save_plot
def initial_description(
        image: np.ndarray, 
        fft_image: np.ndarray, 
        filename: str,
    ) -> tuple[plt.Figure, str]:
    """
    Función para graficar la imagen inicial 
    y su dominio de frecuencias. 
    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 4),
    )
    axes: list[plt.Axes]

    axes[0].imshow(image, "gray")
    axes[0].set_title("Imagen Original")

    log_fft = np.log10(np.abs(fft_image))
    axes[1].imshow(255*log_fft/log_fft.max(), "gray")
    axes[1].set_title("Dominio de Frecuencias")
    
    fig.suptitle(f"Visualización Inicial de la Imagen {filename}")

    return fig, f"img_{filename}_initial"

@save_plot
def visualize_filter(
        fft_image: np.ndarray, 
        filter: np.ndarray,
        filename: str,
    ) -> tuple[plt.Figure, str]:
    """
    Función para graficar el efecto 
    del filtrado por frecuencias y 
    mostrar la imagen resultante. 
    Devuelve el plot generado
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 4),
    )
    axes: list[plt.Axes]

    filter_fft = fft_image*filter
    log_fft = np.log1p(np.abs(filter_fft))
    axes[0].imshow(255*log_fft/log_fft.max(), "gray")
    axes[0].set_title("Dominio de Frecuencias Filtradas")

    filtered_img = np.fft.ifft2(filter_fft)
    filtered_img = np.abs(filtered_img).round().clip(0, 255)
    axes[1].imshow(filtered_img, "gray")
    axes[1].set_title("Imagen Resultante del Filtrado")
    
    fig.suptitle(f"Visualización la Imagen {filename} con Frecuencias Filtradas")

    return fig, f"img_{filename}_final", filtered_img

def apply_frequencies_filter(
        fft_image: np.ndarray, 
        filename: str,
        filter_parameters: list[tuple[tuple[int, int], float, int]]
    ) -> tuple[plt.Figure, np.ndarray]:
    """
    Función para aplicar filtrado de frecuencias 
    con filtros de Butterworth parametrizados 
    sobre el dominio de frecuencias de una imagen. 
    Devuelve el plot generado y la imagen resultante 
    del filtrado. 

    Toma de parámetros el dominio de frecuencias de 
    la imagen, su filename y las lista de parámetros 
    para la función `compose_notch_butterworth_filter`.
    """

    notch_butterworth_filter = compose_notch_butterworth_filter(
        fft_image.shape,
        filter_parameters
    )

    fig, filtered_image = visualize_filter(
        fft_image, 
        notch_butterworth_filter, 
        filename,
    )

    return fig, filtered_image