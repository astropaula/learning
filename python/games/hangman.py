import random

SZUBIENICA_OBRAZKI=['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
    
slowa = 'baran bocian indyk borsuk bobr fretka ges golab jastrzab jaszczurka jelen kaczka kobra kojot kot koza kret'.split()

def wylosujSlowo(listaSlow):
    indeksSlowa = random.randint(0,len(listaSlow)-1)
    return listaSlow[indeksSlowa]

def wyswietlPlansze(strzalyNiecelne, strzalyCelne, tajneslowo):
   
    #WYSWIETLANIE WISIELCA
    print(SZUBIENICA_OBRAZKI[len(strzalyNiecelne)])
    print()


    #PODANE ZŁE LITERY
    print("Strzaly niecelne:", end=' ')
    

    for litera in strzalyNiecelne:
        print(litera, end=' ')
        

    #SLOWO DO UZUPELNIENIA
    pusteMiejsca = '_' * len(tajneslowo)
    
    #WYPELNIANIE PLANSZY
    for i in range(len(tajneslowo)):
        if tajneslowo[i] in strzalyCelne:
            pusteMiejsca = pusteMiejsca[:i] + tajneslowo[i] + pusteMiejsca[i+1:]
    
    print()
    for litera in pusteMiejsca:
        print(litera, end=' ')
    print()

def wczytajStrzal(juzPodawane):
    while True:
        print('Podaj litere.')
        strzal = input()
        strzal = strzal.lower()
        if len(strzal) != 1:
            print("Prosze podaj jedna litere")
        elif strzal in juzPodawane:
            print("Ta litera juz byla!")
        elif strzal not in 'abcdefghijklmnoprstuwvxyz':
            print("Prosze podac LITERE!")
        else:
            return strzal

def zagrajPonownie():

    print("Chcesz zagrac ponownie? (tak lub nie)")
    return input().lower().startswith('t')

print("S Z U B I E N I C A")
strzalyNiecelne = ''
strzalyCelne = ''
tajneslowo = wylosujSlowo(slowa)
koniecGry = False

while True:
    wyswietlPlansze(strzalyNiecelne, strzalyCelne, tajneslowo)

    strzal = wczytajStrzal(strzalyNiecelne + strzalyCelne)
    
    if strzal in tajneslowo:
        strzalyCelne = strzalyCelne + strzal

        wszystkieodgadniete = True

        for i in range(len(tajneslowo)):
            if tajneslowo[i] not in strzalyCelne:
                wszystkieodgadniete = False
                break
        if wszystkieodgadniete:
            print("TAK! Tajne slowo to " + tajneslowo + "! ZWYCIESTWO!")

            koniecGry = True
    else:
        strzalyNiecelne = strzalyNiecelne + strzal

        if len(strzalyNiecelne) == len(SZUBIENICA_OBRAZKI) - 1:
            wyswietlPlansze(strzalyNiecelne, strzalyCelne, tajneslowo)
            print("Nie masz juz wiecej strzalow :(\nPo" + str(len(strzalyNiecelne)) + "strzalach niecelnych i" + str(len(strzalyCelne)) + "strzalach celnych, tajne slowo to: " + tajneslowo)

            koniecGry = True
    
    if koniecGry:
        if zagrajPonownie():
            strzalyNiecelne = ''
            strzalyCelne = ''
            koniecGry = False
            tajneslowo = wylosujSlowo(slowa)
        else:
            break



    