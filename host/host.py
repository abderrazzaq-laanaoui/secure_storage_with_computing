import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
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

    def read(self, table, columns="*", condition=None) -> List[Dict]:
        cursor = self.connection.cursor()
        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        # Convertir les données en une liste de dictionnaires

        if columns == "*":
            # Si toutes les colonnes sont sélectionnées, obtenir les noms de colonnes à partir du curseur
            columns = [col[0] for col in cursor.description]
        for row in data:
            row_data = {}
            for i, value in enumerate(row):
                # Convertir les valeurs bytearray en chaînes de caractères
                if isinstance(value, bytearray):
                    row_data[columns[i]] = value.decode('utf-8')
                else:
                    row_data[columns[i]] = value
            return row_data
        
        return None


app = FastAPI()
db_host = DatabaseHost(host="localhost", user="root", password="Ensibs@log2024", database="secret_db")
db_host.connect()

class Item(BaseModel):
    arithmetic_value: str
    binary_value: str

@app.get("/{id}")
def read_root(id: int):
    condition = f"id = {id}"  # Condition to select the record with the specified id
    data = db_host.read(table="secret_data", condition=condition)
    if not data:
        raise HTTPException(status_code=404, detail="Record not found")
    return data

@app.post("/")
def create_item(item: Item):
    db_host.write(table="secret_data", data=item.dict())
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

