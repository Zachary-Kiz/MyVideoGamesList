import react from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Register from './pages/Register/Register.jsx'
import NavBar from './components/NavBar/NavBar.jsx';
import Login from './pages/Login/Login.jsx';
import './App.css'
import { AuthContextProvider } from '../context/AuthContext.jsx';


function App() {

  return (
    <div>
    <NavBar></NavBar>
    <AuthContextProvider>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<div>TEST</div>}/>
        <Route path='/user/login' element={<Login/>}/>
        <Route path='/user/register' element={<Register/>}/>
      </Routes>
    </BrowserRouter>
    </AuthContextProvider>
    </div>
  )
}

export default App;
