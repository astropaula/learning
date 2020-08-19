import random

wys = 100
szer = 100

def losuj(siatka,szer,wys):
    for i in range(0,wys):
        for j in range(0,szer):
            siatka[i][j] = random.randint(0,1)

model_siatki = [0]*wys
nastepny_model_siatki = [0]*wys

for i in range(wys):
    model_siatki[i]=[0]*szer
    nastepny_model_siatki[i]=[0]*szer

#losuj(model_siatki, szer, wys)
#print(model_siatki)

def nastepne_pokolenie():
    global model_siatki, nastepny_model_siatki

    for i in range(0,wys):
        for j in range(0,szer):
            komorka=0
            licznik=policz_sasiadow(model_siatki, i, j)

            if model_siatki[i][j] == 0:
                if licznik == 3:
                    komorka = 1
            elif model_siatki[i][j] == 1:
                if licznik == 2 or licznik == 3:
                    komorka = 1
            nastepny_model_siatki[i][j] = komorka

    #print(nastepny_model_siatki)
    tymczasowa=model_siatki
    model_siatki=nastepny_model_siatki
    nastepny_model_siatki=tymczasowa


def policz_sasiadow(siatka,rzad,kolumna):
   licznik = 0
   if rzad-1 >= 0:
       licznik = licznik + siatka[rzad-1][kolumna]
   if (rzad-1 >= 0) and (kolumna-1 >= 0):
       licznik = licznik + siatka[rzad-1][kolumna-1]
   if (rzad-1 >= 0) and (kolumna+1 < szer):
       licznik = licznik + siatka[rzad-1][kolumna+1]
   if kolumna-1 >= 0:
       licznik = licznik + siatka[rzad][kolumna-1]
   if kolumna + 1 < szer:
       licznik = licznik + siatka[rzad][kolumna+1]
   if rzad + 1 < wys:
       licznik = licznik + siatka[rzad+1][kolumna]
   if (rzad + 1 < wys) and (kolumna-1 >= 0):
       licznik = licznik + siatka[rzad+1][kolumna-1]
   if (rzad + 1 < wys) and (kolumna+1 < szer):
       licznik = licznik + siatka[rzad+1][kolumna+1]
   return licznik

wzorzec_szybowiec = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0],[0, 0, 0, 1, 0],[0, 1, 1, 1, 0],[0, 0, 0, 0, 0]]

wzorzec_dzialo_szybowiec = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def wczytaj_wzorzec(wzorzec, odstep_x=0, odstep_y=0):
    global model_siatki

    for i in range(0, wys):
        for j in range(0, szer):
            model_siatki[i][j] = 0

    j = odstep_y

    for rzad in wzorzec:
        i = odstep_x
        for wartosc in rzad:
            model_siatki[i][j] = wartosc
            i = i+1
        j=j+1

if __name__ == '__main__':
    nastepne_pokolenie()
        
        
    
