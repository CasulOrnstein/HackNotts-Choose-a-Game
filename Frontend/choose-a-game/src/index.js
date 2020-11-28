import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Home from './home-page/Home';
import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import FriendsPage from './friends-page/FriendsPage';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
         <Route path="/friends">
          <FriendsPage/>
        </Route> 
        <Route path="">
          <Home/>
        </Route>
      
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
