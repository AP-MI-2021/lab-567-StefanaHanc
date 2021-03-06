from Domain.calculatoare import creeazaCalculator, getId, getLocatie


def adaugaCalculator(id,nume,descriere,pret,locatie,lista):
    """
    Adauga un calculator in lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista:
    :return: Retuneaza o lista continand elementele vechii cat si noua prajitura
    """
    if getById(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    calculator=creeazaCalculator(id,nume,descriere,pret,locatie)
    return lista+[calculator]

def adaugaCalculatorUndoRedo(id,nume,descriere,pret,locatie,lista,undoList,redoList):
    """
    Adauga un calculator in lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista:
    :return: Retuneaza o lista continand elementele vechii cat si noua prajitura
    """
    if getById(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    calculator=creeazaCalculator(id,nume,descriere,pret,locatie)
    undoList.append(lista)
    redoList.clear()
    return lista+[calculator]


def getById(id,lista):
    """
    DA calculatorul cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de calculatoare
    :return:
    """
    for calculator in lista:
        if getId(calculator)==id:
            return calculator
    return None
def getByLocatie(locatie,lista):
    """
    Gaseste calculatorul cu locatia data dintr-o lista
    :param id: string
    :param lista:  lista de calculatoare
    :return:
    """
    for calculator in lista:
        if getLocatie(calculator) == locatie:
            return calculator
    return None


def stergeCalculator(id,lista):
    """
    Sterge calculatorul dupa id
    :param id:
    :param lista:
    :return:
    """
    if getById(id,lista) is None:
        raise ValueError("Nu exista calculatorul cu id-ul dat!")
    return [calculator for calculator in lista if getId(calculator)!=id]


def modificaCalculator(id,nume,descriere,pret,locatie,lista):
    """
    Modifica un calculator dupa id
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: Lista si modificarea facuta
    """
    listaNoua=[]
    for calculator in lista:
        if getId(calculator)==id:
            calculatorNoua=creeazaCalculator(id,nume,descriere,pret,locatie)
            listaNoua.append(calculatorNoua)
        else:
            listaNoua.append(calculator)
    return listaNoua