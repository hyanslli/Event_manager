import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLineEdit, QLabel, QGridLayout
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QPropertyAnimation, QRect

class MainWindow(QWidget):
    ASSETS_FOLDER = Path(__file__).parent

    def assets(self, filename: str) -> str:
        return os.path.join(self.ASSETS_FOLDER, 'assets', filename)
    
    def __init__(self):
        super().__init__()
        self.layout_grid = QGridLayout()
        self.layout_grid.setContentsMargins(0, 0, 15, 0)  # Remove todas as margens (superior, esquerda, inferior, direita)

        self.setWindowTitle("Event Manager")  # Titulo da janela
        self.resize(1200, 700)  # Tamanho da janela
        self.setWindowIcon(QIcon(self.assets('icon.png')))  # Ícone da janela
        self.setStyleSheet("background-color: #4B74BB;")  # Cor de fundo da janela
        
        # grid 1
        img_label = QLabel(self)
        img = QPixmap(self.assets('base.png'))
        img_label.setPixmap(img.scaled(700, 700))
        self.layout_grid.addWidget(img_label, 0, 0, 1, 2)  # Adiciona a imagem na posição (0, 0) e ocupa 1 linha e 2 colunas

        # Adicionando uma linha horizontal
        line1 = QFrame(self)
        line1.setFrameShape(QFrame.Shape.HLine)
        line1.setFrameShadow(QFrame.Shadow.Sunken)
        line1.setStyleSheet("background-color: #ffffff;")  # Define a cor da linha como branca
        line1.move(767, 165)
        line1.resize(170, 1)

        line2 = QFrame(self)
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setFrameShadow(QFrame.Shadow.Sunken)
        line2.setStyleSheet("background-color: #ffffff;")  # Define a cor da linha como branca
        line2.move(1000, 165)
        line2.resize(170, 1)

        icon_label = QLabel(self)
        icon = QPixmap(self.assets('generic.png'))
        icon_label.setPixmap(icon.scaled(51, 51))
        icon_label.move(941, 132)
        icon_label.resize(52, 52)

        button3 = QPushButton("Entrar", self)
        button3.setStyleSheet("""
            background-color: #627AE6;
            font-size: 16px;
            border-radius: 15px;
        """)
        button3.move(810, 530)
        button3.resize(300, 42)

        button4 = QPushButton("Cadastrar-se", self)
        button4.setStyleSheet("font-size: 14px; border: none;")
        button4.move(870, 595)
        button4.resize(170, 42)  # Largura, Altura
        button4.clicked.connect(self.cadastrar)

        line3 = QFrame(self)
        line3.setFrameShape(QFrame.Shape.HLine)
        line3.setFrameShadow(QFrame.Shadow.Sunken)
        line3.setStyleSheet("background-color: #ffffff;")
        line3.move(767, 650)
        line3.resize(400, 1)

        # Adicionando o campo de entrada com animação
        self.entry_label = QLabel("Login", self) # Rótulo do campo de entrada
        self.entry_label.setStyleSheet("font-size: 16px; color: #ffffff;")
        self.entry_label.setGeometry(760, 250, 400, 40)  # Posição inicial do label (x, y, largura, altura)

        self.entry = QLineEdit(self)
        self.entry.setStyleSheet("""
            font-size: 16px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 10px;
        """)
        self.entry.setGeometry(760, 250, 400, 40)  # Posição do campo de entrada
        self.entry.textChanged.connect(lambda: self.animate_label(self.entry, self.entry_label, 250))

        self.entry_label2 = QLabel("Senha", self) # Rótulo do campo de entrada
        self.entry_label2.setStyleSheet("font-size: 16px; color: #ffffff;")
        self.entry_label2.setGeometry(760, 330, 400, 40)  # Posição inicial do label (x, y, largura, altura)

        self.entry2 = QLineEdit(self)
        self.entry2.setStyleSheet("""
            font-size: 16px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 10px;
        """)
        self.entry2.setGeometry(760, 330, 400, 40)  # Posição do campo de entrada
        self.entry2.textChanged.connect(lambda: self.animate_label(self.entry2, self.entry_label2, 330))

    def animate_label(self, entry, label, y):
        if entry.text():
            self.animation = QPropertyAnimation(label, b"geometry")
            self.animation.setDuration(200)
            self.animation.setStartValue(QRect(760, y, 400, 40))
            self.animation.setEndValue(QRect(760, y - 30, 400, 40))
            self.animation.start()
        else:
            self.animation = QPropertyAnimation(label, b"geometry")
            self.animation.setDuration(200)
            self.animation.setStartValue(QRect(760, y - 30, 400, 40))
            self.animation.setEndValue(QRect(760, y, 400, 40))
            self.animation.start()
        
    def cadastrar(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())