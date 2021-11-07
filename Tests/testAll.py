from Tests.testCRUD import testAdaugaCalculator, testStergereCalculator, testUndo
from Tests.testDomain import testCalculator
from Tests.testFuntionalitati import testMaxPretPerLocatie, testOrdonareDupaPret, testModificareLocatie, \
    testAfisareaSumelorPerLocatie, testConcantenareString


def runAllTests():
    testCalculator()
    testAdaugaCalculator()
    testStergereCalculator()
    testMaxPretPerLocatie()
    testOrdonareDupaPret()
    testModificareLocatie()
    testAfisareaSumelorPerLocatie()
    testConcantenareString()