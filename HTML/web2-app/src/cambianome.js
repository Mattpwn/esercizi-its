import { useState } from 'react'

const CambiaNome = () => {
    const [nome, setNome] = useState ("Matteo");

    const cambia = () => {
        if (nome === "Matteo"){
            setNome ("Camilla")

        }else{
            setNome ("Matteo")
        }
    }    

    //     setNome(current=>{
    //         if (current==="Matteo")
    //             return "Camilla"
    //         return "Matteo";
    // })



    return (
        <div>
            {nome}
            <button class="btn btn-dark" onClick= {cambia} > cambia</button>
        
            </div>
  )
}
export default CambiaNome