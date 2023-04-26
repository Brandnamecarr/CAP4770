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
    fetch('http://localhost:5000/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(values),
    })
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error(error));
  };


  return (
    <div className="particle-background">
      <Form onSubmit={handleSubmit} />
      <Footer />
    </div>
  );
}

export default App;
