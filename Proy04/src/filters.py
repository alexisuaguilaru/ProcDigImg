from functools import reduce

import numpy as np

def butterworth_band_reject_filter(
        img_size: tuple[int, int], 
        band_center: tuple[int, int] = (0, 0), 
        width: float = 1, 
        order: int = 2,
    ) -> np.ndarray:
    """
    Función para definir el filtro 
    de Butterworth rechaza banda con 
    los parámetros dados. Devuelve 
    una matriz que representa el 
    filtro.

    Toma de parámetros la forma de la 
    imagen, el centro de la banda, el 
    ancho y el orden. 
    """

    num_rows, num_cols = img_size
    rows = np.arange(-num_rows/2+1, num_rows/2+1)
    cols = np.arange(-num_cols/2+1, num_cols/2+1)
    frequencies_x, frequencies_y = np.meshgrid(rows, cols)

    distances = 1e-15+frequencies_x**2+frequencies_y**2
    distances = distances/distances.max()
    
    distances_center = 1e-15+(frequencies_x-band_center[0])**2+(frequencies_y-band_center[1])**2
    distances_center = distances_center/distances_center.max()

    score = (np.sqrt(distances)*width/distances_center)**(2*order)
    butterworth = 1/(1+score)
    return butterworth

def butterworth_low_pass_filter(
        img_size: tuple[int, int], 
        band_center: tuple[int, int] = (0, 0), 
        width: float = 1, 
        order: int = 2,
    ) -> np.ndarray:
    """
    Función para definir el filtro 
    de Butterworth pasa bajas (banda)
    con los parámetros dados. 
    Devuelve una matriz que representa 
    el filtro. 

    Toma de parámetros la forma de la 
    imagen, el centro de la banda, el 
    ancho y el orden.
    """

    butterworth = 1-butterworth_band_reject_filter(img_size, band_center, width, order)
    return butterworth

def single_notch_butterworth_filter(
        img_size: tuple[int, int], 
        band_center: tuple[int, int] = (0, 0), 
        width: float = 1, 
        order: int = 2,
    ) -> np.ndarray:
    """
    Función para definir un filtro de recorte 
    basado en los filtros de Butterworth con 
    los parámetros dados. Devuelve una matriz 
    que representa el filtro.

    Toma de parámetros la forma de la 
    imagen, el centro de la banda, el 
    ancho y el orden. 
    """

    butterworth_filter_1 = butterworth_band_reject_filter(img_size, band_center, width, order)
    butterworth_filter_2 = butterworth_band_reject_filter(img_size, (-band_center[0], -band_center[1]), width, order)
    notch_butterworth = butterworth_filter_1*butterworth_filter_2
    return notch_butterworth

def compose_notch_butterworth_filter(
        img_size: tuple[int, int],
        filter_parameters: list[tuple[tuple[int, int], float, int]]
    ) -> np.ndarray:
    """
    Función para definir el filtro de recorte 
    basándose en la composición (multiplicación) 
    de filtros simples de Butterworth pasa bajas. 
    Devuelve la matriz resultante de la composición.

    Toma de parámetros la forma de la imagen y 
    una lista con los parámetros de los filtros 
    como tuplas de (band_center, width, order).
    """

    simple_notch_filters = map(lambda params: single_notch_butterworth_filter(img_size, *params), filter_parameters)
    notch_butterworth = reduce(np.ndarray.__mul__, simple_notch_filters)
    return notch_butterworth