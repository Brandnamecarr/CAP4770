import React, { useState } from 'react';
import './App.css';

interface FormProps {
  onSubmit: (values: Record<string, string>) => void;
}

const careerOptions = ['Software Engineer', 'Data Scientist', 'Product Manager'];
const yearsOptions = ['0-2', '2-5', '5+'];
const educationOptions = ['Bachelor', 'Master', 'PhD'];
const technologyOptions = ['Python', 'Java', 'JavaScript', 'C#'];

export const Form: React.FC<FormProps> = ({ onSubmit }) => {
  const [career, setCareer] = useState('');
  const [yearsOfExperience, setYearsOfExperience] = useState('');
  const [education, setEducation] = useState('');
  const [technology, setTechnology] = useState('');
  const [formError, setFormError] = useState('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!isFormValid()) {
      setFormError('Please fill in all fields');
      return;
    }
    onSubmit({ career, yearsOfExperience, education, technology });
  };

  const isFormValid = () => {
    return career && yearsOfExperience && education && technology;
  };

  return (
    <div className="form-container">
      <div className="form-header">Welcome to our technology role salary estimator!</div>
      <p className="form-paragraph">
        By providing us with the below input, we will use data from the 2018 StackOverflow developer survey to estimate and
        model your expected salary.
      </p>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="career">I am a</label>
          <select
            id="career"
            className="form-select"
            value={career}
            onChange={(event) => setCareer(event.target.value)}
          >
            <option value="">Select career</option>
            {careerOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="yearsOfExperience">with</label>
          <select
            id="yearsOfExperience"
            className="form-select"
            value={yearsOfExperience}
            onChange={(event) => setYearsOfExperience(event.target.value)}
          >
            <option value="">Select years of experience</option>
            {yearsOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="education">My educational background is</label>
          <select
            id="education"
            className="form-select"
            value={education}
            onChange={(event) => setEducation(event.target.value)}
          >
            <option value="">Select education background</option>
            {educationOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="technology">and my main technology is</label>
          <select
            id="technology"
            className="form-select"
            value={technology}
            onChange={(event) => setTechnology(event.target.value)}
          >
            <option value="">Select main technology</option>
            {technologyOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <button type="submit" className="form-button" disabled={!isFormValid()}>
            Submit
          </button>
        </div>
      </form>
    </div>
  );
 }