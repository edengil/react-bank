import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
} from "react-router-dom";
import NavBar from "./components/NavBar/NavBar";
import Transactions from "./components/Transactions/Transactions";
import Operations from "./components/Operations/Operations";
import Breakdown from "./components/Breakdown/Breakdown";
import { useEffect, useState } from "react";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import GET_USER_BY_ID from "./utils/ConstantUrls" 


function App() {
  const [balance, setBalance] = useState(0);
  const [userId, setUserId] = useState(0);
  
  async function fetchBalance() {
    const res = await axios.get(
      `http://localhost:8000/users/1`
      );
      const balance = res.data.user[0].balance;
      const userId = res.data.user[0].id;
      setUserId(userId)
      setBalance(balance);
    }
    useEffect(() => {
      fetchBalance();
    }, []);
    
    
    return (
      <Router>
      <div className="app">
        <NavBar balance={balance}></NavBar>
        <div className="routes">
          <Switch>
            <Route
              path="/transactions"
              render={() => <Transactions userId={userId} updateBalance={fetchBalance} />}
            ></Route>
            <Route
              exact
              path="/operations"
              render={() => <Operations updateBalance={fetchBalance} />}
            ></Route>
            <Route exact 
              path="/breakdown" 
              render={() => <Breakdown />}
              >
            </Route>
            <Redirect to="/transactions" />
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;