from Domain.calculatoare import getId, getLocatie, getDescriere
from Logic.CRUD import adaugaCalculator, adaugaCalculatorUndoRedo
from Logic.functionalitate import maxPretPerLocatie, ordonareDupaPret, modificaLocatia, afisareaSumelorPerLocatie, \
    cacontereaStringLaDescriere, Undo, Redo


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

def testUndoRedo():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaCalculatorUndoRedo("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista,undo,redo)
    lista = adaugaCalculatorUndoRedo("2", "Lenovo", "Windows 11", 4400, "Cluj", lista,undo,redo)
    lista = adaugaCalculatorUndoRedo("3", "Lenovo", "Windows 11", 4400, "Cluj", lista, undo, redo)
    assert lista==[{'id': '1', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'}, {'id': '2', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}, {'id': '3', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}]
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'}, {'id': '2', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}]
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista = Undo(lista, undo, redo)
    assert lista ==[]
    lista = Undo(lista, undo, redo)
    assert lista is None
    undo=[]
    redo=[]
    lista=[]
    lista = adaugaCalculatorUndoRedo("4", "Lenovo", "Windows 10", 2400.23, "Cluj", lista, undo, redo)
    lista = adaugaCalculatorUndoRedo("5", "Lenovo", "Windows 11", 4400, "Cluj", lista, undo, redo)
    lista = adaugaCalculatorUndoRedo("6", "Lenovo", "Windows 11", 4400, "Cluj", lista, undo, redo)
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                   {'id': '5', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'},
                   {'id': '6', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}]
    lista = Undo(lista, undo, redo)
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                   {'id': '5', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}]
    lista = Redo(lista, undo, redo)
    assert lista == [{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                     {'id': '5', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'},
                     {'id': '6', 'nume': 'Lenovo', 'descriere': 'Windows 11', 'pret': 4400, 'locatie': 'Cluj'}]
    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista=adaugaCalculatorUndoRedo("7", "MAC", "IOS", 2400.23, "Cluj", lista, undo, redo)
    assert lista==[{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                   {'id': '7', 'nume': 'MAC', 'descriere': 'IOS', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                     {'id': '7', 'nume': 'MAC', 'descriere': 'IOS', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista = Undo(lista, undo, redo)
    assert lista == [{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista = Undo(lista, undo, redo)
    assert lista == []
    lista=Redo(lista,undo,redo)
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                     {'id': '7', 'nume': 'MAC', 'descriere': 'IOS', 'pret': 2400.23, 'locatie': 'Cluj'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '4', 'nume': 'Lenovo', 'descriere': 'Windows 10', 'pret': 2400.23, 'locatie': 'Cluj'},
                     {'id': '7', 'nume': 'MAC', 'descriere': 'IOS', 'pret': 2400.23, 'locatie': 'Cluj'}]