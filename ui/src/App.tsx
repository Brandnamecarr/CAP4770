import React, { useState, useEffect } from 'react';
import { Form } from './form';
import { Footer} from './footer';

function App() {
  const [data, setData] = useState({ message: '' });

  useEffect(() => {
    //fetchData(NULL);
  }, []);

  const handleSubmit = (values: Record<string, string>) => {
    console.log(values);
    fetchData(values);
  };

  // this is how we're going to retrieve data from the backend:
  const fetchData = (values: Record<string, string>) => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>{data.message}</h1>
      <Form onSubmit={handleSubmit} />
      <Footer />
    </div>
  );
}

export default App;
