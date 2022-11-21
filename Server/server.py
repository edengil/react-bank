import requests
from db import db_engine as db_engine
from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/transaction")
async def get_all_transactions():
    # can return all the transactions
    return {"transactions":  db_engine.get_all_transactions_from_db()}

@app.get("/transaction/{transactionId}")
async def get_transaction(transactionId):
    #return transaction by id
    return db_engine.get_transaction_by_id(transactionId)


@app.get("/categories")
async def get_all_categories():
    #return all the categories
    return db_engine.get_all_categories_from_db()


@app.get("/categories/breakdown")
async def get_categories_breakdown():
    #return all the categories breakdown
    return db_engine.get_categories_breakdown()


@app.post("/transaction")
async def add_transaction(request: Request):
    # adds a new transaction
    req = await request.json()
    db_engine.add_transactions_to_db(
        req["amount"], req["vendor"], req["categoryId"], req["userId"])
    return {"message": "transaction added successfully"}


@app.delete("/transaction/{transactionId}")
def delete_transaction(transactionId):
    db_engine.remove_transaction(transactionId)
    return {"message": "transaction was removed successfully"}


@app.get("/users/{id}")
def get_user_balance(id):
    user = db_engine.get_user(id)
    return {"user": user}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
