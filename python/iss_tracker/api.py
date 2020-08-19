import requests, json, turtle

iss=turtle.Turtle()

def ustawienia(okno):
    global iss
    okno.setup(1000,500)
    okno.bgpic('earth.gif')
    okno.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")

def rusz_iss(dlugosc, szerokosc):
    global iss
    #iss.penup()
    iss.goto(szerokosc, dlugosc)
    iss.pendown()
    
def ustaw_iss():
    url='http://api.open-notify.org/iss-now.json'
    odpowiedz=requests.get(url)

    if(odpowiedz.status_code == 200):

        odpowiedz_slownik = json.loads(odpowiedz.text)
        polozenie = odpowiedz_slownik['iss_position']
        dlugosc = float(polozenie['latitude'])
        szerokosc = float(polozenie['longitude'])
        iss.penup()
        iss.goto(szerokosc, dlugosc)

 

def sledz_iss():
    url='http://api.open-notify.org/iss-now.json'
    odpowiedz=requests.get(url)

    if(odpowiedz.status_code == 200):

        odpowiedz_slownik = json.loads(odpowiedz.text)
        polozenie = odpowiedz_slownik['iss_position']
        #print('Współrzędne ISS to ' + polozenie['latitude'] + ' ,' + polozenie['longitude'])
        dlugosc = float(polozenie['latitude'])
        szerokosc = float(polozenie['longitude'])
        rusz_iss(dlugosc, szerokosc)

    else:
        print("Houston, mamy problem:", odpowiedz.status_code)

    widget=turtle.getcanvas()
    widget.after(500, sledz_iss)

def main():
    global iss
    ekran = turtle.Screen()
    ustawienia(ekran)
    ustaw_iss()
    sledz_iss()

if __name__=="__main__":
    main()
    turtle.mainloop()
