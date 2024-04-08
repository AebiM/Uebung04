import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QLineEdit, QPushButton, QAction, QComboBox, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Daten Speichern')
        self.setGeometry(100, 100, 400, 200)

       
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)

        
        labels = ['Vorname:', 'Nachname:', 'Geburtsdatum:', 'Adresse:', 'PLZ:', 'Ort:', 'Land:']
        self.lineEdits = {}
        for i, label in enumerate(labels):
            layout.addWidget(QLabel(label), i, 0)
            if label == 'Land:':
                self.comboBox = QComboBox()
                self.comboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
                layout.addWidget(self.comboBox, i, 1)
            else:
                lineEdit = QLineEdit()
                self.lineEdits[label[:-1]] = lineEdit  
                layout.addWidget(lineEdit, i, 1)

        
        self.saveButton = QPushButton('Save')
        self.saveButton.clicked.connect(self.saveData)
        layout.addWidget(self.saveButton, len(labels), 1)

        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveData)
        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.close)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(quitAction)

    def saveData(self):
        data = []
        for key, lineEdit in self.lineEdits.items():
            data.append(lineEdit.text())
        data.append(self.comboBox.currentText())  
        with open('output.txt', 'w') as file:
            file.write(','.join(data))
        QMessageBox.information(self, "Speichern", "Daten wurden erfolgreich gespeichert!", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
