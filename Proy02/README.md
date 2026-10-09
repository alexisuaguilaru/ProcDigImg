<div align="center">
<img src="../recursos/logo_unam.jpg" height="100">
<img src="../recursos/logo_enes.jpg" height="100">
<p style="font-size: 14px; font-weight: bold;"> Universidad Nacional Autónoma de México </p>
<p style="font-size: 14px; font-weight: bold;"> Escuela Nacional de Estudios Superiores Unidad Morelia </p>
<br>
<p style="font-size: 18px; font-weight: bold;"> Proyecto 02:<br>Encontrando Estructuras</p>
<br>
<p style="font-size: 12px;"> PRESENTA: </p>
<p style="font-size: 16px; font-weight: 500;"> Aguilar Uribe Alexis Uriel </p>
<p style="font-size: 14px;"> Numero de Cuenta:<br> 424060075 </p>
<br>
<br>
<p style="font-size: 12px;"> PROFESOR: </p>
<p style="font-size: 16px; font-weight: 500;"> Dr. Tinoco Martínez Sergio Rogelio </p>
<br>
<br>
<p style="font-size: 14px;"> Licenciatura  en Tecnologías para la Información en Ciencias </p>
<p style="font-size: 15px;"> Procesamiento Digital de Imágenes </p>
<br>
<p style="font-size: 14px;"> A 12 de Octubre de 2026 </p>
</div>

---

## Introducción
Referirse al [reporte de proyecto](./report/proy02_report.pdf) para un desarrollo completo de la realización del proyecto y a la [Jupyter notebook](./proyecto.ipynb) para un desglose del código empleado para generar los resultados obtenidos.

## Planteamiento del Problema
Para un conjunto de imágenes se deberá comparar:
1. Métodos de detección
2. Ventajas y desventajas de los diferentes métodos

Así como comparar el resultado de aplicar los siguientes tipos de suavizados sobre la imagen (para cada método de detección), analizando el efecto sobre los bordes:
* Sin suavizado.
* Con suavizado gaussiano con un kernel de $3\times3$ píxeles.
* Con suavizado gaussiano con un kernel de $7\times7$ píxeles.

Adicionalmente, se deberá incluir la interpretación de las siguientes expresiones:
* $G_x = \frac{\partial I(x, y)}{\partial x}$
* $G_y = \frac{\partial I(x, y)}{\partial y}$
* $G = \sqrt{G_x^2+G_y^2}$
* $\theta = \arctan(\frac{G_y}{G_x})$

Por último, se visualizará la orientación de los bordes colocando una flecha con inicio en el pixel actual, de longitud conveniente, que apunte en la dirección señalada por el ángulo calculado $\theta$.

Al menos Sobel y Prewitt deberán implementarse manualmente con NumPy, sin utilizar una función de alto nivel que haga el procedimiento.

## Uso y Ejecución
### Proyecto en Jupyter Notebook
En el caso de estar empleando uv, basta con ejecutar el siguiente comando para abrir y ejecutar la notebook en Jupyter:
```bash
uv run jupyter notebook proyecto.ipynb
```
En caso de estar en un ambiente virtual basado en conda, emplee:
```bash
jupyter notebook proyecto.ipynb
```
### Reporte en LaTeX
Para poder compilar el reporte del proyecto en LaTeX es requerido primero ejecutar toda la Jupyter notebook abierta en el apartado anterior. Posterior se podrá compilar y generar el PDF del reporte.