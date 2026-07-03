from dictionary import slownik

def translate(textInput):
    return slownik.get(textInput, f"Nie znam takiego słowa!")