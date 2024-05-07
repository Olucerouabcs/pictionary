import tkinter as tk
from tkinter import colorchooser
import json
import random

class PictionaryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pictionary")

        # Cargar palabras desde el archivo JSON
        with open('words.json') as f:
            data = json.load(f)
            self.words = data['words']

        # Elegir una palabra aleatoria
        self.current_word = random.choice(self.words)

        # Canvas para dibujar
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(side=tk.TOP, expand=True, fill="both")

        # Etiqueta para mostrar la palabra
        self.word_label = tk.Label(root, text=f"Palabra: {self.current_word}", font=("Helvetica", 14))
        self.word_label.pack(side=tk.TOP, pady=10)

        # Frame para herramientas
        self.tools_frame = tk.Frame(root)
        self.tools_frame.pack(side=tk.BOTTOM, fill="x")

        # Botones de herramientas
        self.clear_button = tk.Button(self.tools_frame, text="Borrar todo", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.eraser_button = tk.Button(self.tools_frame, text="Borrador", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.brush_button = tk.Button(self.tools_frame, text="Pincel", command=self.use_brush)
        self.brush_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.brush_button.configure(state="disabled")

        self.color_button = tk.Button(self.tools_frame, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.brush_size_label = tk.Label(self.tools_frame, text="Grosor del pincel:")
        self.brush_size_label.pack(side=tk.LEFT, padx=5, pady=10)

        self.brush_size_slider = tk.Scale(self.tools_frame, from_=1, to=20, orient=tk.HORIZONTAL)
        self.brush_size_slider.pack(side=tk.LEFT, padx=5, pady=10)

        # Frame para el chat
        self.chat_frame = tk.Frame(root)
        self.chat_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

        self.chat_label = tk.Label(self.chat_frame, text="Chat", font=("Helvetica", 14))
        self.chat_label.pack(pady=10)

        self.chat_text = tk.Text(self.chat_frame, width=30, height=20)
        self.chat_text.pack(fill="both", expand=True)

        # Configurar el evento de dibujo
        self.canvas.bind("<B1-Motion>", self.draw)

        # Inicializar el color de dibujo
        self.current_color = "black"
        self.eraser_mode = False

    def clear_canvas(self):
        self.canvas.delete("all")

    def use_eraser(self):
        self.canvas.configure(cursor="dot")
        self.canvas.bind("<B1-Motion>", self.erase)
        self.eraser_mode = True
        self.eraser_button.configure(state="disabled")
        self.brush_button.configure(state="normal")

    def erase(self, event):
        x = event.x
        y = event.y
        brush_size = self.brush_size_slider.get()
        self.canvas.create_oval(x-brush_size, y-brush_size, x+brush_size, y+brush_size, fill="white", outline="white")

    def use_brush(self):
        self.canvas.configure(cursor="")
        self.canvas.bind("<B1-Motion>", self.draw)
        self.eraser_mode = False
        self.eraser_button.configure(state="normal")
        self.brush_button.configure(state="disabled")

    def choose_color(self):
        color = colorchooser.askcolor()
        if color[1]:
            self.current_color = color[1]

    def draw(self, event):
        x = event.x
        y = event.y
        brush_size = self.brush_size_slider.get()
        if not self.eraser_mode:
            self.canvas.create_oval(x-brush_size, y-brush_size, x+brush_size, y+brush_size, fill=self.current_color, outline=self.current_color)

def main():
    root = tk.Tk()
    app = PictionaryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
