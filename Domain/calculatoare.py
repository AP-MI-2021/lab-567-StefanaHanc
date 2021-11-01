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
    return {
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie
    }
def getId(calculator):
    """
    da id_ul unui telefon
    :param telefon: dictionar ce contine un telefon
    :return: id_ul telefonului
    """
    return calculator["id"]

def getNume(calculator):
    return calculator["nume"]


def getDescriere(calculator):
    return calculator["descriere"]


def getPret(calculator):
    return calculator["pret"]


def getLocatie(calculator):
    return calculator["locatie"]

def toString(calculator):
    return "Id:{}, Nume: {}, Descriere: {}, Pret: {}, Locatie:{}".format(
    getId(calculator),
    getNume(calculator),
    getDescriere(calculator),
    getPret(calculator),
    getLocatie(calculator)
    )