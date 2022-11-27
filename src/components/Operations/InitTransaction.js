import React, { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import TransactionObj from "../../objects/TransactionObj";
import axios from "axios";

export default function InsertTransaction(props) {
    const [categories, setCategories] = useState([]);
    const [validated, setValidated] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [transactionInput, setTransactionInput] = useState({
      amount: "",vendor: "",categoryId: "",
    });
    const userId = 1
    useEffect(() => {
      async function fetchCategories() {
        const res = await axios.get("http://localhost:8000/categories");
        const categories = res.data;
        setCategories(categories);
      }
      fetchCategories();
    }, []);
  

    function handleInput(e) {
      setTransactionInput({...transactionInput,[e.target.name]: e.target.value,
      });
    }
  
  //fix submit to submit form 
    async function submit(e) {
      const form = e.currentTarget;
      e.preventDefault();
      e.stopPropagation();
      if (form.checkValidity() === true) {
        setIsModalOpen(true);
        let sign = e.nativeEvent.submitter.name === "Deposit" ? 1 : -1;
        await axios.post("http://localhost:8000/transaction",(
          new TransactionObj(
            null,
            sign * + transactionInput.amount,
            transactionInput.vendor,
            transactionInput.categoryId,
            userId 
          )
        ));
        props.updateBalance();
        setTransactionInput({
          amount: "",
          vendor: "",
          categoryId: "",
        });
        setValidated(false);
      } else {
        setValidated(true);
      }
    }
  
    return (
      <div>
        <Card style={{ width: "25rem", margin: "auto" }}>
          <Card.Header as="h3">Insert Transaction</Card.Header>
          <Card.Body>
            <Form
              noValidate
              validated={validated}
              onSubmit={submit}
              autoComplete="off"
            >
              <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Transaction Amount</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Transaction amount"
                  name="amount"
                  value={transactionInput.amount}
                  onChange={handleInput}
                  required
                />
              </Form.Group>
  
              <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Transaction Vendor</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Transaction vendor"
                  value={transactionInput.vendor}
                  onChange={handleInput}
                  name="vendor"
                  required
                />
              </Form.Group>
  
              <Form.Group className="mb-3">
                <Form.Label>Transaction Category</Form.Label>
                <Form.Select
                  value={transactionInput.categoryId}
                  onChange={handleInput}
                  name="categoryId"
                  required
                >
                  <option value="" hidden>
                    Select category
                  </option>
                  {categories.sort().map((c, i) => (
                    <option key={i} value={c.id}>
                      {c.name}
                    </option>
                  ))}
                </Form.Select>
              </Form.Group>
  
              <Button 
                variant="success" 
                name="Deposit" 
                type="submit"
                >
                Deposit
              </Button>
              <Button
                name="Withdraw"
                variant="danger"
                style={{ float: "right" }}
                type="submit"
              >
                Withdraw
              </Button>
            </Form>
          </Card.Body>
        </Card>
      </div>
    );
  }