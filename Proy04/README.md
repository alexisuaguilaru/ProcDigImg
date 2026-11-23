<div align="center">
<img src="../recursos/logo_unam.jpg" height="100">
<img src="../recursos/logo_enes.jpg" height="100">
<p style="font-size: 14px; font-weight: bold;"> Universidad Nacional Autónoma de México </p>
<p style="font-size: 14px; font-weight: bold;"> Escuela Nacional de Estudios Superiores Unidad Morelia </p>
<br>
<p style="font-size: 18px; font-weight: bold;"> Proyecto 04:<br>El Dominio de Fourier: Filtrado en la Frecuencia</p>
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
<p style="font-size: 14px;"> A 27 de Noviembre de 2026 </p>
</div>

---

## Introducción
Referirse al [reporte de proyecto](./report/proy04_report.pdf) para un desarrollo completo de la realización del proyecto y a la [Jupyter notebook](./proyecto.ipynb) para un desglose del código empleado para generar los resultados obtenidos.

## Planteamiento del Problema
Implementar y comparar:
1. Filtros de recorte (*Notch filters*) de Butterworth.
2. Con base en el espectro de Fourier en 2D, el alumno deberá desarrrollar un programa que elimine el ruido periódico de un conjunto de imágenes  proporcionadas por el docente.
3. El programa debe recibir como entrada la imagen ruidosa y debe devolver la imagen filtrada.

Una sola función de filtrado deberá recibir los parámetros necesarios que limpie lo mejor posible cada una de las 5 imágenes corruptas.

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