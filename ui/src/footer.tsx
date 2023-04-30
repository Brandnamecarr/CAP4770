import React, { useState } from 'react';
import { Modal } from './Modal';
import AverageSalary from './static/average_salary.png';
import AverageSalaryExperience from './static/average_salary_by_years_experience.png';
import JobSatisfactionByCompanySize from './static/job_satisfaction_by_company_size.png';
import SalaryByCountry from './static/salary_by_top_countries.png';


export const Footer: React.FC = () => {
  const [showModal, setShowModal] = useState(false);
  const [modalImageSrc, setModalImageSrc] = useState('');

  const openModalWithImage = (src: string) => {
    setModalImageSrc(src);
    setShowModal(true);
  };

  return (
    <div className="footer">
      <h5>In addition to the above form, you can view the following visualizations of the StackOverflow data:</h5>
      <div>
        <button onClick={() => window.open('https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey', '_blank')}>
          View Raw Data
        </button>
        <button onClick={() => openModalWithImage(AverageSalary)}>
          Avg Salary by Education Type
        </button>
        <button onClick={() => openModalWithImage(AverageSalaryExperience)}>
          Avg Salary by Years of Experience and Education Type
        </button>
        <button onClick={() => openModalWithImage(JobSatisfactionByCompanySize)}>
          Satisfaction by Company Size
        </button>
        <button onClick={() => openModalWithImage(SalaryByCountry)}>
          Salary by Top 10 Countries
        </button>
      </div>
      {showModal && <Modal imageSrc={modalImageSrc} onClose={() => setShowModal(false)} />}
    </div>
  );
};
