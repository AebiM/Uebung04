import  urllib.parse
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()
        self.setMinimumSize(500,200)

        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.geburtstagLineEdit.setDisplayFormat("dd/MM/yyyy")
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button2 = QPushButton('Auf Karte anzeigen')
        self.button3 = QPushButton('Laden')        
        self.button1 = QPushButton("Speichern")
        

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:" , self.countries)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        
        self.button1.clicked.connect(self.speichern)
        self.button2.clicked.connect(self.karte)
        self.button3.clicked.connect(self.laden)


    def speichern(self):
        filename, typ = QFileDialog.getSaveFileName(self, 'Datei speichern', '' , 'TXT (*.txt)' ) 

        file = open(filename, "w")
        daten = [self.vornameLineEdit.text(), 
                 self.nameLineEdit.text(), 
                 self.geburtstagLineEdit.text(), 
                 self.adresseLineEdit.text(), 
                 self.plzLineEdit.text(), 
                 self.ortLineEdit.text(), 
                 self.countries.currentText()
                 ]
        daten_2= ",".join(str(i) for i in daten)
        file.write (daten_2)
        file.close()


    def karte(self):
        adresse = f'{self.adresseLineEdit.text()}+{self.plzLineEdit.text()}+{self.ortLineEdit.text()}+{self.countries.currentText()}'
        query = urllib.parse.quote(adresse)
        link = f"https://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))


    def laden(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Files (*.txt)")
        if filepath:
                with open(filepath, "r") as f:
                    data = f.read().split(',')
                    
                    if len(data) == 7:  # Stellen Sie sicher, dass die Datenstruktur wie erwartet ist
                        self.vornameLineEdit.setText(data[0])
                        self.nameLineEdit.setText(data[1])
                        self.geburtstagLineEdit.setDate(QDate.fromString(data[2], "dd/MM/yyyy"))
                        self.adresseLineEdit.setText(data[3])
                        self.plzLineEdit.setText(data[4])
                        self.ortLineEdit.setText(data[5])
                        
                        # Auswahl des Landes im QComboBox
                        index = self.countries.findText(data[6], Qt.MatchFixedString)
                        if index >= 0:
                            self.countries.setCurrentIndex(index)
          






def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()