import React from "react";

function Promote() {

const employees = ["Anu","Milind","Surya","Ramesh","Kiran"];

const staff = [
{
id:1,
name:"Kiran",
qualification:"Engineer",
pic:"https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg",
desc:"Kiran is from Bangalore. He joined the company in the year 2012."
},
{
id:2,
name:"Jitesh",
qualification:"Accountant",
pic:"https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg",
desc:"Jitesh is from Jaipur. He joined the company in the year 2016."
},
{
id:3,
name:"Sonam",
qualification:"HR MBA",
pic:"https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg",
desc:"Sonam is from Mumbai. She joined the company in the year 2015."
}
];

return (
<>
<h1>Employee Promotion Module!</h1>

<table className="table">
<thead>
<tr>
<th>Employee#</th>
<th>Employee</th>
<th>Promote</th>
</tr>
</thead>

<tbody>
{employees.map((emp,index)=>(
<tr key={index}>
<td>{index+1}</td>
<td>Mr/Ms {emp}</td>
<td>
<button className="btn btn-success">Promote</button>
</td>
</tr>
))}
</tbody>
</table>


<div className="container mt-5">

{staff.map((item)=>(
  
<div key={item.id} className="card mb-4" style={{width:"18rem"}}>
  
<img src={item.pic} className="card-img-top" alt="staff"/>

<div className="card-body">

<h5 className="card-title text-primary">
{item.name}
</h5>

<h6>{item.qualification}</h6>

<p className="card-text">
{item.desc}
</p>

<button className="btn btn-primary">
Read more...
</button>

</div>

</div>

))}

</div>

</>
);

}

export default Promote;