import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom'
import logo from './logo.svg';
import './App.css';
import Login from './auth/Login'
import Assembly from './assembly/Assembly'
import Walkthrough from './walkthrough/Walkthrough'
import Dashboard from './dashboard/Dashboard'

function App() {
  return (
    <>
      <Router>
        <Switch>
          <Route path='/app/login'>
            <Login />
          </Route>
          <Route path='/app/dashboard'>
            <Dashboard />
          </Route>
          <Route path='/app/walkthrough'>
            <Walkthrough />
          </Route>
          <Route path='/app/assembly'>
            <Assembly />
          </Route>
        </Switch>
      </Router>
    </>
  );
}

export default App;
