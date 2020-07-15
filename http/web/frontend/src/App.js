import React, {useState} from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from 'react-router-dom'
import logo from './logo.svg';
import './App.css';
import Login from './auth/Login'
import Assembly from './assembly/Assembly'
import Walkthrough from './walkthrough/Walkthrough'
import Dashboard from './dashboard/Dashboard'


function App() {
  const [user, setUser] = useState(null)

  return (
    <>
      
      <Router> 
        <Switch>
          <Route path='/app/dashboard'>
          {!user && <Redirect to='/app/login' />}
            <Dashboard />
          </Route>
          <Route path='/app/walkthrough'>
          {!user && <Redirect to='/app/login' />}
            <Walkthrough />
          </Route>
          <Route path='/app/assembly'>
          {!user && <Redirect to='/app/login' />}
            <Assembly />
          </Route>
          <Route>
            <Redirect to='/app/dashboard' />
          </Route>
        </Switch>
      </Router>
    </>
  );
}

export default App;
