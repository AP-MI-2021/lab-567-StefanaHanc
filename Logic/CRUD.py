from Domain.calculatoare import creeazaCalculator, getId


def adaugaCalculator(id,nume,descriere,pret,locatie,lista):
    """
    Adauga un ccalculator in lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista:
    :return: Retuneaza o lista continand elementele vechii cat si noua prajitura
    """
    calculator=creeazaCalculator(id,nume,descriere,pret,locatie)
    return lista+[calculator]

def getById(id,lista):
    """
    DA alculatorul cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de calculatoare
    :return:
    """
    for calculator in lista:
        if getId(calculator)==id:
            return calculator
    return None

def stergeCalculator(id,lista):
    """
    Sterge calculatorul dupe id
    :param id:
    :param lista:
    :return:
    """
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
            calculatorNoua=creeazaCalculator(id,nume,descriere,pret,locatie,lista)
            listaNoua.append(calculatorNoua)
        else:
            listaNoua.append(calculator)
    return listaNoua
