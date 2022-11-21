import React, { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import TransactionObj from "../../objects/TransactionObj";
import axios from "axios";
import ListGroup from "react-bootstrap/ListGroup";
import Transaction from "./Transaction"

export default function Transactions(props) {
  const [transactions, setTransactions] = useState([]);

  async function fetchTransactions() {
    const res = await axios.get("http://localhost:8000/transaction");
    const transactionsData = res.data.transactions;
    const transactionsObj = transactionsData.map(
      t =>
        new TransactionObj(
          t.id,
          t.amount,
          t.vendor,
          t.categoryId,
          t.userId
        )
    );
    setTransactions(transactionsObj);
  }
  useEffect(() => {
    fetchTransactions();
  }, []);

  async function deleteTransaction(transactionId) {
    alert("Transaction deleted successfully!");
    await axios.delete( `http://localhost:8000/transaction/${transactionId}`);
    await fetchTransactions();
    props.updateBalance();
  }
  return (
    <Card style={{ width: "35rem" }}>
      <Card.Header as="h3">Transactions</Card.Header>
      <ListGroup as="ol">
        {transactions.map((t, i) => (
          <Transaction
            key={i}
            transaction={t}
            delete={deleteTransaction}
          ></Transaction>
        ))}
      </ListGroup>
    </Card>
  );
}


// import React, { Component } from 'react'

// export default class Transactions extends Component {
//   render() {
//     return (
//       <div>Transactions</div>
//     )
//   }
// }
