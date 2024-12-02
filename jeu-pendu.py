import random
import tkinter as tk
import time
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import os

# Liste de mots pour le jeu
mots = ['python', 'pendu', 'informatique', 'jeu', 'ordinateur', 'programmation', 'algorithmique']

# Choisir un mot au hasard
mot_a_deviner = random.choice(mots)

# Créer une liste vide pour garder la trace des lettres devinées
lettres_devinees = ['_'] * len(mot_a_deviner)

# Définir le nombre d'essais
tentatives_max = 3
tentatives_restantes = tentatives_max

# Liste pour garder une trace des lettres déjà proposées
lettres_proposees = []

# Charger l'image du pendu (Vérification de l'existence de l'image)
image_pendu_path = 'pendu_image.png'  # Mettez à jour le chemin si nécessaire

# Vérifiez si l'image existe dans le chemin donné
if os.path.exists(image_pendu_path):
    image_pendu = Image.open(image_pendu_path)
    image_pendu = image_pendu.resize((200, 200), Image.ANTIALIAS)  # Redimensionner l'image
    image_pendu_tk = ImageTk.PhotoImage(image_pendu)
else:
    print(f"Erreur : L'image {image_pendu_path} n'a pas été trouvée.")
    image_pendu_tk = None  # Si l'image n'est pas trouvée, ne pas charger l'image du pendu.

# Fonction pour afficher l'état actuel du jeu dans l'interface
def afficher_jeu():
    mot_affiche = ' '.join(lettres_devinees)
    label_mot.config(text="Mot à deviner : " + mot_affiche)
    label_tentatives.config(text=f"Essais restants : {tentatives_restantes}")
    
    # Mettre à jour l'image du pendu en fonction des tentatives restantes
    if tentatives_restantes == 0 and image_pendu_tk:
        label_pendu.config(image=image_pendu_tk)  # Afficher l'image du pendu quand le joueur perd
    else:
        label_pendu.config(image='')  # Réinitialiser l'image pour les essais
    
    # Mettre à jour la liste des lettres proposées
    lettres_proposees_affiche = ' '.join(lettres_proposees)
    label_lettres_proposees.config(text=f"Lettres déjà proposées : {lettres_proposees_affiche}")

# Fonction pour l'animation de la victoire
def animation_victoire():
    # Création de la fenêtre pop-up de victoire
    popup = Toplevel(root)
    popup.title("Félicitations !")
    popup.geometry("400x200")
    popup.configure(bg="#a5d6a7")
    
    label = Label(popup, text="Félicitations", font=("Arial", 12, "bold"), bg="#a5d6a7", fg="green")
    label.pack(pady=20)

    # Animation du texte
    for i in range(len(label.cget("text"))):
        label.config(text=label.cget("text")[:i+1])
        time.sleep(0.1)  # Pause pour l'animation
        popup.update()  # Met à jour l'interface

    time.sleep(1)  # Attente avant de fermer la fenêtre
    popup.destroy()  # Fermer la fenêtre de victoire
    recommencer()

# Fonction pour l'animation de la défaite
def animation_defaite():
    # Création de la fenêtre pop-up de défaite
    popup = Toplevel(root)
    popup.title("Dommage!")
    popup.geometry("400x300")
    popup.configure(bg="#ffccbc")
    
    label = Label(popup, text="Dommage", font=("Arial", 12, "bold"), bg="#ffccbc", fg="red")
    label.pack(pady=20)

    # Animation du texte
    for i in range(len(label.cget("text"))):
        label.config(text=label.cget("text")[:i+1])
        time.sleep(0.1)  # Pause pour l'animation
        popup.update()  # Met à jour l'interface

    time.sleep(1)  # Attente avant de fermer la fenêtre
    popup.destroy()  # Fermer la fenêtre de défaite
    recommencer()

# Fonction appelée lorsqu'un joueur fait une devinette
def deviner():
    global tentatives_restantes
    
    lettre = entry_lettr.get().lower()
    
    # Vérifier si la lettre est valide
    if len(lettre) != 1 or not lettre.isalpha():
        return  # Ignorer les entrées invalides

    # Vérifier si la lettre a déjà été devinée
    if lettre in lettres_proposees:
        return  # Ignorer si la lettre a déjà été proposée
    
    # Ajouter la lettre à la liste des lettres proposées
    lettres_proposees.append(lettre)
    
    # Vérifier si la lettre est dans le mot
    if lettre in mot_a_deviner:
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                lettres_devinees[i] = lettre
    else:
        tentatives_restantes -= 1
    
    # Mettre à jour l'affichage du jeu
    afficher_jeu()

    # Vérifier si l'utilisateur a gagné
    if '_' not in lettres_devinees:
        animation_victoire()
    elif tentatives_restantes == 0:
        animation_defaite()

# Fonction pour recommencer une nouvelle partie
def recommencer():
    global mot_a_deviner, lettres_devinees, tentatives_restantes, lettres_proposees
    mot_a_deviner = random.choice(mots)
    lettres_devinees = ['_'] * len(mot_a_deviner)
    tentatives_restantes = tentatives_max
    lettres_proposees = []
    afficher_jeu()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Pendu")
root.geometry("600x600")  # Taille de la fenêtre
root.configure(bg='#f0f4c3')  # Couleur de fond claire

# Affichage du mot à deviner et des tentatives restantes
label_mot = tk.Label(root, text="Mot à deviner : " + ' '.join(lettres_devinees), font=("Arial", 24, "bold"), bg='#f0f4c3', fg='#388e3c')
label_mot.pack(pady=20)

label_tentatives = tk.Label(root, text=f"Essais restants : {tentatives_restantes}", font=("Arial", 18), bg='#f0f4c3', fg='#d32f2f')
label_tentatives.pack(pady=10)

# Zone pour afficher l'image du pendu
label_pendu = tk.Label(root, relief="sunken", width=20, height=10, bg='#f0f4c3')
label_pendu.pack(pady=20)

# Champ pour entrer la lettre
entry_lettr = tk.Entry(root, font=("Arial", 18), width=3, justify="center", bg='#e8f5e9')
entry_lettr.pack(pady=10)

# Bouton pour faire une devinette
button_deviner = tk.Button(root, text="Deviner", font=("Arial", 18, "bold"), command=deviner, bg='#4CAF50', fg='white')
button_deviner.pack(pady=20)

# Affichage des lettres déjà proposées
label_lettres_proposees = tk.Label(root, text="Lettres déjà proposées : ", font=("Arial", 16), bg='#f0f4c3', fg='#0277bd')
label_lettres_proposees.pack(pady=10)

# Bouton pour recommencer
button_recommencer = tk.Button(root, text="Recommencer", font=("Arial", 18, "bold"), command=recommencer, bg='#FF9800', fg='white')
button_recommencer.pack(pady=20)

# Lancer l'affichage initial
afficher_jeu()

root.mainloop()
