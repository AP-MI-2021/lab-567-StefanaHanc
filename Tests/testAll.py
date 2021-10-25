from Tests.testCRUD import testAdaugaCalculator, testStergereCalculator
from Tests.testDomain import testCalculator


def runAllTests():
    testCalculator()
    testAdaugaCalculator()
    testStergereCalculator()