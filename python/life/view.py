from tkinter import *
import life

wielkosc_komorki = 5
uruchomiony = False


def ustawienia():
    global okno_glowne, widok_siatki, wielkosc_komorki, przycisk_start, przycisk_wyczysc, wybor

    okno_glowne = Tk()
    okno_glowne.title('LIFE')


    # background_image = PhotoImage(file = '4.gif')

    background_label = Label(okno_glowne, image = background_image)
    background_label.image = background_image
    background_label.place(x = 1, y = 1, relwidth = 1, relheight = 1)
    
    widok_siatki = Canvas(okno_glowne, width=life.szer*wielkosc_komorki, height=life.wys*wielkosc_komorki, borderwidth=0, highlightthickness=0)


    przycisk_start = Button(okno_glowne, text='START', width=12, font='Bauer', bd=5, bg='white')
    przycisk_start.bind('<Button-1>', handler_start)
    przycisk_wyczysc = Button(okno_glowne, text='CLEAR', width=12, font='Bauer', bd=5, bg='white')
    przycisk_wyczysc.bind('<Button-1>', handler_wyczysc)

    wybor = StringVar(okno_glowne)
    wybor.set('Wybierz wzorzec')
    opcja = OptionMenu(okno_glowne, wybor, 'Wybierz wzorzec', 'Szybowiec', 'Dzialo/Szybowiec', 'Losowy', command=handler_opcja)
    opcja.config(width=30, font='Bauer', bd=5, bg='white')

    widok_siatki.grid(row=0, columnspan=3, padx=20, pady=20)
    widok_siatki.bind('<Button-1>', handler_siatki)
    przycisk_start.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    opcja.grid(row=1, column=1, padx=20)
    przycisk_wyczysc.grid(row=1, column=2, sticky=E, padx=20, pady=20)

def handler_opcja(zdarzenie):
    global uruchomiony, przycisk_start, wybor

    uruchomiony = False
    przycisk_start.configure(text='START')

    wybrany = wybor.get()

    if wybrany =='Szybowiec':
        life.wczytaj_wzorzec(life.wzorzec_szybowiec, 10, 10)
    elif wybrany == 'Dzialo/Szybowiec':
        life.wczytaj_wzorzec(life.wzorzec_dzialo_szybowiec, 10, 10)
    elif wybrany =='Losowy':
        life.losuj(life.model_siatki, life.szer, life.wys)
    aktualizacja()

def handler_start(zdarzenie):
    global uruchomiony, przycisk_start

    if uruchomiony:
        uruchomiony = False
        przycisk_start.configure(text ='START')
    else:
        uruchomiony = True
        przycisk_start.configure(text='PAUZA')
        aktualizacja()

def handler_wyczysc(zdarzenie):
    global przycisk_start, uruchomiony

    uruchomiony = False
    for i in range(0, life.wys):
        for j in range(0, life.szer):
            life.model_siatki[i][j] = 0
    przycisk_start.configure(text = 'START')
    #life.losuj(life.model_siatki, life.szer, life.wys)
    aktualizacja()

def handler_siatki(zdarzenie):
    global widok_siatki, wielkosc_komorki

    x=int(zdarzenie.x/wielkosc_komorki)
    y=int(zdarzenie.y/wielkosc_komorki)

    if (life.model_siatki[x][y] == 1):
        life.model_siatki[x][y] = 0
        narysuj_komorke(x, y, 'white')
    else:
        life.model_siatki[x][y] = 1
        narysuj_komorke(x, y, 'black')

def aktualizacja():
    global widok_siatki, okno_glowne, uruchomiony

    widok_siatki.delete(ALL)
    life.nastepne_pokolenie()

    for i in range(0, life.wys):
        for j in range(0, life.szer):
            if life.model_siatki[i][j] == 1:
                narysuj_komorke(i, j, 'black')

    if uruchomiony:
        okno_glowne.after(100, aktualizacja)

def narysuj_komorke(rzad, kolumna, kolor):
    global widok_siatki, wielkosc_komorki

    if kolor == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    widok_siatki.create_rectangle(rzad*wielkosc_komorki, kolumna*wielkosc_komorki, rzad*wielkosc_komorki+wielkosc_komorki, kolumna*wielkosc_komorki+wielkosc_komorki, fill = kolor, outline = outline)


if __name__ == '__main__':
    ustawienia()
    aktualizacja()
    mainloop()
