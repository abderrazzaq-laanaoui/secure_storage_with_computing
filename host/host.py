import mysql.connector
class DatabaseHost:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connexion à la base de données réussie.")
        except mysql.connector.Error as err:
            print("Erreur de connexion à la base de données:", err)
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Déconnexion de la base de données.")
    def read(self, table, columns="*", condition=None):
        cursor = self.connection.cursor()
        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
    def write(self, table, data):
        cursor = self.connection.cursor()
        query = f"INSERT INTO {table} VALUES ({', '.join(['%s'] * len(data))})"
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()

# Exemple d'utilisation
if __name__ == "__main__":
    db_host = DatabaseHost(host="localhost", user="root", password="Ensibs@log2024", database="secret_db")
    db_host.connect()
    # Lecture des données depuis la table 'secret_data'
    data = db_host.read(table="secret_data")
    print("Données récupérées depuis la base de données:", data)
    # Exemple d'écriture de données dans la table 'secret_data'
    new_data = (1, b"arithmetic_value", b"binary_value")
    db_host.write(table="secret_data", data=new_data)

    db_host.disconnect()

