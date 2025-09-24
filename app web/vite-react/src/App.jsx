import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Saluto from './esercizi/Esercizi_1/Saluto'
import UserAlbumsFullStack from './UserAlbumsFullstack'
import CardUtente from './esercizi/Esercizio_2/CardUtente'
import MenuRistorante from './esercizi/Esercizi_3/MenuRistorante'
import ToDoApp from './todolist/ToDoApp'




function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     
     <ToDoApp></ToDoApp>
     
     </>
  )
}

export default App
