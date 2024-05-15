import tkinter as tk
import random
import string
import subprocess

class CreateRoomScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Crear Sala")

        # Lista de usuarios que se unen a la sala
        self.users_list = []

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=50, pady=20)

        # Etiqueta para la lista de usuarios
        self.users_label = tk.Label(self.main_frame, text="Usuarios en la Sala:")
        self.users_label.pack()

        # Lista para mostrar los usuarios
        self.users_listbox = tk.Listbox(self.main_frame, width=30)
        self.users_listbox.pack()

        # Generar código de sala al azar
        self.room_code = self.generate_room_code()

        # Etiqueta para mostrar el código de sala generado
        self.room_code_label = tk.Label(self.main_frame, text=f"Código de Sala: {self.room_code}")
        self.room_code_label.pack()

        # Botón para crear sala
        self.create_room_button = tk.Button(self.main_frame, text="Crear Sala", command=self.create_room)
        self.create_room_button.pack(pady=10)

    def create_room(self):
        # Aquí iría la lógica para agregar la sala y manejar los usuarios
        # Por ahora, simplemente ejecutamos el juego Pictionary
        subprocess.run(["python", "pictionary_game.py"])

    def generate_room_code(self):
        # Generar un código de sala al azar con el formato (letra, 3 números, letra)
        letters = string.ascii_letters
        random_letter1 = random.choice(letters)
        random_letter2 = random.choice(letters)
        numbers = ''.join(random.choices(string.digits, k=3))
        room_code = f"{random_letter1}{numbers}{random_letter2}"
        return room_code

def main():
    root = tk.Tk()
    app = CreateRoomScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
