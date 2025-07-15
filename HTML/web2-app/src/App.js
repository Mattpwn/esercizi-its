

import './App.css';

import CambiaNome from './cambianome';

function getDate(date) {

  return date.toLocaleDateString()+ " " + date.toLocaleTimeString();
}

function App(){
  let nome = "Matteo";
  return (
    <div className='App'>
    <CambiaNome></CambiaNome>
    </div>
  );
}

export default App;
