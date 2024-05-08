import tkinter as tk
from pictionary_game import PictionaryGame
from login_screen import LoginScreen

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
        
        game_window = tk.Toplevel(self.root)
        pictionary_game = PictionaryGame(game_window)

    def login(self):
        login_screen = LoginScreen(tk.Toplevel(self.root))
        

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
