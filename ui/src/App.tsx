import React, { useState, useEffect } from 'react';
import { Form } from './form';

function App() {
  const [data, setData] = useState({ message: '' });

  useEffect(() => {
    fetchData();
  }, []);

  const handleSubmit = (values: Record<string, string>) => {
    console.log(values);
  };

  // this is how we're going to retrieve data from the backend:
  const fetchData = () => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>{data.message}</h1>
      <Form onSubmit={handleSubmit} />
    </div>
  );
}

export default App;
