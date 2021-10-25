from Domain.calculatoare import toString
from Logic.CRUD import adaugaCalculator, stergeCalculator, modificaCalculator


def printMenu():
    print("MENIU")
    print("1.Aduaga calculator ")
    print("2.Stergere calculator")
    print("3.Modificare calculator")
    print("a.Arata lista")
    print("4.Mutarea tuturor calculatoarelor dintr-o locatie in alta")
    print("5.Iesire")


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
        elif optiune=="5":
            break
        else:
            print("Optiune gresita!")