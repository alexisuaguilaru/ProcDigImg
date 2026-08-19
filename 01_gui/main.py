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

## Creación de placeholders en la GUI
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
    button = tk.Button(frame, text=text, width=20, command=command)
    button.pack(side="top")
    return button

def delete_children_widgets(frame: tk.Frame) -> None:
    for widget in frame.winfo_children():
        widget.destroy()

## Botón para cargar/seleccionar una imagen
file_path: Path | str | None = None
gray_image: Image.Image | None = None

def open_image() -> None:
    global file_path
    global gray_image

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

        ## Eliminar widgets o botones mostrados previamente
        if gray_image:
            list(map(delete_children_widgets, frames[1:]))

        insert_image(color_image, frames[2])
        
        button_save = add_button(frames[1], "Guardar", save_image)
        gray_image = color_image.convert("L")
        insert_image(gray_image, frames[3])

def insert_image(pil_image: Image.Image, frame: tk.Frame) -> None:
    ## Reescalamiento de la imagen para que ocupe todo el widget
    frm_width = frame.winfo_width()
    fmr_height = frame.winfo_height()
    image = pil_image.copy()
    image.thumbnail((frm_width,fmr_height))

    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=image, justify="center")
    image_label.pack(side="top")
    image_label.image = image # Referencia adicional para evitar que el garbage collector elimine la imagen antes de mostrarla en la GUI

button_open = add_button(frames[0], "Abrir", open_image)

## Botón para guardar la imagen en escala de grises
def save_image() -> None:
    if file_path and gray_image:
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