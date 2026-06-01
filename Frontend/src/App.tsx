import './App.css'
import { useState } from 'react';
import axios from "axios";

function App() {
  const [name, setName] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async () => {
    const request = axios.post("http://localhost:8000/messages/", {
      name: name,
      msg: msg
    });
    const response = await request;
    if (response.status === 200) {
      alert('Message sent successfully');
    } else {
      alert("Failed to send message");
    }
  };

  return (
    <>
    <div className="App">
      <h1>Welcome to my K8s App</h1>
      <input type="text" placeholder="Enter your name" id="name" value={name} onChange={(e) => setName(e.target.value)}/>
      <br></br>
      <input type="text" placeholder="Enter your message" id="msg" value={msg} onChange={(e) => setMsg(e.target.value)}/>
      <br></br>
      <button onClick={handleSubmit} >Submit</button> 
    </div>
    </>
  )
}

export default App
