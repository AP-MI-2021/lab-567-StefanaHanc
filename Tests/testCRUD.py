from Domain.calculatoare import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaCalculator, getById, stergeCalculator
from UI.console import uiAdaugaCalculator


def testAdaugaCalculator():
    lista=[]
    lista=adaugaCalculator("1","Lenovo","Windows 10",2400.23,"Cluj",lista)
    assert getId(getById("1",lista))=="1"
    assert getNume(lista[0]) == "Lenovo"
    assert getDescriere(lista[0])=="Windows 10"
    assert getPret(lista[0]) == 2400.23
    assert getLocatie(lista[0]) == "Cluj"

def testStergereCalculator():
    lista=[]
    lista=adaugaCalculator("1","Lenovo","Windows 10",2400.23,"Cluj",lista)
    lista=adaugaCalculator("2","Lenovo","Windows 11",4400,"Cluj",lista)
    lista=stergeCalculator("1",lista)
    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2",lista) is not None

def testUndo():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
    lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
    rezultat=uiAdaugaCalculator(lista,undo,redo)
    assert len(rezultat)==1

