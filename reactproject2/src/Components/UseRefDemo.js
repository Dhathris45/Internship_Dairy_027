import React,{useState,useRef} from "react";

function UseRefDemo(){

const [name,setName] = useState("");

const refName = useRef();

function cleartext(){

setName("");

refName.current.focus();

}

function changeText(){

refName.current.style.color="red";

}

return(

<div>

<label>Enter your Name:</label>

<input
ref={refName}
type="text"
value={name}
onChange={(e)=>setName(e.target.value)}
/>

<br/><br/>

<label>Enter your Phone:</label>
<input type="text"/>

<br/><br/>

<button onClick={cleartext}>Clear</button>

<button onClick={changeText}>Change Text</button>

</div>

)

}

export default UseRefDemo;