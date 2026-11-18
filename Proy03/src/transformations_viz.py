from typing import Callable

import numpy as np
import matplotlib.pyplot as plt

from .transformations import apply_affine_transformation

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
def plot_rotations(image: np.ndarray, filename: str, rotation_angles: list[float]) -> tuple[plt.Figure, str]:
    """
    Función para comparar diferentes rotaciones 
    sobre una misma imagen.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        nrows = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    for ax, rotation_angle in zip(axes.flatten(), rotation_angles):
        rotated_image = apply_affine_transformation(image, angle=rotation_angle)
        ax.imshow(rotated_image, "gray")
        ax.set_title(f"Ángulo de {np.rad2deg(rotation_angle):.2f}°")

    fig.suptitle(f"Comparación de Diferentes Rotaciones en la Imagen {filename}")

    return fig, f"img_{filename}_rotation"

@save_plot
def plot_translation(image: np.ndarray, filename: str, translations_moves: list[tuple[float, float]]) -> tuple[plt.Figure, str]:
    """
    Función para comparar diferentes traslaciones 
    sobre una misma imagen.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        nrows = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    for ax, (x_move, y_move) in zip(axes.flatten(), translations_moves):
        translated_image = apply_affine_transformation(image, x_move=x_move, y_move=y_move)
        ax.imshow(translated_image, "gray")
        ax.set_title(f"Traslación de ({x_move:.2f}, {y_move:.2f})")

    fig.suptitle(f"Comparación de Diferentes Traslaciones en la Imagen {filename}")

    return fig, f"img_{filename}_translation"

@save_plot
def plot_reflection(image: np.ndarray, filename: str) -> tuple[plt.Figure, str]:
    """
    Función para comparar las diferentes 
    reflexiones sobre una misma imagen.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        nrows = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    reflections = [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ]
    for ax, (reflect_x, reflect_y) in zip(axes.flatten(), reflections):
        translated_image = apply_affine_transformation(image, reflect_x=reflect_x, reflect_y=reflect_y)
        ax.imshow(translated_image, "gray")
        reflections = (["Eje Y"] if reflect_x else []) + (["Eje X"] if reflect_y else [])
        if reflections:
            reflection_axis = " y ".join(reflections)
            reflection_axis = ("los " if "y" in reflection_axis else "el ")+reflection_axis
            ax_title = f"Reflexión sobre {reflection_axis}"
        else:
            ax_title = "Sin reflexión"
        ax.set_title(ax_title)

    fig.suptitle(f"Comparación de Diferentes Traslaciones en la Imagen {filename}")

    return fig, f"img_{filename}_reflection"

@save_plot
def plot_scaling(image: np.ndarray, filename: str, scaling_factors: list[tuple[float, float]]) -> tuple[plt.Figure, str]:
    """
    Función para comparar diferentes escalamientos  
    sobre una misma imagen.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        nrows = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    for ax, (scale_x, scale_y) in zip(axes.flatten(), scaling_factors):
        scaled_image = apply_affine_transformation(image, scale_x=scale_x, scale_y=scale_y)
        ax.imshow(scaled_image, "gray")
        ax.set_title(f"Escalamiento de {scale_y:.2f} en\nEje X y {scale_x:.2f} en Eje Y")

    fig.suptitle(f"Comparación de Diferentes Escalamientos en la Imagen {filename}")

    return fig, f"img_{filename}_scaling"

@save_plot
def plot_affine_transformation(image: np.ndarray, filename: str, affine_transformations: list[dict[str, int|float|bool]]) -> tuple[plt.Figure, str]:
    """
    Función para comparar diferentes transformaciones 
    afines sobre una misma imagen.

    Devuelve el plot generado.
    """

    fig, axes = plt.subplots(
        ncols = 2,
        nrows = 2,
        subplot_kw = {
            "yticks": [],
            "xticks": [],
        },
        figsize = (8, 7),
    )

    for index_transformation, ax, affine_parameters in zip(range(1,5), axes.flatten(), affine_transformations):
        scaled_image = apply_affine_transformation(image, **affine_parameters)
        ax.imshow(scaled_image, "gray")
        ax.set_title(f"Transformación afín {index_transformation}")

    fig.suptitle(f"Comparación de Diferentes Transformaciones Afines en la Imagen {filename}")

    return fig, f"img_{filename}_affine"