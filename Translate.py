from dictionary import slownik

def translate(_polishWord):
    return slownik.get(_polishWord, f"Nie znam takiego słowa!")