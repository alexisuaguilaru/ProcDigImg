import numpy as np
import matplotlib.pyplot as plt

from transformations import gain_bias_transformation, gamma_correction, histogram_equalize

def gain_bias_comparison(
        image: np.ndarray, 
        filename: str, 
        gain: float, 
        bias: float,
        channels: list[int] | None = None,
    ) -> plt.Figure:
    """
    Función para comparar visualmente los 
    efecto de aplicar un gain y bias.

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (10, 4.5),
    )

    fig.suptitle(f"Comparativa de Usar Gain-Bias en la Imagen {filename[-5]}")

    axes[0].imshow(image)
    axes[0].set_title("Imagen original")

    axes[1].imshow(gain_bias_transformation(image, gain, bias, channels))
    axes[1].set_title(f"Imagen Gain-Bias")

    return fig

def gamma_correction_comparison(
        image: np.ndarray, 
        filename: str, 
        lower_gamma: float, 
        higher_gamma: float,
        channels: list[int] | None = None,
    ) -> plt.Figure:
    """
    Función para comparar visualmente los efectos 
    de correcciones gammas con diferentes valores.

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        ncols = 3,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (14, 4),
    )

    fig.suptitle(f"Comparativa de Diferentes Correcciones Gamma en la Imagen {filename[-5]}")

    axes[0].imshow(gamma_correction(image, lower_gamma, channels=channels))
    axes[0].set_title(f"Gamma igual a {lower_gamma:.2f}")

    axes[1].imshow(image)
    axes[1].set_title("Imagen original (Sin corrección)")

    axes[2].imshow(gamma_correction(image, higher_gamma, channels=channels))
    axes[2].set_title(f"Gamma igual a {higher_gamma:.2f}")

    return fig

def histogram_equalize_comparison(
        image: np.ndarray, 
        filename: str,
        channels: list[int] | None = None,
    ) -> plt.Figure:
    """
    Función para comparar visualmente los efectos 
    de la ecualización por histograma.

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (10, 4.5),
    )

    fig.suptitle(f"Comparativa de la Ecualización por Histograma en la Imagen {filename[-5]}")

    axes[0].imshow(image)
    axes[0].set_title("Imagen original")

    axes[1].imshow(histogram_equalize(image, channels))
    axes[1].set_title(f"Imagen ecualizada")

    return fig