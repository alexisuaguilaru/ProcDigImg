import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from typing import Callable

from PIL import Image, ImageOps, ImageTk

## Inicialización del gestor de ventana
root = tk.Tk()
root.title("Imagen a Escala de Grises")
root.geometry("924x520")
root.minsize(640, 480)

## Configuración de como las filas y columnas se van a distribuir sobre la ventana
root.grid_columnconfigure((0, 1), weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)

## Creación de placeholders/contenedores en la GUI
num_columns = 2
num_rows = 2
frames: list[tk.Frame] = []

for row in range(num_rows):
    for column in range(num_columns):
        frame = tk.Frame(root, width=75, height=50)
        frame.grid(row=row, column=column, pady=5, sticky="nsew")
        frames.append(frame)

## Definición de utilidades para crear y destruir widgets 
def add_button(frame: tk.Frame, text: str, command: Callable) -> tk.Button:
    """
    Función para añadir un botón en la parte superior de 
    un contenedor (`frame`) con un cierto texto y para que 
    ejecute un comando.

    Devuelve el botón añadido al frame.
    """
    button = tk.Button(frame, text=text, width=20, command=command)
    button.pack(side="top")
    return button

def delete_children_widgets(frame: tk.Frame) -> None:
    """
    Función para eliminar los elementos o 
    widgets contenidos en un frame con el 
    fin de resetearlo.
    """
    for widget in frame.winfo_children():
        widget.destroy()

## Botón para cargar/seleccionar una imagen
file_path: Path | str | None = None
gray_image: Image.Image | None = None

def open_image() -> None:
    """
    Función para seleccionar y cargar una imagen a 
    la GUI. Primero abre un ventana para buscar 
    y seleccionar la imagen del usuario, posteriormente 
    se carga y se transforma a escala de grises, este 
    proceso de realiza con PIL. Finalmente, se inserta la 
    imagen en la GUI y se añade el botón para guardar la 
    versión en escala de grises.

    En caso de se haya cargado previamente una imagen, lo 
    primero que se realiza es un reset en cada uno de 
    los contenedores.
    """
    global file_path
    global gray_image

    ## Abrir cuadro de dialogo para buscar una imagen
    file_path = filedialog.askopenfilename(
        title = "Seleccione una imagen para convertirla a escala de grises",
        initialdir = "~/downloads",
        filetypes = [("Imágenes", ["*.png", "*.jpg", "*.jpeg"])]
    )
    
    ## Abrir y transformar la imagen en el formato que tkinter espera
    ## Display la imagen reescalada en la GUI 
    if file_path:
        file_path = Path(file_path)
        color_image = Image.open(file_path)
        color_image = ImageOps.exif_transpose(color_image) # Preservar la orientación original de la imagen usando los metadatos

        ## Eliminar widgets o botones mostrados previamente, en caso de seleccionar otra imagen
        if gray_image:
            list(map(delete_children_widgets, frames[1:]))

        insert_image(color_image, frames[2])
        
        button_save = add_button(frames[1], "Guardar", save_image)
        gray_image = color_image.convert("L")
        insert_image(gray_image, frames[3])

def insert_image(pil_image: Image.Image, frame: tk.Frame) -> None:
    """
    Función para insertar una imagen en un contenedor (`frame`), 
    en la que primero se ajusta al tamaño máximo del mismo para 
    último convertirla a una imagen en el formato que espera 
    tkinter.

    Un detalle técnico importante es que se le suma uno al 
    número del contador de referencias de la imagen que se inserta 
    para evitar que sea eliminada por el GB después de ejecutar 
    la función.
    """
    ## Reescalamiento de la imagen para que ocupe todo el widget
    frm_width = frame.winfo_width()
    fmr_height = frame.winfo_height()
    image = pil_image.copy()
    image.thumbnail((frm_width,fmr_height))

    ## Inserción de la imagen en la GUI ajustada a los widgets/contenedores
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=image, justify="center")
    image_label.pack(side="top")
    image_label.image = image # Referencia adicional para evitar que el garbage collector elimine la imagen antes de mostrarla en la GUI

button_open = add_button(frames[0], "Abrir", open_image)

## Botón para guardar la imagen en escala de grises
def save_image() -> None:
    """
    Función para guardar la imagen en escala de grises al hacer 
    click en el correspondiente botón. Abre una ventana para 
    confirmar el nombre de la imagen y la ruta en la que se 
    va a guardar, por default se usa nombre derivado de la 
    imagen original y el mismo path
    """
    global file_path
    global gray_image

    if file_path and gray_image:
        ## Abrir cuadro de dialogo para guardar la imagen en escala de grises
        extension = file_path.suffix[1:]
        save_file_path = filedialog.asksaveasfilename(
            title = "Guardar imagen a escala de grises.",
            initialdir = file_path.parent,
            initialfile = file_path.stem+"_gray",
            defaultextension = extension,
            filetypes = [(f"Imagen {extension.upper()}", f"*.{extension}")]
        )
        
        if save_file_path:
            save_file_path = Path(save_file_path)
            gray_image.save(save_file_path)

if __name__ == "__main__":
    root.mainloop()