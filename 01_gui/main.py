import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from PIL import Image, ImageTk

## Inicialización del gestor de ventana
root = tk.Tk()
root.title("Imagen a Escala de Grises")
root.geometry("640x480")
root.minsize(320, 240)

## Configuración de como las filas y columnas se van a distribuir sobre la ventana
root.grid_columnconfigure((0, 1), weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)

## Creación de placeholders en la GUI
num_columns = 2
num_rows = 2
frames: list[tk.Frame] = []
colors = [["red", "blue"], ["green", "yellow"]]

for row in range(num_rows):
    for column in range(num_columns):
        frame = tk.Frame(root, width=75, height=50, bg=colors[row][column])
        frame.grid(row=row, column=column, pady=5, sticky="nsew")
        frames.append(frame)

## Botón para cargar/seleccionar una imagen
file_path: Path | str | None = None
gray_image: Image.Image | None = None

def open_image() -> None:
    global file_path
    file_path = filedialog.askopenfilename(
        title = "Seleccione una imagen para convertirla a escala de grises",
        initialdir = "~/downloads",
        filetypes = [("Imágenes", ["*.png", "*.jpg", "*.jpeg", "*.svg"])]
    )
    
    ## Abrir y transformar la imagen en el formato que tkinter espera
    ## Display la imagen reescalada en la GUI 
    if file_path:
        file_path = Path(file_path)
        color_image = Image.open(file_path)
        
        global gray_image
        gray_image = color_image.convert("L")
        
        insert_image(color_image, frames[2])
        insert_image(gray_image, frames[3])

def insert_image(pil_image: Image.Image, frame: tk.Frame) -> None:
    aspect_ratio = int.__truediv__(*pil_image.size)

    frm_width = frame.winfo_width()*0.5
    fmr_height = frame.winfo_height()*0.5
    image = pil_image.copy()
    image.thumbnail((int(aspect_ratio*frm_width),int(aspect_ratio*fmr_height)))

    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=image, justify="center")
    image_label.grid(column=1, row=1)
    image_label.image = image # Referencia adicional para evitar que el garbage collector elimine la imagen antes de mostrarla en la GUI

button_open = tk.Button(frames[0], text="Abrir", width=20, command=open_image)
button_open.pack(side="top")

## Botón para guardar la imagen en escala de grises
def save_image() -> None:
    if file_path and gray_image:
        extension = file_path.suffix[1:]
        save_file_path = filedialog.asksaveasfilename(
            title = "Guardar imagen a escala de grises.",
            initialdir = file_path.parent,
            initialfile = file_path.stem+"_gray"+file_path.suffix,
            defaultextension = extension,
            # filetypes = [("Image", ["*.png", "*.jpg", "*.jpeg", "*.svg"])],
            filetypes = [(f"Imagen {extension.upper()}", f"*.{extension}")]
        )
        save_file_path = Path(save_file_path)

        gray_image.save(save_file_path)

button_save = tk.Button(frames[1], text="Guardar", width=20, command=save_image)
button_save.pack(side="top")

if __name__ == "__main__":
    root.mainloop()