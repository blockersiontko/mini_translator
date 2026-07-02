from tkinter import *
from tkinter import ttk
from Translate import translate
from dictionary import slownik

def translate_button():
    text = polishWord.get()
    englishWord.set(translate(text))

root = Tk()
root.title("Mini Translator v1.0.8")

mainframe = ttk.Frame(root, padding=(3, 3, 12 ,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

polishWord = StringVar()
polish_entry = ttk.Entry(mainframe, width=7, textvariable=polishWord)
polish_entry.grid(column=2, row=1, sticky=(W, E))

englishWord = StringVar()
ttk.Label(mainframe, textvariable=englishWord).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Translate", command=translate_button).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Polski").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="↓").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="English").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
polish_entry.focus()
root.bind("<Return>", lambda event: translate_button())

root.mainloop()