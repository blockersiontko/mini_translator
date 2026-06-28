slownik = {
    "kot" : "cat",
    "pies" : "dog",
    "panda" : "panda",
    "lis" : "fox",
    "wilk" : "wolf",
    "wąż" : "snake",
    "niedźwiedź"  : "bear"
}

userInput = input("Wpisz nazwę zwierzęcia po polsku: ")

cAP = "'"
cDT = "."

while userInput not in slownik:
    print("Nie ma tego słowa w moim słowniku!")
    userInput = input("Wpisz nazwę zwierzęcia po polsku: ")
    s_userInput = str(userInput)
else:
    wartosc = slownik[userInput]
    s_userInput = str(userInput)
    s_wartosc = str(wartosc)
    print("Zwierzę " + cAP + s_userInput + cAP + " nazywa się po angielsku " + cAP + s_wartosc + cAP + cDT)