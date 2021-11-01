from Domain.calculatoare import getId, getLocatie
from Logic.CRUD import adaugaCalculator
from Logic.functionalitate import maxPretPerLocatie, ordonareDupaPret, modificaLocatia


def testMaxPretPerLocatie():
    lista=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400.23, "Sv", lista)
    rezultat=maxPretPerLocatie(lista)
    assert len(rezultat)==2
    assert rezultat["Cluj"]==4400
    assert rezultat["Sv"]==2400.23

def testOrdonareDupaPret():
    lista=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=ordonareDupaPret(lista)
    assert getId(rezultat[0])=="3"
    assert getId(rezultat[1]) == "1"
    assert getId(rezultat[2]) == "2"

def testModificareLocatie():
    lista=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=modificaLocatia("Cluj","Mures",lista)
    assert getLocatie(rezultat[0]) == "Mures"
    assert getLocatie(rezultat[1])=="Mures"
    assert getLocatie(rezultat[2]) == "Sv"