// App.tsx
import React, { useState, useEffect } from 'react';
import { Form } from './form';
import { Footer } from './footer';
import Result from './Result';

function App() {
  const [data, setData] = useState<{ status: string; message: string; predicted_salary: number } | null>(
    null,
  );
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // fetchData(NULL);
  }, []);

  const handleSubmit = (values: Record<string, string>) => {
    console.log(values);
    fetchData(values);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

    // this is how we're going to retrieve data from the backend:
  const fetchData = (values: Record<string, string>) => {
    setIsLoading(true);
    setIsModalOpen(true);
    fetch('http://localhost:5000/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(values),
    })
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setIsLoading(false);
      });
  };

  return (
    <div className="particle-background">
      <Form onSubmit={handleSubmit} />
      <Result
        isOpen={isModalOpen}
        onClose={closeModal}
        status={data?.status || ''}
        message={data?.message || ''}
        predictedSalary={data?.predicted_salary || 0}
        isLoading={isLoading}
      />
      <Footer />
    </div>
  );
}

export default App;
