import React from 'react';
import App from '../App';
import styles from '../components/inferencingForm/InferencingForm.module.css';

const HomePage: React.FC = () => {
  return (
    <form className={styles.form}>
      <label className={styles.label}>Label</label>
      <input className={styles.input} type="text" />
      <button className={styles.button}>Submit</button>
    </form>
  );
};

export default HomePage;