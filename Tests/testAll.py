from Tests.testCRUD import testAdaugaCalculator, testStergereCalculator
from Tests.testDomain import testCalculator
from Tests.testFuntionalitati import testMaxPretPerLocatie, testOrdonareDupaPret, testModificareLocatie


def runAllTests():
    testCalculator()
    testAdaugaCalculator()
    testStergereCalculator()
    testMaxPretPerLocatie()
    testOrdonareDupaPret()
    testModificareLocatie()