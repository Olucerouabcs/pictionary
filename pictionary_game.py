import tkinter as tk
from tkinter import colorchooser
import random
import mysql.connector
import json
from unidecode import unidecode

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
        
        # Cargar usuarios desde el archivo JSON
        with open('users.json') as f:
            data = json.load(f)
            self.users = data['usuarios']


        # Obtener nombres de usuario
        # Crear un diccionario de usuarios con sus puntos
        self.user_points = {user['username']: user.get('puntos', 0) for user in self.users}
        
        """
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pictionary"
        )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar una consulta
        cursor.execute("SHOW DATABASES")

        # Iterar sobre los resultados e imprimirlos
        for base in cursor:
            print(base)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()
        
        # Obtener una palabra aleatoria de la base de datos
        self.current_word = self.get_random_word()
        """
        # Canvas para dibujar
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(side=tk.TOP, expand=True, fill="both")

        # Etiqueta para mostrar la palabra a dibujar
        self.word_label = tk.Label(root, text=f"A dibujar: {self.current_word}", font=("Helvetica", 14))
        self.word_label.pack(side=tk.TOP, anchor=tk.CENTER, pady=10)
        
        # Frame para herramientas
        self.tools_frame = tk.Frame(root)
        self.tools_frame.pack(side=tk.TOP, fill="x")

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
        self.chat_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        self.chat_label = tk.Label(self.chat_frame, text="Chat", font=("Helvetica", 14))
        self.chat_label.pack(pady=10)

        self.chat_text = tk.Text(self.chat_frame, width=30, height=20)
        self.chat_text.pack(fill="both", expand=True)
        self.chat_text.config(state=tk.DISABLED)

        # Cuadro de entrada para el chat
        self.chat_entry = tk.Entry(self.chat_frame)
        self.chat_entry.pack(side=tk.BOTTOM, fill="x")
        self.chat_entry.bind("<Return>", self.send_message)

        # 
        # Elementos de la interfaz de usuario
        self.points_frame = tk.Frame(root)
        self.points_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.points_label = tk.Label(self.points_frame, text="Usuarios y Puntos", font=("Helvetica", 18))  
        self.points_label.pack(pady=10)

        self.user_listbox = tk.Listbox(self.points_frame, font=("Helvetica", 14))  
        for username, points in self.user_points.items():
            self.user_listbox.insert(tk.END, f"{username}: {points} puntos")
        self.user_listbox.pack(fill="both", expand=True)

        # Configurar el evento de dibujo
        self.canvas.bind("<B1-Motion>", self.draw)

        # Inicializar el color de dibujo
        self.current_color = "black"
        self.eraser_mode = False

        # Configurar temporizador de 4 minutos
        self.timer_label = tk.Label(root, text="Tiempo restante: 4:00", font=("Helvetica", 14))
        self.timer_label.pack(side=tk.TOP, pady=10)
        self.remaining_time = 240  # 4 minutos en segundos
        self.update_timer()


    def send_message(self, event):
        message = self.chat_entry.get()
        if message:
            if unidecode(message.lower()) == unidecode(self.current_word.lower()):
                self.display_message("¡Palabra encontrada!")
            else:
                self.display_message(message)
            self.chat_entry.delete(0, tk.END)

    def display_message(self, message):
        if message.startswith("¡Palabra encontrada!"):
            word = self.current_word
            hidden_word = '*' * len(word)
            message = f"¡Palabra encontrada! {hidden_word}"
        self.chat_text.config(state=tk.NORMAL) 
        self.chat_text.insert(tk.END, message + '\n')
        self.chat_text.config(state=tk.DISABLED)  

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
    
    def get_random_word(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT word FROM words ORDER BY RAND() LIMIT 1")
        word = cursor.fetchone()[0]
        cursor.close()
        return word
    
    def update_timer(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        time_str = f"Tiempo restante: {minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=time_str)
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.current_word = random.choice(self.words)
            self.word_label.config(text=f"A dibujar: {self.current_word}")
            self.remaining_time = 240
            self.update_timer()
        
def main():
    root = tk.Tk()
    app = PictionaryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
