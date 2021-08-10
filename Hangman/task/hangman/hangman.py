from random import choice


def izaberi_rec():
    lista = ['python', 'java', 'kotlin', 'javascript']
    return choice(lista)


def sredi_ispis(lista, rec, slovo):
    brojac = 0
    ispis = ''
    for i in rec:
        if brojac in lista:
            ispis += slovo
            brojac += 1
            continue
        ispis += i
        brojac += 1
    return ispis


def pogadjaj():
    zivot_moj = 8
    za_pogadjanje = izaberi_rec()
    ispis = ''
    for i in za_pogadjanje:
        ispis += '-'
    flag = True
    indeksi = []
    slova = []
    while flag:
        print()
        print(ispis)
        slovo = input(f"Input a letter: ")
        if len(slovo) != 1:
            print("You should input a single letter")
            continue
        if not (slovo.islower()):
            print("Please enter a lowercase English letter")
            continue
        if slovo in slova:
            print("You've already guessed this letter")
        elif slovo in za_pogadjanje:
            while za_pogadjanje.count(slovo) != 0:
                ind = za_pogadjanje.index(slovo)
                indeksi.append(ind)
                za_pogadjanje = za_pogadjanje.replace(slovo, '!', 1)
            ispis = sredi_ispis(indeksi, ispis, slovo)
            indeksi.clear()
        else:
            zivot_moj -= 1
            print("That letter doesn't appear in the word")
        if zivot_moj == 0:
            flag = False
            print("You lost!")
        if za_pogadjanje.count('!') == len(za_pogadjanje):
            flag = False
            print("You survived!")
        slova.append(slovo)


print("H A N G M A N")
while True:
    igraj = input('Type "play" to play the game, "exit" to quit: ')
    if igraj == 'play':
        pogadjaj()
    if igraj == 'exit':
        break


