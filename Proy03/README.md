<div align="center">
<img src="../recursos/logo_unam.jpg" height="100">
<img src="../recursos/logo_enes.jpg" height="100">
<p style="font-size: 14px; font-weight: bold;"> Universidad Nacional Autónoma de México </p>
<p style="font-size: 14px; font-weight: bold;"> Escuela Nacional de Estudios Superiores Unidad Morelia </p>
<br>
<p style="font-size: 18px; font-weight: bold;"> Proyecto 03:<br>Modificando el Marco de Referencia</p>
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
Referirse al [reporte de proyecto](./report/proy03_report.pdf) para un desarrollo completo de la realización del proyecto y a la [Jupyter notebook](./proyecto.ipynb) para un desglose del código empleado para generar los resultados obtenidos.

## Planteamiento del Problema
Implementar y comparar:
1. Transformación afín general para un imagen en escala de grises.
2. Interpolación bilineal

Así como probar la implementación sobre una matriz de transformación afín que realice, al menos, una operación de: 
1. Rotación, con un ángulo que no sea múltiplo de 45°.
2. Traslación en ambos ejes.
3. Reflexión en ambos ejes.
4. Escalamiento en ambas direcciones/ejes
5. Al menos dos ejemplos de composición de transformaciones afines: rotación, traslación, escalamiento (an)isotrópico, reflexión y/o cizallamiento.

Las operaciones indicadas deberán ser implementadas como matrices de transformación afín, utilizando la interpolación bilineal para el relleno de huecos.

Ambas operaciones deberán implementarse manualmente con NumPy, sin utilizar una función de alto nivel que haga el procedimiento.

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