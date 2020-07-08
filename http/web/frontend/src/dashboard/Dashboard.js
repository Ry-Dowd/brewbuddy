import React from 'react'
import {Link} from 'react-router-dom'

const Dashboard = () => {

  return (
    <>
      <h1>Dashboard</h1>
      <ul>
        <li>
          <h3>My Recipes</h3>
          <ul>
            Beers go here
            <li>
              <Link to='/app/walkthrough'>Brew This!</Link>
            </li>
            <li>
              <Link to='/app/assembly'>Create a new recipe</Link>
            </li>
          </ul>
        </li>
      </ul>
    </>
  )
}

export default Dashboard