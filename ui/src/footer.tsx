import React, { useState } from 'react';
import { Modal } from './Modal';

export const Footer: React.FC = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <div style={{ marginTop: '2rem', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <h5 style={{ marginBottom: '0.5rem' }}>In addition to the above form, you can view the following visualizations of the StackOverflow data:</h5>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <button style={{ margin: '0 0.5rem' }} onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey', '_blank')}>
          View Raw Data
        </button>
        <button style={{ margin: '0 0.5rem' }} onClick={() => setShowModal(true)}>
          View Data by Salary
        </button>
        <button style={{ margin: '0 0.5rem' }} onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#state', '_blank')}>
          View Data by State
        </button>
        <button style={{ margin: '0 0.5rem' }} onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#devtype', '_blank')}>
          View Data by Role Type
        </button>
      </div>
      {showModal && <Modal onClose={() => setShowModal(false)} />}
    </div>
  );
};
