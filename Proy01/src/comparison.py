import numpy as np
import matplotlib.pyplot as plt

from transformations import gain_bias_transformation, gamma_correction, histogram_equalize

@save_plot
def gain_bias_comparison(
        image: np.ndarray, 
        filename: str, 
        gain: float, 
        bias: float,
        channels: list[int] | None = None,
    ) -> tuple[plt.Figure, str]:
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
    axes[1].set_title(f"Imagen Gain-Bias (c={gain:.2f}, b={bias:.2f})")

    return fig, f"gain_bias_{filename[:-4]}"

@save_plot
def gamma_correction_comparison(
        image: np.ndarray, 
        filename: str, 
        lower_gamma: float, 
        higher_gamma: float,
        channels: list[int] | None = None,
    ) -> tuple[plt.Figure, str]:
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

    return fig, f"gammas_{filename[:-4]}"

@save_plot
def histogram_equalize_comparison(
        image: np.ndarray, 
        filename: str,
        channels: list[int] | None = None,
    ) -> tuple[plt.Figure, str]:
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

    return fig, f"histogram_eq_{filename[:-4]}"

def plot_list_gain_bias(
        image: np.ndarray, 
        filename: str,
        gains: list[float],
        biases: list[float],
        channels: list[int] | None = None,
        save_fig: bool = True,
    ) -> None:
    """
    Función para generar varios 
    plots de transformaciones 
    gain-bias con base a dos listas 
    de valores.

    Opcionalmente puede guardar los 
    plots generados.
    """

    for gain, bias in zip(gains, biases):
        plot_gain_bias(image, filename, gain, bias, channels, save_fig)

@save_plot
def plot_gain_bias(
        image: np.ndarray, 
        filename: str, 
        gain: float,
        bias: float,
        channels: list[int] | None = None,
        save_fig: bool = True,
    ) -> tuple[plt.Figure, str | None]:
    """
    Función para generar el plot 
    de la imagen resultante de 
    aplicarle la transformación
    gain-bias con ciertos valores.

    Opcionalmente puede guardar 
    el plot creado.

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (4.5, 4.6),
    )
    axes.imshow(gain_bias_transformation(image, gain, bias, channels))
    axes.set_title(f"Trans. Gain-Bias con c={gain:.2f} y b={bias:.2f} en la Imagen {filename[-5]}")

    return fig, f"gain_bias_{gain:.2f}_{bias:.2f}_{filename[:-4]}" if save_fig else None

def plot_list_gammas_corrections(
        image: np.ndarray, 
        filename: str,
        gammas: list[float],
        channels: list[int] | None = None,
        save_fig: bool = True,
    ) -> None:
    """
    Función para generar varios 
    plots de correcciones gammas 
    con base a una lista de valores.

    Opcionalmente puede guardar los 
    plots generados.
    """

    for gamma in gammas:
        plot_gamma_correction(image, filename, gamma, save_fig)    

@save_plot
def plot_gamma_correction(
        image: np.ndarray, 
        filename: str, 
        gamma: float,
        channels: list[int] | None = None,
        save_fig: bool = True,
    ) -> tuple[plt.Figure, str | None]:
    """
    Función para generar el plot 
    de la imagen resultante de 
    aplicarle la corrección gamma 
    con un cierto valor.

    Opcionalmente puede guardar 
    el plot creado.

    Devuelve el plot diseñado.
    """

    fig, axes = plt.subplots(
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (4.5, 4.6),
    )
    axes.imshow(gamma_correction(image, gamma, channels=channels))
    axes.set_title(f"Corrección Gamma con gamma={gamma:.2f} en la Imagen {filename[-5]}")

    return fig, f"gamma_{gamma:.2f}_{filename[:-4]}" if save_fig else None