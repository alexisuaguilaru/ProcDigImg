from itertools import product
from typing import Callable

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

    return conv_image

def apply_filter_decorator(function_filer: Callable[[], np.ndarray]):
    """
    Decorador para aplicar una filtro específico a 
    una imagen, donde el resultado del filtrado 
    se convierte a una imagen válida para CV2. 
    """

    def apply_filter(
            image: np.ndarray, 
            fill_value: float = 0,
        ) -> np.ndarray:

        conv_image = apply_convolution(image, function_filer(), fill_value)
        return conv_image.round().clip(0, 255).astype(np.uint8)

    return apply_filter

PREWITT_FILTER_HOR = np.array([
    [-1,  0,  1],
    [-1,  0,  1],
    [-1,  0,  1],
])

PREWITT_FILTER_VER = np.rot90(PREWITT_FILTER_HOR)

@apply_filter_decorator
def prewitt_filter_horizontal() -> np.ndarray:
    return PREWITT_FILTER_HOR

@apply_filter_decorator
def prewitt_filter_vertical() -> np.ndarray:
    return PREWITT_FILTER_VER

SOBEL_FILTER_HOR = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1],
])

SOBEL_FILTER_VER = np.rot90(SOBEL_FILTER_HOR) 

@apply_filter_decorator
def sobel_filter_horizontal() -> np.ndarray:
    return SOBEL_FILTER_HOR

@apply_filter_decorator
def sobel_filter_vertical() -> np.ndarray:
    return SOBEL_FILTER_VER

LAPLACIAN_FILTER_1 = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0],
])

@apply_filter_decorator
def laplacian_filter_1() -> np.ndarray:
    return LAPLACIAN_FILTER_1

LAPLACIAN_FILTER_2 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])

@apply_filter_decorator
def laplacian_filter_2() -> np.ndarray:
    return LAPLACIAN_FILTER_2

LAPLACIAN_GAUSSIAN_FILTER = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [1, 2, -16, 2, 1],
    [0, 1, 2, 1, 0],
    [0, 0, 1, 0, 0],
])

@apply_filter_decorator
def laplacian_gaussian_filter() -> np.ndarray:
    return LAPLACIAN_GAUSSIAN_FILTER

def canny_filter(
        image: np.ndarray,
        lower_bound: int,
        upper_bound: int,
    ) -> np.ndarray:

    return cv2.Canny(image, lower_bound, upper_bound)

def apply_filter_base_cv2(
        filter: np.ndarray
    ) -> Callable[[np.ndarray], np.ndarray]:
    """
    Función wrapper para aplicar un filtro 
    a una imagen usando las funciones de CV2. 

    Se aplica un padding constante para que el output 
    image size sea igual al input.

    Devuelve la función para aplicar el filer 
    a la imagen.
    """

    def apply_filter_cv2(image: np.ndarray) -> np.ndarray:
        return cv2.filter2D(image, -1, filter, borderType=0)
    
    return apply_filter_cv2

prewitt_filter_horizontal_cv2 = apply_filter_base_cv2(PREWITT_FILTER_HOR)
prewitt_filter_vertical_cv2 = apply_filter_base_cv2(PREWITT_FILTER_VER)
sobel_filter_horizontal_cv2 = apply_filter_base_cv2(SOBEL_FILTER_HOR)
sobel_filter_vertical_cv2 = apply_filter_base_cv2(SOBEL_FILTER_VER)
laplacian_filter_1_cv2 = apply_filter_base_cv2(LAPLACIAN_FILTER_1)
laplacian_filter_2_cv2 = apply_filter_base_cv2(LAPLACIAN_FILTER_2)
laplacian_gaussian_filter_cv2 = apply_filter_base_cv2(LAPLACIAN_GAUSSIAN_FILTER)

class TypeFilters:
    all_names = ["prewitt", "sobel", "laplacian_1", "laplacian_2", "laplacian_gaussian"]

    prewitt = [PREWITT_FILTER_HOR, PREWITT_FILTER_VER]
    sobel = [SOBEL_FILTER_HOR, SOBEL_FILTER_VER]
    laplacian_1 = [LAPLACIAN_FILTER_1, LAPLACIAN_FILTER_1]
    laplacian_2 = [LAPLACIAN_FILTER_2, LAPLACIAN_FILTER_2]
    laplacian_gaussian = [LAPLACIAN_GAUSSIAN_FILTER, LAPLACIAN_GAUSSIAN_FILTER]

    function_prewitt = [prewitt_filter_horizontal_cv2, prewitt_filter_vertical_cv2]
    function_sobel = [sobel_filter_horizontal_cv2, sobel_filter_vertical_cv2]
    function_laplacian_1 = [laplacian_filter_1_cv2]
    function_laplacian_2 = [laplacian_filter_2_cv2]
    function_laplacian_gaussian = [laplacian_gaussian_filter_cv2]

    name_prewitt = "Prewitt"
    name_sobel = "Sobel"
    name_laplacian_1 = "Laplace 1"
    name_laplacian_2 = "Laplace 2"
    name_laplacian_gaussian = "Laplaciano de Gaussiana"

    @classmethod
    def get_filter(cls, type_filter: str) -> tuple[np.ndarray, np.ndarray]:
        return vars(TypeFilters)[type_filter]
    
    @classmethod
    def get_functions(cls, type_filter: str) -> tuple[Callable[[np.ndarray], np.ndarray], Callable[[np.ndarray], np.ndarray]]:
        return vars(TypeFilters)["function_"+type_filter]
    
    @classmethod
    def get_name(cls, type_filter: str) -> str:
        return vars(TypeFilters)["name_"+type_filter]