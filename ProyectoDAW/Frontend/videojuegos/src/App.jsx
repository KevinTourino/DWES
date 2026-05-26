import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from './components/Home'
import Login from './components/auth/login'
import Register from './components/auth/register'
import Layout from './components/layaout/Layout'
import Library from './components/Library'
import AddGames from './components/AddGame'
import GameDetail from './components/GameDetail'
import NotFound from './components/NotFound'
import ProtectedRoute from './components/auth/ProtectRoute'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          
          <Route index element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route
            path="/library"
            element={
              <ProtectedRoute>
                <Library />
              </ProtectedRoute>
            }
          />

          <Route
            path="/addGame"
            element={
              <ProtectedRoute>
                <AddGames />
              </ProtectedRoute>
            }
          />

          <Route
            path="/game/:id"
            element={
              <ProtectedRoute>
                <GameDetail />
              </ProtectedRoute>
            }
          />

          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App