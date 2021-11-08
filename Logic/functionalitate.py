from Domain.calculatoare import getLocatie, getPret, getId, getNume, getDescriere, creeazaCalculator
from Logic.CRUD import getByLocatie


def maxPretPerLocatie(lista):
    """
        Determinarea celui mai mare preț pentru fiecare locație.
        :param lista: Lista verificata
        :return:Lista cu cele mai mari preturi pentru locatii
    """
    rezultat = {}
    for calculator in lista:
        locatie=getLocatie(calculator)
        pret=getPret(calculator)
        if locatie in rezultat:
            if pret>rezultat[locatie]:
                rezultat[locatie]=pret
        else:
            rezultat[locatie]=pret
    return rezultat


def afisareaSumelorPerLocatie(lista):
    """
        Afișarea sumelor prețurilor pentru fiecare locație
        :param lista:
        :return:Un dictionar nou
    """
    rezultat={}
    for calculator in lista:
        locatie=getLocatie(calculator)
        pret=getPret(calculator)
        if locatie in rezultat:
            rezultat[locatie]=rezultat[locatie]+pret
        else:
            rezultat[locatie]=pret
    return rezultat


def ordonareDupaPret(lista,undoList,redoList):
    """
         Ordonarea obiectelor crescător după prețul de achiziție.
        :param lista: Lista are trebuie sortata
        :return : Lista sortata
    """
    undoList.append(lista)
    redoList.clear()
    return sorted(lista,key=lambda calculator:getPret(calculator))


def modificaLocatia(adresaCautata,adresanoua,lista,undoList,redoList):
    """
         Mutarea tuturor obiectelor dintr-o locație în alta.
        :param adresaCautata: string
        :param adresanoua:string
        :param lista:adresa verificata
        :return:noua lista cu locatia modificata
    """
    if getByLocatie(adresaCautata, lista) is None:
        raise ValueError("Nu exista calculatorul cu locatia data!")
    listaNoua=[]
    for calculator in lista:
        id =getId(calculator)
        nume =getNume(calculator)
        descriere =getDescriere(calculator)
        pret = getPret(calculator)
        locatia = getLocatie(calculator)
        if locatia == adresaCautata :
            calculatorNoua = creeazaCalculator(id, nume, descriere, pret, adresanoua)
            listaNoua.append(calculatorNoua)
        else:
            listaNoua.append(calculator)
    undoList.append(lista)
    redoList.clear()
    return listaNoua


def cacontereaStringLaDescriere(substringdesc,pretcitit,lista,undoList,redoList):
    listaNoua = []
    for calculator in lista:
        if pretcitit <getPret(calculator):
            calculatorNou= creeazaCalculator(
                getId(calculator),
                getNume(calculator),
                getDescriere(calculator)+substringdesc,
                getPret(calculator),
                getLocatie(calculator)

            )
            listaNoua.append(calculatorNou)
        else:
            listaNoua.append(calculator)
    undoList.append(lista)
    redoList.clear()
    return listaNoua

def Undo(lista,undolist,redolist):
    if len(undolist)>0:
        redolist.append(lista)
        lista = undolist.pop()
    else:
        return None
    return lista

def Redo(lista,undolist,redolist):
    if len(redolist) > 0:
        undolist.append(lista)
        lista = redolist.pop()
    return lista