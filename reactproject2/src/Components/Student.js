import React from "react";
import Exam from "./Exam";

function Student(){

const students = [

{ id:1, name:"Kiran Kumar", subject:"Maths", date:"December 23rd" },

{ id:2, name:"Chandrakant More", subject:"Java", date:"Jan 23rd" },

{ id:3, name:"Surya Singh", subject:"Python", date:"Jan 23rd" }

];

return(

<>
<div>Student</div>

{
students.map((stud)=>(
<Exam
name={stud.name}
subject={stud.subject}
date={stud.date}
/>
))
}

</>

)

}

export default Student;