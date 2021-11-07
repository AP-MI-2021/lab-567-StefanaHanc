import copy

from Domain.calculatoare import toString
from Logic.CRUD import adaugaCalculator, stergeCalculator, modificaCalculator
from Logic.functionalitate import maxPretPerLocatie, ordonareDupaPret, modificaLocatia, afisareaSumelorPerLocatie, \
    cacontereaStringLaDescriere


def printMenu():
    print("MENIU")
    print("1.Adauga calculator ")
    print("2.Stergere calculator")
    print("3.Modificare calculator")
    print("4.Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație.")
    print("7. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("8.Ordonarea obiectelor crescător după prețul de achiziție")
    print("a.Arata lista")
    print("u.Undo")
    print("r. Redo")
    print("9.Iesire")


def uiAdaugaCalculator(lista, undoList,redoList):
    try:
        id=input("Dati id-ul:")
        nume = input("Dati numele:")
        descriere = input("Dati descrierea:")
        pret= float(input("Dati pretul: "))
        locatie=input("Dati locatia:")
        rezultat=adaugaCalculator(id,nume,descriere,pret,locatie,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereCalculator(lista,undoList,redoList):
    try:
        id=input("Dati id-ul de sters: ")
        rezultat=stergeCalculator(id,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaCalculator(lista,undoList,redoList):
    try:
        id = input("Dati id-ul calculatorului pe are doriti sa il modificati: ")
        nume = input("Dati numele nou: ")
        descriere = input("Dati descrierea noua: ")
        pret = float(input("Dati pretul nou: "))
        locatie = input("Dati locatia noua: ")
        rezultat=modificaCalculator(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiShowLista(lista):
    for calculator in lista:
        print(toString(calculator))


def uiMaxPretPerLocatie(lista):
    rezultat=maxPretPerLocatie(lista)
    for locatie in rezultat:
        print("Pretul maxim {} se gaseste in locatia {}".format(rezultat[locatie],locatie))


def uiAfisareaSumelorPerLocatie(lista):
    rezultat=afisareaSumelorPerLocatie(lista)
    for locatia in rezultat:
        print("Suma preturilor pentru locatia {} este {}".format(locatia,rezultat[locatia]))


def runMenu(lista):
    undoList= []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati opiune: ")
        if optiune == "1":
            lista = uiAdaugaCalculator(lista,undoList,redoList)
        elif optiune=="2":
            lista=uiStergereCalculator(lista,undoList,redoList)
        elif optiune=="5":
            descriereadaugata=input("Dati descrierea pe care o doriti sa o adaugati: ")
            pretcitit=float(input("Dati pretul: "))
            lista=cacontereaStringLaDescriere(descriereadaugata,pretcitit,lista,undoList,redoList)
        elif optiune=="3":
            lista=uiModificaCalculator(lista)
        elif optiune=="a":
            uiShowLista(lista)
        elif optiune=="4":
            adresaCautata=input("Dati adresa initiala a obiectelor: ")
            adresaNoua=input("Dati noua adresa a obiectelor: ")
            lista =modificaLocatia(adresaCautata, adresaNoua, lista,undoList,redoList)
        elif optiune=="6":
            uiMaxPretPerLocatie(lista)
        elif optiune=="7":
            uiAfisareaSumelorPerLocatie(lista)
        elif optiune=="8":
            lista=ordonareDupaPret(lista,undoList,redoList)
        elif optiune == "u":
            if len(undoList)>0:
                redoList.append(lista)
                lista=undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList)>0:
                undoList.append(lista)
                lista=redoList.pop()
            else:
                print("Nu se poate face redo! ")
        elif optiune=="9":
            break
        else:
            print("Optiune gresita!")