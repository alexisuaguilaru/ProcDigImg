from typing import Callable

import numpy as np

def image_limits_adjust(
        factor_scaling: float = 1,
    ) -> Callable:
    """
    Función para inicializar el decorador para 
    reajustar el rango de salida después de aplicarle 
    una transformación a una imagen de forma 
    que la intensidad de los colores estén en [0, 255]

    Devuelve el decorador para ajustar el rango de 
    colores de la imagen al aplicar un factor de escala.
    """

    def image_adjust_wrapper(transformation: Callable[[np.ndarray], np.ndarray]) -> Callable:

        def image_adjust(image: np.ndarray, *args, **kwargs) -> np.ndarray:
            transformed_image = transformation(image, *args, **kwargs)
            return (factor_scaling*transformed_image).round().astype(int).clip(0, 255)
        return image_adjust
    
    return image_adjust_wrapper

@image_limits_adjust()
def gain_bias_transformation(
        image: np.ndarray,
        gain_c: float,
        bias_b: float,
        channels: list[int] | None = None,
    ) -> np.ndarray:
    """
    Función para aplicar una ganancia (gain) y 
    un sesgo (bias). Esta función permite 
    ajustar el contraste con gain y el brillo 
    con el bias.
    """

    if not channels:
        transf_image = gain_c*image.astype(int)+bias_b
    else:
        transf_image = image.copy().astype(int)
        transf_image[:, :, channels] = gain_c*image[:, :, channels]+bias_b
    
    return transf_image

def negative_transformation(image: np.ndarray) -> np.ndarray:
    """
    Función para devolver el negativo de una imagen.
    """

    return gain_bias_transformation(image, -1, 255)

@image_limits_adjust()
def gamma_correction(
        image: np.ndarray,
        gamma: float,
        factor_k: float = 1,
        channels: list[int] | None = None,
    ) -> np.ndarray:
    """
    Función para aplicar una corrección 
    gamma. Esta función permite ajustar 
    el contraste y brillo de forma 
    exponencial (no lineal)
    """

    if not channels:
        transf_image = factor_k*image**gamma
    else:
        transf_image = image.copy()
        transf_image[:, :, channels] = factor_k*image[:, :, channels]**gamma
    
    return transf_image

@image_limits_adjust()
def logarithm_transformation(
        image: np.ndarray,
        factor_k: float = None,
    ) -> np.ndarray:
    """
    Función para aplicar una corrección 
    logarítmica. Esta función permite ajustar 
    el contraste y brillo de una imagen 
    de forma logarítmica.
    """

    if not factor_k:
        factor_k = 255/np.log10(1+image.max())
    
    return factor_k*np.log10(1+image)

@image_limits_adjust(factor_scaling=255)
def sigmoid_correction(
        image: np.ndarray,
        threshold: float,
        factor_c: float,
    ) -> np.ndarray:
    """
    Función aplicar una "binarización" a las 
    intensidad de una imagen
    """

    norm_image = normalize_image(image)
    return 1/(1+np.exp(factor_c*(threshold-norm_image)))

@image_limits_adjust(factor_scaling=255)
def histogram_equalize(
        image: np.ndarray,
        channels: list[int] | None = None,
    ) -> np.ndarray:
    """
    Función para aplicar una ecualización de contraste 
    empleando su histograma. Esta función permite ecualizar 
    el rango de contraste en una imagen.
    """

    if len(image.shape) == 2:
        image = np.expand_dims(image, 2)
    
    if not channels:
        equalize_image = np.apply_over_axes(equalize_channel, image, 2)
    else:
        equalize_image = image.copy()
        equalize_image[:, :, channels] = np.apply_over_axes(equalize_channel, image[:, :, channels], 2)

    return equalize_image

def equalize_channel(image_channel: np.ndarray, axis) -> np.ndarray:
    """
    Función para ecualizar un único canal de 
    color empleando su histograma.

    Devuelve un canal ecualizado de la imagen.
    """

    histogram, _ = np.histogram(image_channel, bins=256)
    normalized_histogram = histogram/image_channel.size
    running_sum = normalized_histogram.cumsum()
    return running_sum[image_channel]

def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Función para normalizar el rango de contraste de una 
    imagen por canal. 

    Devuelve una imagen cuyas intensidades están en [0, 1]
    """

    min_intensities_channel = image.min(axis=(0,1), keepdims=True)
    max_intensities_channel = image.max(axis=(0,1), keepdims=True)

    range_intensities_channel = max_intensities_channel-min_intensities_channel
    norm_image = (image-min_intensities_channel)/range_intensities_channel 
    return norm_image