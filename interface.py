from tkinter import *
from tkinter import ttk
from translate import translate
from dictionary import slownik

padding_size = 10

def translate_button():
    textInput = polishWord.get()
    englishWord.set(translate(textInput))

root = Tk()
root.title("Mini Translator v1.0.9")
root.geometry("280x150")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding=5)
mainframe.pack(fill="both", expand=True)

mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=0)

mainframe.grid_rowconfigure(1, weight=1)

polishWord = StringVar()
englishWord = StringVar()

polish_entry = ttk.Entry(mainframe, textvariable=polishWord)
polish_entry.grid(column=0, row=0, columnspan=2, sticky="ew")

# WIERSZ 1
ttk.Label(mainframe, textvariable=englishWord).grid(column=0, row=1, sticky="new")

# WIERSZ 2
ttk.Label(mainframe, text="Polish -> English").grid(column=0, row=2, sticky="e")
ttk.Button(mainframe, text="Translate", command=translate_button).grid(column=1, row=2, sticky="e")

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", lambda event: translate_button())

root.mainloop()