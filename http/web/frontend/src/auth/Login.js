import React from 'react'
import {useHistory, useLocation} from 'react-router-dom'

const Login = () => {
  let history = useHistory()
  let location = useLocation()

  const attemptLogin = () => {

  }
  
  const handleSubmit = (e) => {
    e.preventDefault()
    history.replace('/app/dashboard/')
  }


  return (
    <>
      <form onSubmit={handleSubmit}>
        <button>Login</button>
      </form>
    </>
  )
}
export default Login