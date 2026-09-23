import ctypes # window title colors
import os # filepath
import json # metadata

from tkinter import *
from tkinter import ttk
from Translate import translate

class TranslatorApp:
    def __init__(self):
        self.root = Tk()

        metadata = self.get_metadata()

        self.root.title(f"{metadata['name']} v{metadata['version']}")
        self.root.iconbitmap("open_book_icon.ico")
        self.root.geometry("280x150")
        self.root.resizable(False, False)

        self.is_dark_mode = False

        self.lightMode = {
            'bg': '#FFFFFF',
            'fg': '#000000',
            'bc' : '#D3D3D3',
            'hv' : '#D3D3D3'
            }

        self.darkMode = {
            'bg': '#333333',
            'fg': '#FFFFFF',
            'bc' : '#7d7d7d',
            'hv' : '#808080'
            }

        self.style = ttk.Style()

        self.polishWord = StringVar()

        self.englishWord = StringVar()

        self.style.theme_use("clam")

        self.apply_theme(self.lightMode)
        self.build_ui()

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
        self.themeButton = ttk.Button(self.mainframe, text="Toggle Theme", command=self.toggle_theme)
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
        self.root.config(bg=theme['bg'])
        self.style.configure("TFrame", background=theme['bg'], bordercolor=theme['bc'], lightcolor=theme['bc'], darkcolor=theme['bc'])
        self.style.configure("TLabel", background=theme['bg'], foreground=theme['fg'], bordercolor=theme['bc'], lightcolor=theme['bc'], darkcolor=theme['bc'])
        self.style.configure("TButton", background=theme['bg'], foreground=theme['fg'], bordercolor=theme['bc'], lightcolor=theme['bc'], darkcolor=theme['bc'])
        self.style.configure("TEntry", fieldbackground=theme['bg'], foreground=theme['fg'], bordercolor=theme['bc'], lightcolor=theme['bc'], darkcolor=theme['bc'])

        self.style.map(
        "TButton",
        background=[
            ("active", theme['hv'])
        ]
        )

        self.style.configure(
        "TEntry",
        fieldbackground=theme['bg'],
        foreground=theme['fg'],
        bordercolor=theme['bc'],
        lightcolor=theme['bc'],
        darkcolor=theme['bc']
        )

        # WINDOWS TITLE BAR

        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())

        color = theme['bg'].lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)

        dwmapi = ctypes.windll.dwmapi
        dwmapi.DwmSetWindowAttribute(
            hwnd,
            35,
            ctypes.byref(ctypes.c_int(r | (g << 8) | (b << 16))),
            ctypes.sizeof(ctypes.c_int)
        )

    # LOGIC
    def translate_word(self):
        _polishWord = self.polishWord.get()
        _englishWord = self.englishWord.get()
        self.englishWord.set(translate(_polishWord))

    # METADATA
    def get_metadata(self):
        path = os.path.join(os.path.dirname(__file__), "metadata.json")

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TranslatorApp()
    app.run()