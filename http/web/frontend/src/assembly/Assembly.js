import React,{useState} from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from 'react-router-dom'
import AddIngredient from './AddIngredient'
import FermentableEntry from './FermentableEntry'
import HopEntry from './HopEntry'
import YeastEntry from './YeastEntry'



const Assembly = (props) => {
  const [recipe, setRecipe] = useState( props.recipe ? props.recipe : {
    'name':'',
    'fermentables':[],
    'hops':[],
    'yeasts':[],
    'id':null
  })

  return (
    <>
      <h1>Assembly</h1>
      { !props.recipe && <Redirect to='/app/dashboard' />}
      <Router>
        <Switch>
          <Route path='/app/assembly/fermentables'>
            <div>
              <FermentableEntry />
              <AddIngredient type='fermentables'/>
              <Link to='/app/assembly/hops'>Save Fermentables</Link>
            </div>
          </Route>
          <Route path='/app/assembly/hops'>
            <div>
              <HopEntry />
              <AddIngredient type='hops'/>
              <Link to='app/assembly/fermentables'>Back to fermentables</Link>
              <Link to='app/assembly/yeast'>On to the yeast/bacteria</Link>
            </div>
          </Route>
          <Route path='/app/assembly/yeast'>
            <div>
              <YeastEntry />
              <AddIngredient type='yeast'/>
              <Link to='app/assembly/fermentables'>Back to fermentables</Link>
              <Link to='app/assembly/hops/'>Back to hops</Link>
            </div>
          </Route>
        </Switch>
      </Router>
    </>
  )
}

export default Assembly