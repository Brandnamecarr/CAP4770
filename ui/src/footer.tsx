import React, { useState } from 'react';
import { Modal } from './Modal';

export const Footer: React.FC = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <div className="footer">
      <h5>In addition to the above form, you can view the following visualizations of the StackOverflow data:</h5>
      <div>
        <button onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey', '_blank')}>
          View Raw Data
        </button>
        <button onClick={() => setShowModal(true)}>
          View Data by Salary
        </button>
        <button onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#state', '_blank')}>
          View Data by State
        </button>
        <button onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#devtype', '_blank')}>
          View Data by Role Type
        </button>
      </div>
      {showModal && <Modal onClose={() => setShowModal(false)} />}
    </div>
  );
};
