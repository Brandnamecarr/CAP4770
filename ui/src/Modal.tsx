import React from 'react';

type ModalProps = {
  onClose: () => void;
  imageSrc: string;
};

export const Modal: React.FC<ModalProps> = ({ onClose, imageSrc }) => {
  return (
    <div className="modal-overlay">
      <div className="modal">
        <span className="close" onClick={onClose}>&times;</span>
        <div className="modal-content">
          <img src={imageSrc} alt="Modal Visualization" />
        </div>
      </div>
    </div>
  );
};
