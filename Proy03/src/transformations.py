from functools import reduce

import numpy as np

def translation_matrix(
        x_move: float = 0,
        y_move: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de traslación. Toma 
    de entrada el movimiento 
    horizontal y vertical.
    """

    matrix = np.array([
        [1, 0, -y_move],
        [0, 1, x_move],
        [0, 0, 1]
    ], dtype=float)
    return matrix

def inverse_translation_matrix(
        x_move: float = 0,
        y_move: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de traslación inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    return translation_matrix(-x_move, -y_move)

def rotation_matrix(angle: float) -> np.ndarray:
    """
    Función para generar la 
    matriz de rotación. Toma 
    de entrada el ángulo de 
    rotación.
    """

    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    matrix = np.array([
        [cos_angle, sin_angle, 0],
        [-sin_angle, cos_angle, 0],
        [0, 0, 1]
    ], dtype=float)
    return matrix

def inverse_rotation_matrix(angle: float) -> np.ndarray:
    """
    Función para generar la 
    matriz de rotación inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    return rotation_matrix(-angle)

def centered_rotation_matrix(
        angle: float = 0,
        center_x: float = 0,
        center_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de rotación centrada 
    respecto al centro de la 
    imagen. Toma de entrada las 
    coordenadas del centro de 
    la imagen y el ángulo de rotation.
    """

    return inverse_translation_matrix(-center_x, center_y)@rotation_matrix(angle)@translation_matrix(-center_x, center_y)

def inverse_centered_rotation_matrix(
        angle: float = 0,
        center_x: float = 0,
        center_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de rotación centrada inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    return centered_rotation_matrix(-angle, center_x, center_y)

def reflection_matrix(
        reflect_x: bool = False,
        reflect_y: bool = False,
        center_x: float = 0,
        center_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la matriz 
    de reflexión sobre los ejes centrados 
    en la imagen. Toma de entrada si se aplica 
    la reflexión individualmente sobre los ejes x 
    y y, y las coordenadas del centro de la imagen.
    """

    value_x = -1 if reflect_x else 1
    value_y = -1 if reflect_y else 1
    reflection = np.array([
        [value_y, 0, 0],
        [0, value_x, 0],
        [0, 0, 1],
    ])

    return inverse_translation_matrix(-center_x, center_y)@reflection@translation_matrix(-center_x, center_y)

def inverse_reflection_matrix(
        reflect_x: bool = False,
        reflect_y: bool = False,
        center_x: float = 0,
        center_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de reflexión inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    return reflection_matrix(reflect_x, reflect_y, center_x, center_y)

def scaling_matrix(
        scale_x: float = 1,
        scale_y: float = 1,
    ) -> np.ndarray:
    """
    Función para generar la matriz 
    de escala sobre los ejes. 
    Toma de entrada las nuevas escalas 
    de los ejes x y y.
    """

    scaling = np.array([
        [scale_x, 0, 0],
        [0, scale_y, 0],
        [0, 0, 1],
    ])
    return scaling

def inverse_scaling_matrix(
        scale_x: float = 1,
        scale_y: float = 1,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de escalmiento inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    return scaling_matrix(1/scale_x, 1/scale_y)

def shearing_matrix(
        shift_x: float = 0,
        shift_y: float = 0,
        img_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la matriz 
    de cizallamiento sobre los ejes. 
    Toma de entrada los desplazamientos 
    de los ejes x y y, como el tamaño 
    en y de la imagen para reajustarla.
    """

    determinant_shearing = 1-shift_x*shift_y
    shearing = np.array([
        [1, -shift_x, 0],
        [-shift_y, 1, 0],
        [0, 0, determinant_shearing]
    ])
    translation = translation_matrix(img_y*shift_y)
    return shearing@translation/determinant_shearing

def inverse_shearing_matrix(
        shift_x: float = 0,
        shift_y: float = 0,
        img_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la 
    matriz de cizallamiento inversa 
    usando los mismos parámetros 
    que en la matriz original.
    """

    inverse_shearing = np.array([
        [1, shift_x, 0],
        [shift_y, 1, 0],
        [0, 0, 1]
    ])
    inverse_translation = translation_matrix(-img_y*shift_y)
    return inverse_translation@inverse_shearing

def affine_transformation_matrix(
        x_move: float = 0,
        y_move: float = 0,
        center_x: float = 0,
        center_y: float = 0,
        angle: float = 0,
        reflect_x: bool = False,
        reflect_y: bool = False,
        scale_x: float = 1, 
        scale_y: float = 1,
        shift_x: float = 0,
        shift_y: float = 0,
        img_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la matriz general 
    de una transformación afín. Toma de 
    parámetros los definidos para cada 
    matriz de transformación individualmente.
    """

    transformations = [
        translation_matrix(x_move, y_move),
        centered_rotation_matrix(center_x, center_y, angle),
        reflection_matrix(reflect_x, reflect_y),
        scaling_matrix(scale_x, scale_y),
        shearing_matrix(shift_x, shift_y, img_y),
    ]
    return reduce(lambda t_1, t_2 : t_1@t_2, transformations)

def inverse_affine_transformation_matrix(
        x_move: float = 0,
        y_move: float = 0,
        center_x: float = 0,
        center_y: float = 0,
        angle: float = 0,
        reflect_x: bool = False,
        reflect_y: bool = False,
        scale_x: float = 1, 
        scale_y: float = 1,
        shift_x: float = 0,
        shift_y: float = 0,
        img_y: float = 0,
    ) -> np.ndarray:
    """
    Función para generar la matriz general 
    de una transformación afín inversa. Toma de 
    parámetros los mismos que los definidos 
    para cada matriz inversa y equivalentes 
    a la original.
    """

    inverse_transformations = [
        inverse_shearing_matrix(shift_x, shift_y, img_y),
        inverse_scaling_matrix(scale_x, scale_y),
        inverse_reflection_matrix(reflect_x, reflect_y, center_x, center_y),
        inverse_centered_rotation_matrix(angle, center_x, center_y),
        inverse_translation_matrix(x_move, y_move),
    ]
    return reduce(lambda t_1, t_2 : t_1@t_2, inverse_transformations)

def interpolation_bilinear_pixels(
        image: np.ndarray, 
        point: np.ndarray,
    ) -> int:
    """
    Función para calcular la interpolación bilineal 
    de los pixeles de una imagen donde emplea 
    las intensidades de los pixeles vecinos de un 
    punto dado por la transformada afín inversa. 
    Devuelve la intensidad del punto asociado.
    """

    integer_point, deltas = divmod(point, 1)
    integer_point = integer_point.astype(int)

    intensities_neighborhood = np.array([
        [image[*(integer_point+[0,0])],
        image[*(integer_point+[0,1])]],
        [image[*(integer_point+[1,0])],
        image[*(integer_point+[1,1])]],
    ], dtype=int)

    delta_x = deltas[0]
    weights_x = np.array([1-delta_x, delta_x])

    delta_y = deltas[1]
    weights_y = np.array([1-delta_y, delta_y])

    return (weights_x@intensities_neighborhood@weights_y).round().astype(int)

def apply_affine_transformation(
        image: np.ndarray,
        inverse_affine: np.ndarray|None = None, 
        *,
        x_move: float = 0,
        y_move: float = 0,
        angle: float = 0,
        reflect_x: bool = False,
        reflect_y: bool = False,
        scale_x: float = 1, 
        scale_y: float = 1,
        shift_x: float = 0,
        shift_y: float = 0,
    ) -> np.ndarray:
    """
    Función para aplicar una transformación afín a 
    una imagen dada. Se emplea de la transformación 
    afín inversa y de interpolación bileneal para 
    estimar la intensidad de color en la imagen 
    resultante. Devuelve la matriz de la imagen 
    después de aplicarle la transformada.
    """

    if inverse_affine is None:
        img_y, img_x = image.shape[:2]
        center_x = img_x/2
        center_y = img_y/2
        inverse_affine = inverse_affine_transformation_matrix(
            x_move = x_move,
            y_move = y_move,
            center_x = center_x,
            center_y = center_y,
            angle = angle,
            reflect_x = reflect_x,
            reflect_y = reflect_y,
            scale_x = scale_x,
            scale_y = scale_y,
            shift_x = shift_x,
            shift_y = shift_y,
            img_y = img_y,
        )

    height, width = image.shape
    range_height = np.arange(height)
    range_width = np.arange(width)
    grid = np.meshgrid(range_height, range_width)
    grid_ones = np.ones_like(grid[0])
    meshgrid = np.stack([*grid, grid_ones]).reshape(3, -1)
    inverse_meshgrid = inverse_affine@meshgrid    
    
    transformed_image = np.zeros_like(image)
    padded_image = np.pad(image, 1)

    lower_bound = np.array([0, 0, 1])
    upper_bound = np.array([height, width, 1.1])
    for point, inverse_point in zip(meshgrid.T, inverse_meshgrid.T):
        valid_point = np.all((lower_bound<=inverse_point)&(inverse_point<upper_bound))
        if valid_point:
            img_point = point[:2]
            transformed_image[*img_point] = interpolation_bilinear_pixels(padded_image, inverse_point[:2])

    return transformed_image