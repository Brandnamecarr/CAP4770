import React from 'react';
import AverageSalary from './static/average_salary.png';

type ModalProps = {
  onClose: () => void;
};

export const Modal: React.FC<ModalProps> = ({ onClose }) => {
  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <img src={AverageSalary} alt="Average Salary" />
      </div>
    </div>
  );
};
