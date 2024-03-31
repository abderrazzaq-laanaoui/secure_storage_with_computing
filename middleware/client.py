from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from phe import paillier
from pyope.ope import OPE
import host

app = FastAPI()

# Generate keys for Paillier encryption
public_key, private_key = paillier.generate_paillier_keypair()

# Generate a key for OPE

ope_key = OPE(OPE.generate_key())

class Item(BaseModel):
    id1: int
    id2: int

@app.post("/add_value/{value}")
def add_value(value: int):
    # Encrypt the value
    arithmetic_value = public_key.encrypt(value)
    binary_value = ope_key.encrypt(value)

    # Send the hashes to the host
    hashes = host.Hashes(arithmetic_value=str(arithmetic_value), binary_value=str(binary_value))
    return host.add_hashes(hashes)

@app.post("/compare_by_id")
def compare_by_id(item: Item):
    # Send the ids to the host for comparison
    return host.compare(item)

@app.post("/sum_by_id")
def sum_by_id(item: Item):
    # Send the ids to the host for sum
    return host.sum(item)