import tkinter as tk

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=50, pady=20)

        # Campos de entrada para usuario y contraseña
        self.username_label = tk.Label(self.main_frame, text="Usuario:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.main_frame, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)

        # Botón de inicio de sesión
        self.login_button = tk.Button(self.main_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=10)

        # Botón de registro
        self.register_button = tk.Button(self.main_frame, text="Registrarse", command=self.register)
        self.register_button.pack(pady=5)

    def login(self):
        self.root.destroy()
        import main_menu  
        root = tk.Tk()
        app = main_menu.MainMenu(root)

    def register(self):
        self.root.destroy()
        import registration_screen
        root = tk.Tk()
        app = registration_screen.RegistrationScreen(root)

def main():
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
