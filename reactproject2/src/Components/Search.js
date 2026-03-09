import React,{useState} from "react";

function Search(){

const customers = [

"Zuber Khan",
"Tarun B",
"Tarun M",
"Junaid Khan",
"Ruhi Khan"

];

const [search,setSearch] = useState("");

const filtered = customers.filter((name)=>
name.toLowerCase().includes(search.toLowerCase())
);

return(

<div>

<h1>Search customer name:</h1>

<input
type="text"
value={search}
onChange={(e)=>setSearch(e.target.value)}
/>

<ul>

{
filtered.map((item,index)=>(
<li key={index}>{item}</li>
))
}

</ul>

</div>

)

}

export default Search;