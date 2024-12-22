import sys
import os
from PyQt5 import QtWidgets, QtCore, uic
import pygame

def shutdown():
    # Commande pour éteindre l'ordinateur sous Windows
    os.system("shutdown /s /t 1")
    # Commande pour éteindre l'ordinateur sous macOS/Linux
    # os.system("sudo shutdown now")

def enable_label_8(window):
    window.label_8.setEnabled(True)

def stop_explorer():
    # Commande pour arrêter explorer.exe sous Windows
    if sys.platform == 'win32':
        os.system("taskkill /f /im explorer.exe")

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # Lecture en boucle

def main():
    # Arrêter explorer.exe
    stop_explorer()
    
    # Jouer la musique
    play_music()
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Charger le fichier .ui
    window = uic.loadUi("window.ui")
    
    # Modifier les windowFlags pour désactiver les boutons de fermeture et d'agrandissement
    window.setWindowFlags(
        window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint
    )

    # Interdire le redimensionnement de la fenêtre
    window.setFixedSize(window.size())
    
    # Connecter le bouton pushButton à la fonction shutdown
    window.pushButton.clicked.connect(shutdown)
    
    # Connecter le bouton pushButton_2 à la fonction enable_label_8
    window.pushButton_2.clicked.connect(lambda: enable_label_8(window))
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()