import tkinter as tk
from main_menu import MainMenu  

class RegistrationScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro")

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=50, pady=20)

        # Campos de entrada para nombre, nombre de usuario, correo y contraseña
        self.name_label = tk.Label(self.main_frame, text="Nombre:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack(pady=5)

        self.username_label = tk.Label(self.main_frame, text="Nombre de usuario:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        self.email_label = tk.Label(self.main_frame, text="Correo electrónico:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.pack(pady=5)

        self.password_label = tk.Label(self.main_frame, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        # Botón de registro
        self.register_button = tk.Button(self.main_frame, text="Registrarse", command=self.register)
        self.register_button.pack(pady=10)

    def register(self):
        self.root.destroy()  # Cerrar la ventana de registro
        root = tk.Tk()
        app = MainMenu(root)  # Mostrar la pantalla de inicio de sesión
        root.mainloop()

def main():
    root = tk.Tk()
    app = RegistrationScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
