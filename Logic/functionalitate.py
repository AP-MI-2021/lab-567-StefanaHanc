from Domain.calculatoare import getLocatie, getPret, creeazaCalculator, getId, getNume, getDescriere


def maxPretPerLocatie(lista):
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
    return sorted(lista,key=lambda calculator:getPret(calculator))


def getlocatie(calculator):
    pass


def modificaLocatia(adresaCautata,adresanoua,lista):
    listaNoua=[]
    for calculator in lista:
        id =getId(calculator)
        nume =getNume(calculator)
        descriere =getDescriere(calculator)
        pret = getPret(calculator)
        locatia = getLocatie(calculator)
        if locatia is adresaCautata:
          calculatorNoua = creeazaCalculator(id, nume, descriere, pret, adresanoua)
          listaNoua.append(calculatorNoua)
        else:
            listaNoua.append(calculator)
    return listaNoua