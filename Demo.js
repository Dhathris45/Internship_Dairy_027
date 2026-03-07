import React, {useState,useEffect} from "react";

function Demo(){

const [count,setCount] = useState(0);

useEffect(()=>{
setTimeout(()=>{
setCount(count+1);
},1000)
} , [] );

return(
<>
<h2>The page has rendered {count} times</h2>
</>
)

}

export default Demo;