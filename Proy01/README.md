<div align="center">
<img src="../recursos/logo_unam.jpg" height="100">
<img src="../recursos/logo_enes.jpg" height="100">
<p style="font-size: 14px; font-weight: bold;"> Universidad Nacional Autónoma de México </p>
<p style="font-size: 14px; font-weight: bold;"> Escuela Nacional de Estudios Superiores Unidad Morelia </p>
<br>
<p style="font-size: 18px; font-weight: bold;"> Proyecto 01:<br>Conociendo la Imagen </p>
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
<p style="font-size: 14px;"> A 24 de Septiembre de 2026 </p>
</div>

---

## Introducción
Referirse al [reporte de proyecto](./report/proy01_report.pdf) para un desarrollo completo de la realización del proyecto y a la [Jupyter notebook](./proyecto.ipynb) para un desglose del código empleado para generar los resultados obtenidos.

## Planteamiento del Problema
Dado un [conjunto de imágenes](./dataset/) con diferentes problemas:
* Bajo contraste.
* Sobreexposición.
* Subexposición.
* Iluminación no uniforme.
* Predominio de determinado canal de color.

Se deberá que desarrollar un pequeño sistema de análisis y mejoramiento de imágenes, el cual deberá que:
1. Cargar una imagen.
2. Identificar sus dimensiones y número de canales.
3. Mostrar histogramas.
4. Genera versión en escala de grises.
5. Modificar brillo.
6. Modificar contraste.
7. Aplicar transformación gamma.
8. Realizar ecualización de histograma.
9. Comparar las imágenes antes/después.
10. Generar un reporte de resultados.

Al menos dos transformaciones deberán implementarse manualmente con NumPy, sin utilizar una función de alto nivel que haga directamente todo el procedimiento. Por ejemplo, no basta con llamar a una función de ecualización y entregar el resultado.

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