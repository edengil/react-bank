from fastapi import FastAPI, Request, Response
import uvicorn
import requests
from db.db_accessor import transactions_accessor

from db import db_engine
app = FastAPI()


@app.get("/transactions")
async def get_all_transactions(pokemon_name="", trainer_id="", trainer_name=""):
    # can return all the pokemons from some type
    return db_engine.get_all_transactions_from_db()


@app.post("/transaction")
async def add_transaction(request: Request):
    # adds a new transaction
    req = await request.json()
    db_engine.add_transactions_to_db(
        req["amount"], req["vendor"], req["categoryId"], req["userId"])
    return {"message": "transaction added successfully"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
