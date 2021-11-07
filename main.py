from Logic.CRUD import adaugaCalculator
from Tests.testAll import runAllTests
from UI.command_line_console import meniu
from UI.console import runMenu


def main():
   runAllTests()
   lista=[]
   lista = adaugaCalculator("1", "Lenovo", "Windows 10", 2400.23, "Cluj", lista)
   lista = adaugaCalculator("2", "Lenovo", "Windows 11", 4400, "Cluj", lista)
   lista = adaugaCalculator("3", "Lenovo", "Windows 10", 2400, "Sv", lista)
   runMenu(lista)
main()