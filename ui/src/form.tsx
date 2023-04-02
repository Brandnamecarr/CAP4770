import React, { useState } from 'react';

interface FormProps {
  onSubmit: (values: Record<string, string>) => void;
}

const careerOptions = ['Software Engineer', 'Data Scientist', 'Product Manager'];
const yearsOptions = ['0-2', '2-5', '5+'];
const stateOptions = ['California', 'New York', 'Texas', 'Florida'];
const educationOptions = ['Bachelor', 'Master', 'PhD'];
const technologyOptions = ['Python', 'Java', 'JavaScript', 'C#'];

export const Form: React.FC<FormProps> = ({ onSubmit }) => {
  const [career, setCareer] = useState('');
  const [yearsOfExperience, setYearsOfExperience] = useState('');
  const [state, setState] = useState('');
  const [education, setEducation] = useState('');
  const [technology, setTechnology] = useState('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSubmit({ career, yearsOfExperience, state, education, technology });
  };

  const isFormValid = () => {
    return career && yearsOfExperience && state && education && technology;
  };

  return (
    <div>
    <center>
    <h2>Welcome to our technology role salary estimator!</h2>
    <p>By providing us with the below input, we will use data from the 2018 StackOverflow developer survey to estimate and model your expected salary. </p>
    </center>
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <center>
      <p>
        I am a&nbsp;
        <select value={career} onChange={(event) => setCareer(event.target.value)}>
          <option value="">Select career</option>
          {careerOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        &nbsp;with&nbsp;
        <select value={yearsOfExperience} onChange={(event) => setYearsOfExperience(event.target.value)}>
          <option value="">Select years of experience</option>
          {yearsOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        &nbsp;living in&nbsp;
        <select value={state} onChange={(event) => setState(event.target.value)}>
          <option value="">Select state</option>
          {stateOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        . My educational background is&nbsp;
        <select value={education} onChange={(event) => setEducation(event.target.value)}>
          <option value="">Select education background</option>
          {educationOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        <br />
        &nbsp;and my main technology is&nbsp;
        <select value={technology} onChange={(event) => setTechnology(event.target.value)}>
          <option value="">Select main technology</option>
          {technologyOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        .
      </p>
      <button type="submit" disabled={!isFormValid()}>
        Submit
      </button>
      </center>
    </form>
    </div>
  );
};