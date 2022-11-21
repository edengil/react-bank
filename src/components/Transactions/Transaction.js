import React from "react";
import "./Transaction.css";
import ListGroup from "react-bootstrap/ListGroup";
import Badge from "react-bootstrap/Badge";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import Button from "react-bootstrap/Button";
import "./Transaction.css";

export default function Transaction(props) {

  return (
    <ListGroup.Item
      as="li"
      className="d-flex justify-content-between align-items-start"
    >
      <div className="container">
        <strong className="ms-2 center-vertically">{props.transaction.vendor}</strong>
        <div className="ms-2 center-vertically">
        </div>
        <Badge
          bg={props.transaction.amount > 0 ? "success" : "danger"}
          pill
          className="center-vertically amount"
        >
          {props.transaction.amount}
        </Badge>
        <Button
          onClick={() => {
            props.delete(props.transaction.id);
          }}
          variant="outline-dark"
          className="delete-btn"
        >
          <FontAwesomeIcon icon={faTrash} />
        </Button>
      </div>
    </ListGroup.Item>
  );
}
