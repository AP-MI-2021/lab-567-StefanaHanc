from Domain.calculatoare import getLocatie, getPret, creeazaCalculator, getId, getNume, getDescriere


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


def ordonareDupaPret(lista):
    """
     Ordonarea obiectelor crescător după prețul de achiziție.
    :param lista: Lista are trebuie sortata
    :return : Lista sortata
    """
    return sorted(lista,key=lambda calculator:getPret(calculator))



def modificaLocatia(adresaCautata,adresanoua,lista):
    """
     Mutarea tuturor obiectelor dintr-o locație în alta.
    :param adresaCautata: string
    :param adresanoua:string
    :param lista:adresa verificata
    :return:noua lista cu locatia modificata
    """
    listaNoua=[]
    for calculator in lista:
        id =getId(calculator)
        nume =getNume(calculator)
        descriere =getDescriere(calculator)
        pret = getPret(calculator)
        locatia = getLocatie(calculator)
        if locatia == adresaCautata:
          calculatorNoua = creeazaCalculator(id, nume, descriere, pret, adresanoua)
          listaNoua.append(calculatorNoua)
        else:
            listaNoua.append(calculator)
    return listaNoua