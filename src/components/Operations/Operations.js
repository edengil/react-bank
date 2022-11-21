import React from "react";
// import "./Operations.css";
import InitTransaction from "./InitTransaction"

export default function Operations(props) {
  return (
    <div>
      <InitTransaction
        updateBalance={props.updateBalance}
      ></InitTransaction>
    </div>
  );
}