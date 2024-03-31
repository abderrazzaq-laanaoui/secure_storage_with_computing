import requests
from pydantic import BaseModel

class Hashes(BaseModel):
    arithmetic_value: str
    binary_value: str

class Item(BaseModel):
    id1: int
    id2: int

def add_hashes(hashes: Hashes):
    # Send the hashes to the database host
    response = requests.post('http://localhost:8080', json=hashes.dict())
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to add hashes")

def compare(item: Item):
    # Get the binary hashes for the ids from the database host
    response1 = requests.get(f'http://localhost:8080/{item.id1}')
    response2 = requests.get(f'http://localhost:8080/{item.id2}')
    if response1.status_code == 200 and response2.status_code == 200:
        hash1 = response1.json()
        hash2 = response2.json()

        # Compare the binary hashes
        if hash1['binary_value'] > hash2['binary_value']:
            return 1
        elif hash1['binary_value'] < hash2['binary_value']:
            return -1
        else:
            return 0
    else:
        raise Exception("Invalid id(s)")

def sum(item: Item):
    # Get the arithmetic hashes for the ids from the database host
    response1 = requests.get(f'http://localhost:8080/get/{item.id1}')
    response2 = requests.get(f'http://localhost:8080/get/{item.id2}')
    if response1.status_code == 200 and response2.status_code == 200:
        hash1 = response1.json()
        hash2 = response2.json()

        # Sum the arithmetic hashes
        sum_hash = int(hash1['arithmetic_value']) + int(hash2['arithmetic_value'])
        return str(sum_hash)
    else:
        raise Exception("Invalid id(s)")