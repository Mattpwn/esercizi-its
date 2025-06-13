
import { Component } from 'react';
import './App.css';
import Componente1 from './Componente1';

function getDate(date) {

  return date.toLocaleDateString()+ " " + date.toLocaleTimeString();
}

function App(){
  let nome = "Matteo";
  return (
    <div className="App">
     <h1> Prima App React {nome}</h1>
     <h2>
      {

        new Date().toLocaleDateString()+" "+new Date().toLocaleTimeString()

      }
     </h2>
     <Componente1></Componente1>
     <h3> {getDate(new Date())}</h3>
    </div>
  );
}

export default App;
