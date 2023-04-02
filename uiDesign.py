import tkinter as tk

BG = '#FFFBF5'


class Gui:
    def __init__(self, t_cmd, f_cmd):
        # Quiz screen.
        self.screen = tk.Tk()
        # Title name.
        self.screen.title('Quiz System')
        # No resizable.
        self.screen.resizable(False, False)
        # icon
        icon = tk.PhotoImage(file='icon.png')
        self.screen.iconphoto(False, icon)
        # Geometry.
        self.screen.configure(padx=20, pady=20, bg=BG)
        # Score label.
        self.score_label = tk.Label(text='Score = 0', bg=BG, font=('fantasy', 16, 'bold'), foreground='grey')
        self.score_label.grid(row=0, column=1, padx=(100, 0))
        # Question showing canvas.
        self.canvas = tk.Canvas(height=300, width=250, bg="#674188")
        # Question label.
        # Images
        true_image = tk.PhotoImage(file='true_image.png')
        false_image = tk.PhotoImage(file='false_button.png')

        # Griding canvas.
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        # True button:
        self.true_button = tk.Button(image=true_image, highlightthickness=0, borderwidth=0, bg=BG, command=t_cmd)
        self.true_button.grid(row=3, column=0)
        # False button:
        self.false_button = tk.Button(image=false_image, highlightthickness=0, borderwidth=0, bg=BG, command=f_cmd)
        self.false_button.grid(row=3, column=1, padx=(150, 0))
        # Keep alive screen.
        self.screen.mainloop()

    def show_question(self, question):
        self.canvas.create_text(
            150,  # height
            125,  # width
            text=f'{question}',
            font=('Times New Roman', 16),
            fill='black',
            width=200  # to wrap text

        )
