import React from "react";

function Exam(props){

return(

<div className="container" style={{
backgroundColor:"lightblue",
borderRadius:"12px",
width:"250px",
padding:"20px",
margin:"20px"
}}>

<div className="jumbotron">

<h1 className="display-4">{props.name}</h1>

<p className="lead">
Exam details coming from the child component
</p>

<hr/>

<p>Subject: {props.subject}</p>

<p>Date: {props.date}</p>

<button className="btn btn-primary">
View Exam Report
</button>

</div>

</div>

)

}

export default Exam;