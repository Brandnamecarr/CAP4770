// Results.tsx
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import { faMoneyBillAlt } from '@fortawesome/free-solid-svg-icons';

interface ResultProps {
  status: string;
  message: string;
  predictedSalary: number;
  onClose: () => void;
  isOpen: boolean;
  isLoading: boolean;
}

const Result: React.FC<ResultProps> = ({ status, message, predictedSalary, onClose, isOpen, isLoading }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal">
        <span className="close" onClick={onClose}>
          &times;
        </span>
        
          {isLoading ? (
            <div className="loading-container">
              <p>Predicting your Salary...</p>
              <FontAwesomeIcon className="spinner" icon={faSpinner} spin />
            </div>
          ) : (
            <>
  <h2 className="salary-heading">Your predicted Salary is:</h2>
  <p className="salary-value">
    <FontAwesomeIcon icon={faMoneyBillAlt} />
    <span>{predictedSalary}</span>
  </p>
</>

          )}
        
      </div>
    </div>
  );
};

export default Result;
