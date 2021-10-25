def creeazaCalculator(id,nume,descriere,pret,locatie):
    """
    Creeaza un ditionar ce repretinta un telefon
    :param id:string
    :param nume:string
    :param descriere:string
    :param pret: float
    :param locatie: string
    :return:  un ditionar ce descriere un telefon
    """
    return [id,nume,descriere,pret,locatie]
def getId(calculator):
    """
    da id_ul unui telefon
    :param telefon: dictionar ce contine un telefon
    :return: id_ul telefonului
    """
    return calculator[0]

def getNume(calculator):
    return calculator[1]


def getDescriere(calculator):
    return calculator[2]


def getPret(calculator):
    return calculator[3]


def getLocatie(calculator):
    return calculator[4]

def toString(calculator):
    return "Id:{}, Nume: {}, Descriere: {}, Pret: {}, Locatie:{}".format(
    getId(calculator),
    getNume(calculator),
    getDescriere(calculator),
    getPret(calculator),
    getLocatie(calculator)
    )