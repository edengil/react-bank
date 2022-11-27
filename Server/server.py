import requests
from db import db_engine as db_engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse

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
    transactions = db_engine.get_all_transactions_from_db()
    if(len(transactions) == 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Can't get transactions")
    return {"transactions":  transactions}

@app.get("/transaction/{transactionId}")
async def get_transaction(transactionId):
    #return transaction by id
    transaction = db_engine.get_transaction_by_id(transactionId)
    if(len(transaction) == 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="transaction id not found ")
    return transaction


@app.get("/categories")
async def get_all_categories():
    #return all the categories
    categories = db_engine.get_all_categories_from_db()
    if(len(categories) == 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Can't get breakdown")
    return categories

@app.get("/categories/breakdown")
async def get_categories_breakdown():
    #return all the categories breakdown
    breakdown = db_engine.get_categories_breakdown()
    if (len(breakdown) == 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Can't get breakdown")
    return breakdown


@app.post("/transaction")
async def add_transaction(request: Request):
    # adds a new transaction
    req = await request.json()
    db_engine.add_transactions_to_db(
        req["amount"], req["vendor"], req["categoryId"], req["userId"])
    return {"message": "transaction added successfully"}


@app.delete("/transaction/{transactionId}")
def delete_transaction(transactionId):
    try:
        db_engine.remove_transaction(transactionId)
        return {"message": "Transaction was removed successfully"}
    except Exception as e:
        print(e)
        return JSONResponse({"Error": "transaction id not found"},status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/users/{id}")
def get_user_by_id(id):

        user = db_engine.get_user(id)
        if(len(user) == 0):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user id not found")
        return {"user": user}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
