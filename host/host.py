import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

app = FastAPI()
db_host = DatabaseHost(host="localhost", user="root", password="Ensibs@log2024", database="secret_db")
db_host.connect()

class Item(BaseModel):
    arithmetic_value: str
    binary_value: str

@app.get("/")
def read_root():
    data = db_host.read(table="secret_data")
    return data

@app.post("/")
def create_item(item: Item):
    db_host.write(table="secret_data", data=item.dict())
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

