import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    try {
      console.log('Sending request...');
      const res = await axios.post('http://localhost:5000/generate', { prompt });
      console.log('Response received:', res.data);
      setResponse(res.data.generated_text);
    } catch (error) {
      console.error('Error en la solicitud:', error);
    }
  };

  return (
    <div>
      <h1>Generador de Texto con GPT-3</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows="5"
        cols="50"
      />
      <br />
      <button onClick={handleSubmit}>Generar</button>
      <h2>Respuesta:</h2>
      <p>{response}</p>
    </div>
  );
}

export default App;
