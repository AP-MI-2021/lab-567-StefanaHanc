from Domain.calculatoare import getId, getLocatie, getDescriere
from Logic.CRUD import adaugaCalculator
from Logic.functionalitate import maxPretPerLocatie, ordonareDupaPret, modificaLocatia, afisareaSumelorPerLocatie, \
    cacontereaStringLaDescriere


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
    undo=[]
    redo=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=ordonareDupaPret(lista,undo,redo)
    assert getId(rezultat[0])=="3"
    assert getId(rezultat[1]) == "1"
    assert getId(rezultat[2]) == "2"

def testModificareLocatie():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=modificaLocatia("Cluj","Mures",lista,undo,redo)
    assert getLocatie(rezultat[0]) == "Mures"
    assert getLocatie(rezultat[1])=="Mures"
    assert getLocatie(rezultat[2]) == "Sv"

def testAfisareaSumelorPerLocatie():
    lista=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=afisareaSumelorPerLocatie(lista)
    assert rezultat["Cluj"]==6800.23
    assert rezultat["Sv"]==2400
    assert len(rezultat)==2

def testConcantenareString():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
    rezultat=cacontereaStringLaDescriere(" Windows 10",2400,lista,undo,redo)
    assert getDescriere(rezultat[0])=="Windows 10 Windows 10"