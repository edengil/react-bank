import React, { useEffect, useState } from "react";
import "./Breakdown.css";
import axios from "axios";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

export default function Breakdown() {
  const [breakdown, setBreakdown] = useState([]);

  useEffect(() => {
    async function fetchBreakdown() {
        const res = await axios.get("http://localhost:8000/categories/breakdown");
        const breakdown = res.data;
        setBreakdown(breakdown);
    }
    fetchBreakdown();
  }, []);

  return (
    <Card style={{ width: "13rem", margin: "auto" }}>
      <Card.Header as="h3">Breakdown</Card.Header>
      <ListGroup variant="flush">
        {breakdown.map((b, i) => (
          <ListGroup.Item key={i}>
            <div className="containerBreakdown">
            <span>{b.category}: </span>
            <span className={b.total < 0 ? "red" : "green"}>{b.total}</span>
        </div>
          </ListGroup.Item>
        ))}
      </ListGroup>
    </Card>
  );
}