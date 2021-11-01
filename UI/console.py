import copy

from Domain.calculatoare import toString
from Logic.CRUD import adaugaCalculator, stergeCalculator, modificaCalculator
from Logic.functionalitate import maxPretPerLocatie, ordonareDupaPret, modificaLocatia


def printMenu():
    print("MENIU")
    print("1.Adauga calculator ")
    print("2.Stergere calculator")
    print("3.Modificare calculator")
    print("4.Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5. Determinarea celui mai mare preț pentru fiecare locație.")
    print("6.Ordonarea obiectelor crescător după prețul de achiziție")
    print("a.Arata lista")
    print("7.Iesire")


def uiAdaugaCalculator(lista):
    id=input("Dati id-ul:")
    nume = input("Dati numele:")
    descriere = input("Dati descrierea:")
    pret= float(input("Dati pretul: "))
    locatie=input("Dati locatia:")
    return adaugaCalculator(id,nume,descriere,pret,locatie,lista)


def uiStergereCalculator(lista):
    id=input("Dati id-ul stergerii de sters: ")
    return stergeCalculator(id,lista)


def uiModificaCalculator(lista):
    id = input("Dati id-ul nou:")
    nume = input("Dati numele nou:")
    descriere = input("Dati descrierea noua:")
    pret = float(input("Dati pretul nou: "))
    locatie = input("Dati locatia noua:")
    return modificaCalculator(id, nume, descriere, pret, locatie, lista)



def uiShowLista(lista):
    for calculator in lista:
        print(toString(calculator))

def uiMaxPretPerLocatie(lista):
    rezultat=maxPretPerLocatie(lista)
    for locatie in rezultat:
        print("Pretul maxim {} se gaseste in locatia {}".format(rezultat[locatie],locatie))



def runMenu(lista):
    while True:
        printMenu()
        optiune=input("Dati opiune: ")
        if optiune=="1":
            lista=uiAdaugaCalculator(lista)
        elif optiune=="2":
            lista=uiStergereCalculator(lista)
        elif optiune=="3":
            lista=uiModificaCalculator(lista)
        elif optiune=="a":
            uiShowLista(lista)
        elif optiune=="4":
            adresaCautata=input("Dati adresa initiala a obiectelor")
            adresaNoua=input("Dati noua adresa a obiectelor")
            lista =modificaLocatia(adresaCautata, adresaNoua, lista)

        elif optiune=="5":
            uiMaxPretPerLocatie(lista)
        elif optiune=="6":
            ordonareDupaPret(lista)
        elif optiune=="7":
            break
        else:
            print("Optiune gresita!")