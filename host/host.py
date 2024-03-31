import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

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
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(data.values()))
        self.connection.commit()
        cursor.close()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Connexion à la base de données
        db_host = DatabaseHost(host="localhost", user="root", password="Ensibs@log2024", database="secret_db")
        db_host.connect()

        # Récupération des données depuis la table 'secret_data'
        data = db_host.read_data(table="secret_data")
        data_json = json.dumps(data)

        # Envoi de la réponse
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data_json.encode())

        # Déconnexion de la base de données
        db_host.disconnect()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        db_host = DatabaseHost(host="localhost", user="root", password="Ensibs@log2024", database="secret_db")
        db_host.connect()

        db_host.write(table="secret_data", data=data)

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

        db_host.disconnect()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Serveur démarré sur le port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

