from dictionary import slownik

def translate(text):
    return slownik.get(text, "Nie znam takiego słowa!")