from itertools import product

import cv2
import numpy as np

def apply_convolution(
        image: np.ndarray,
        filter: np.ndarray, 
        fill_value: float = 0,
    ) -> np.ndarray:
    """
    Función para aplicar un filtro o kernel 
    a una imagen. El filtro no es rotado 
    180° para hacer coincidir esta función 
    con la implementación de CV2 filter2D. 

    Aplica un padding constante, por defecto 
    igual a 0, esto siguiendo el comportamiento 
    normal en las redes neuronales.

    Devuelve el resultado de aplicar el filtro 
    a la imagen.
    """

    image = image.astype(int)

    padding = (filter.shape[0]-1)//2
    padding_image = np.pad(
        image, 
        {0: padding, 1: padding}, 
        constant_values = fill_value,
    )

    if len(image.shape) == 3:
        filter = filter[:, :, None]

    conv_image = np.zeros_like(image)
    size_height, size_width = image.shape[:2]

    for (i_height, j_width) in product(range(padding, size_height+padding), range(padding, size_width+padding)):
        image_values = padding_image[i_height-padding: i_height+padding+1, j_width-padding: j_width+padding+1]
        conv_image[i_height-padding, j_width-padding] = (image_values*filter).sum(axis=(0, 1))

    conv_image = conv_image.round().clip(0, 255).astype(np.uint8)
    return conv_image

PREWITT_FILTER_HOR = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1],
])

PREWITT_FILTER_VER = np.rot90(PREWITT_FILTER_HOR)

def prewitt_filter_horizontal(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, PREWITT_FILTER_HOR, fill_value)

def prewitt_filter_vertical(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, PREWITT_FILTER_VER, fill_value)

SOBEL_FILTER_HOR = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],
])

SOBEL_FILTER_VER = np.rot90(SOBEL_FILTER_HOR) 

def sobel_filter_horizontal(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, SOBEL_FILTER_HOR, fill_value)

def sobel_filter_vertical(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, SOBEL_FILTER_VER, fill_value)

LAPLACIAN_FILTER_1 = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0],
])

def laplacian_filter_1(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, LAPLACIAN_FILTER_1, fill_value)

LAPLACIAN_FILTER_2 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])

def laplacian_filter_2(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, LAPLACIAN_FILTER_2, fill_value)

LAPLACIAN_GAUSSIAN_FILTER = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [1, 2, -16, 2, 1],
    [0, 1, 2, 1, 0],
    [0, 0, 1, 0, 0],
])

def laplacian_gaussian_filter(
        image: np.ndarray,
        fill_value: float = 0,
    ) -> np.ndarray:

    return apply_convolution(image, LAPLACIAN_GAUSSIAN_FILTER, fill_value)

def canny_filter(
        image: np.ndarray,
        lower_bound: int,
        upper_bound: int,
    ) -> np.ndarray:

    return cv2.Canny(image, lower_bound, upper_bound)