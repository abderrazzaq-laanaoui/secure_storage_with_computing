"""import mysql.connector

# Se connecter à la base de données
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ensibs@log2024",
    database="secret_db"
)"""

# Définir une fonction pour déchiffrer les données sensibles
def decrypt_data(encrypted_data):
    # Utiliser le middleware pour déchiffrer les données
    decrypted_data = middleware.decrypt(encrypted_data)
    return decrypted_data

# Fonction pour ajouter une valeur
def add_value():
	value = int(input("Choisissez une valeur a ajouter:"))
	# Fonction add
	print("Valeur ajoutée, l'id est ")

def show_id():
	print("Voici la liste des IDs:")
	last_id = 4
	#GetID
	id_list = []  
	for i in range(1, last_id + 1):
		id_list.append(str(i))  
	print("[" + ", ".join(id_list) + "]")


# Fonction pour comparer deux valeurs
def compare_values():
	show_id()
	id_1 = int(input("Choisissez l'id 1:"))
	id_2 = int(input("Choisissez l'id 2:"))

# Fonction pour additionner deux valeurs
def sum_values():
	show_id()
	id_1 = int(input("Choisissez l'id 1:"))
	id_2 = int(input("Choisissez l'id 2:"))
	

# Boucle principale pour le menu
while True:
    print("Votre choix:")
    print("1. Ajouter une valeur")
    print("2. Comparer deux valeurs")
    print("3. Additionner deux valeurs")
    print("4. Quitter")

    choice = int(input("Choisissez une option: "))

    if choice == 1:
        add_value()
    elif choice == 2:
        compare_values()
    elif choice == 3:
        sum_values()
    elif choice == 4:
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")

