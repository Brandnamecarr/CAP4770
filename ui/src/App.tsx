import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({ message: '' });

  useEffect(() => {
    fetchData();
  }, []);

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
    </div>
  );
}

export default App;
