import sys
from Biblioteki import ButtonMenu
from PyQt5.QtWidgets import QApplication
from Core import KmeansCore

app = QApplication(sys.argv)

okno = ButtonMenu(name="Kmeans by s21001")
rdzen = KmeansCore(okno)
okno.addbutton("Grupuj", rdzen.group)
okno.addbutton("Utwórz zbiór danych", rdzen.create_2d_data)

app.exec_()


