import React, {useState,useEffect} from "react";

function PostList(){

const [posts,setPosts] = useState([]);

useEffect(()=>{

fetch("https://jsonplaceholder.typicode.com/posts")

.then((response)=>{
if(!response.ok){
throw new Error("Network Error");
}
return response.json();
})

.then((data)=>{
setPosts(data);
console.log("Data fetched successfully");
})

.catch(()=>{
console.log("Oops! There is an issue with the URL");
});

},[]);

function handleDelete(id){

const newPosts = posts.filter((post)=>post.id !== id);

setPosts(newPosts);

}

return(

<div className="container">

<h1 className="display-1">Posts</h1>

<table className="table table-bordered">

<thead>
<tr>
<th>ID</th>
<th>Title</th>
<th>Body</th>
<th>Delete</th>
</tr>
</thead>

<tbody>

{posts.map((post)=>(
<tr key={post.id}>
<td>{post.id}</td>
<td>{post.title}</td>
<td>{post.body}</td>

<td>
<button
className="btn btn-danger"
onClick={()=>handleDelete(post.id)}
>
Delete
</button>
</td>

</tr>
))}

</tbody>

</table>

</div>

)

}

export default PostList;