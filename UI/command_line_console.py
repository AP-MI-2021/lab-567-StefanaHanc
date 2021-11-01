from Domain.calculatoare import toString
from Logic.CRUD import adaugaCalculator, modificaCalculator


def adaugare_Calculator(id,nume,descriere,pret,locatie,lista):
    try:
        return adaugaCalculator(id,nume,descriere,pret,locatie,lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def modificare(id,nume,descriere,pret,locatie,lista):
    try:
        return modificaCalculator(id,nume,descriere,pret,locatie,lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista



def afisare_toate(lista):
    for calculator in lista:
        print(toString(calculator))


def ajutor():
    print("Legenda comenzilor:")
    print("add -> adaugare cheltuiala")
    print("update -> modificare cheltuiala")
    print("show_all -> afisarea tuturor cheltuielilor")
    print("stop -> oprirea programului")


def meniu():
    lista = []
    merge=True
    while merge is True:
        text = input("Intorduceti comanda: ")
        comandalista = text.split("-")
        for optiune in comandalista:
            comanda=optiune.split(";")
        if comanda[0] == "add":
            lista = adaugare_Calculator(int(comanda[1]), (comanda[2]), (comanda[3]), int(comanda[4]), comanda[5], lista)
        elif comanda[0] == "update":
            lista = modificare(int(comanda[1]), (comanda[2]), (comanda[3]), int(comanda[4]), comanda[5], lista)
        elif comanda[0] == "show_all":
            afisare_toate(lista)
        elif comanda[0] == "help":
            ajutor()
        elif comanda[0] == "stop":
            merge = False
        else:
            print("Comanda gresita! Incercati din nou!")


meniu()