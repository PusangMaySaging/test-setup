import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/errors/NotFound'
import Toast from './components/Toast'
function App() {

  return (
    <div className="bg-gray-50">
    <Router>
      <Switch>
      <Route path='/login' component={Login} />
      <Route path='/' component={Home} exact></Route>
      <Route component={NotFound} />
      </Switch>
    </Router>
    <Toast></Toast>
    </div>
  );
}

export default App;
