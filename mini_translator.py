slownik = {
    "kot" : "cat",
    "pies" : "dog",
    "panda" : "panda",
    "lis" : "fox",
    "wilk" : "wolf",
    "wąż" : "snake",
    "niedźwiedź"  : "bear",
    "koń" : "horse",
    "konik morski" : "seahorse",
    "ryba" : "fish"
}

userInput = input("Wpisz nazwę zwierzęcia po polsku: ").lower()

cAP = "'"
cDT = "."

while userInput.lower() not in slownik:
    print("Nie ma tego słowa w moim słowniku!")
    userInput = input("Wpisz nazwę zwierzęcia po polsku: ").lower()
    s_userInput = str(userInput)
else:
    wartosc = slownik[userInput.lower()]
    s_userInput = str(userInput)
    s_wartosc = str(wartosc)
    print("Zwierzę " + cAP + s_userInput + cAP + " nazywa się po angielsku " + cAP + s_wartosc + cAP + cDT)