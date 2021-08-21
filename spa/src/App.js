import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/errors/NotFound'
function App() {

  return (
    <Router>
      <Switch>
      <Route path='/login' component={Login} />
      <Route path='/' component={Home} exact></Route>
      <Route component={NotFound} />
      </Switch>
    </Router>
  );
}

export default App;
