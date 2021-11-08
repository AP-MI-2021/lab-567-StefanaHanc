from Logic.CRUD import adaugaCalculator
from Tests.testAll import runAllTests
from UI.command_line_console import meniu
from UI.console import runMenu


def main():
   runAllTests()
   lista=[]
   runMenu(lista)
main()