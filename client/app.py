import os
import requests

# Define the base URL of the middleware
base_url = "http://localhost:8085"

# Function to add a value
def add_value():
    print("Vous avez choisi d'ajouter une valeur dans la base de données")
    value = int(input("Choisissez une valeur a ajouter:"))
    # Send a POST request to the middleware to add the value
    response = requests.post(f"{base_url}/add_value/{value}")
    print("Valeur ajoutée, l'id est ", response.json())

# Function to compare two values
def compare_values():
    print("Vous avez choisi de comparer deux valeur dans la base de données")
    id_1 = int(input("Choisissez l'id 1:"))
    id_2 = int(input("Choisissez l'id 2:"))
    # Send a GET request to the middleware to compare the values
    response = requests.get(f"{base_url}/compare_values/{id_1}/{id_2}")
    print("Le résultat de la comparaison est ", response.json())

# Function to sum two values
def sum_values():
    print("Vous avez choisi d'additionner deux valeur")
    id_1 = int(input("Choisissez l'id 1:"))
    id_2 = int(input("Choisissez l'id 2:"))
    # Send a GET request to the middleware to sum the values
    response = requests.get(f"{base_url}/sum_values/{id_1}/{id_2}")
    print("La somme des valeurs est ", response.json())

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console() 
# Main loop for the menu
while True:
    print("Votre choix")
    print("   1. Ajouter une valeur")
    print("   2. Comparer deux valeurs")
    print("   3. Additionner deux valeurs")
    print("   4. Quitter")

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