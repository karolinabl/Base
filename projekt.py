import sqlite3    #import biblioteki bazy
from tkinter import * #import GUI

class Pociag:  #deklaracja klasy
    def __init__(self, rodzaj, nrpociagu):  #konstruktor
        self.rodzaj=rodzaj
        self.nrpociagu=nrpociagu

    
    def wypisz(self): #metoda wypisz
        wynik=uchwyt.execute("SELECT * From Pociag") #zapytanie do bazy
        for rekord in wynik: #petla
            print("Rodzaj pociagu: ", rekord[0])
            print("Numer pociagu: ", rekord[1])
            print()   

    def zapisz(self): #metoda zapisz
        rodzaj = self.rodzaj
        nrpociagu = self.nrpociagu
        polecenie="INSERT INTO Pociag(nrpociagu, rodzaj) VALUES ("+"'"+rodzaj+"','"+nrpociagu+"')" #zapytanie do bazy
        print(polecenie)
        uchwyt.execute(polecenie)
        polaczenie.commit()        
    

z=Pociag(0,0) #deklaracja obiektu
polaczenie=sqlite3.connect('Pociag.db') #import bazy
uchwyt=polaczenie.cursor() #import bazy

def wypisz(zdarzenie): #metoda do obslugi przycisku wypisz
    z.wypisz() #obiekt wywoluje metode zapisz

def zapisz(zdarzenie): #metoda do obslugi przycisku zapisz
    p2=pole1.get() #pobieranie wartosci z pola 1
    p1=pole2.get() #pobieranie wartosci z pola 2
    z=Pociag(p1, p2) #deklaracja konstruktora
    z.zapisz()



            #od tad do konca to juz samo GUI(pola, przyciski, etykiety, okna)

glowna=Tk()
ramka1=Frame(glowna)
ramka1.pack(side=TOP)
etykieta1=Label(ramka1, text="Podaj rodzaj pociagu:")
etykieta1.pack(side=LEFT)
pole1=Entry(ramka1)
pole1.pack(side=RIGHT)

ramka3=Frame(glowna)
ramka3.pack(side=TOP)


etykieta2=Label(ramka3, text="Podaj numer pociagu:")
etykieta2.pack(side=LEFT)
pole2=Entry(ramka3)
pole2.pack(side=RIGHT)

ramka2=Frame(glowna)
ramka2.pack(side=BOTTOM)
przycisk1=Button(ramka2, text="Wypisz")
przycisk1.pack(side=LEFT)
przycisk1.bind("<Button>",wypisz)
przycisk2=Button(ramka2, text="Zapisz")
przycisk2.pack(side=RIGHT)
przycisk2.bind("<Button>",zapisz)

glowna.mainloop()
