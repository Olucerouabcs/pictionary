import tkinter as tk
from pictionary_game import PictionaryGame
from login_screen import LoginScreen
from create_room_screen import CreateRoomScreen

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=50, pady=20)

        # Etiqueta de bienvenida
        self.welcome_label = tk.Label(self.main_frame, text="Bienvenido al juego Pictionary", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)

        # Botones de opciones
        self.play_button = tk.Button(self.main_frame, text="Jugar", command=self.start_game)
        self.play_button.pack(pady=5)

        self.login_button = tk.Button(self.main_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=5)

        self.quit_button = tk.Button(self.main_frame, text="Salir", command=self.root.quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        
        # Crear una nueva ventana para la vista de juego
        self.play_window = tk.Toplevel(self.root)
        self.play_window.title("Jugar")

        # Botón para crear sala
        self.create_room_button = tk.Button(self.play_window, text="Crear Sala", command=self.create_room)
        self.create_room_button.pack(pady=5)

        # Campo de entrada para el código de sala
        self.room_code_label = tk.Label(self.play_window, text="Código de Sala:")
        self.room_code_label.pack()
        self.room_code_entry = tk.Entry(self.play_window)
        self.room_code_entry.pack(pady=5)

        # Botón para unirse a sala
        self.join_room_button = tk.Button(self.play_window, text="Unirse a Sala", command=self.join_room)
        self.join_room_button.pack(pady=5)

    def create_room(self):
        create_room_root = tk.Toplevel(self.root)
        create_room_window = CreateRoomScreen(create_room_root)
        print(f"Creando sala con código: {room_code}")

    def join_room(self):
        # Aquí iría la lógica para unirse a una sala
        # Por ahora, simplemente mostramos un mensaje
        room_code = self.room_code_entry.get()
        print(f"Unirse a sala con código: {room_code}")

    def login(self):
        login_screen = LoginScreen(tk.Toplevel(self.root))
        

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
