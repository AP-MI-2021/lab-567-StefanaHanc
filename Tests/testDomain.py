from Domain.calculatoare import creeazaCalculator, getId, getNume, getDescriere, getPret, getLocatie


def testCalculator():
    calculator=creeazaCalculator("1","Lenovo","Windows 10",2400.23,"Cluj")
    assert getId(calculator)=="1"
    assert getNume(calculator) == "Lenovo"
    assert getDescriere(calculator)=="Windows 10"
    assert getPret(calculator) == 2400.23
    assert getLocatie(calculator) == "Cluj"