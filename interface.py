from tkinter import *
from tkinter import ttk
from translate import translate

class TranslatorApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Mini Translator v1.0.9")
        self.root.geometry("280x150")
        self.root.resizable(False, False)

        self.is_dark_mode = False

        self.lightMode = {
            'background': 'white',
            'foreground': 'black'
            }

        self.darkMode = {
            'bg': '#333',
            'fg': 'white'
            }

        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="white")

        self.polishWord = StringVar()

        self.englishWord = StringVar()

        self.build_ui()
        self.apply_theme(self.lightMode)

        self.root.bind("<Return>", lambda event: self.translate_word())

    # GUI
    def build_ui(self):
        self.mainframe = ttk.Frame(self.root, padding=5)
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(1, weight=0)

        self.mainframe.grid_rowconfigure(1, weight=1)

        # 1ST ROW
        self.polishEntry = ttk.Entry(self.mainframe, textvariable=self.polishWord)
        self.polishEntry.grid(column=0, row=0, columnspan=2, sticky="ew")

        # 2ND ROW
        self.outputArea = ttk.Label(self.mainframe, textvariable=self.englishWord)
        self.outputArea.grid(column=0, row=1, sticky="new")

        # 3RD ROW
        directionDr = ttk.Label(self.mainframe, text="Polish -> English")
        directionDr.grid(column=0, row=2, sticky="e")

        self.translateButton = ttk.Button(self.mainframe, text="Translate", command=self.translate_word)
        self.translateButton.grid(column=1, row=2, sticky="e")

        # 4TH ROW
        self.themeButton = ttk.Button(self.mainframe, text ="Toggle Theme")
        self.themeButton.grid(column=0, row=3, columnspan=2, sticky="new")

    # THEME
    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_theme(self.lightMode)
            self.is_dark_mode = False
        else:
            self.apply_theme(self.darkMode)
            self.is_dark_mode = True

    def apply_theme(self, theme):
        self.root.config()

    # LOGIC
    def translate_word(self):
        _polishWord = self.polishWord.get()
        _englishWord = self.englishWord.get()
        self.englishWord.set(translate(_polishWord))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TranslatorApp()
    app.run()