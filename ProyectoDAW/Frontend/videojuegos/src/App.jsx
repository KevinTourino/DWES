import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from './components/home'
import Login from './components/auth/login'
import Layout from './components/layaout/Layout'
import Library from './components/library'
import AddGames from './components/addGame'
import NotFound from './components/notfound'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/library" element={<Library />} />
          <Route path="/addGame" element={<AddGames />} />

          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
