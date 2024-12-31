import React, { useState } from 'react';
import styles from './InferencingForm.module.css';

const InferencingForm: React.FC = () => {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError(null); // Reset error state
    setResult(null); // Reset result state

    // اعتبارسنجی ورودی
    if (!expression.trim()) {
      setError('لطفاً یک عبارت منطقی وارد کنید.');
      return;
    }

    setLoading(true); // Set loading state
    try {
      const response = await fetch('/api/infer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression }),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error:', error);
      setError('خطایی رخ داده است.');
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <label htmlFor="expression" className={styles.label}>عبارت منطقی:</label>
      <input
        type="text"
        id="expression"
        value={expression}
        onChange={(e) => setExpression(e.target.value)}
        className={styles.input}
      />
      <button type="submit" className={styles.button} disabled={loading}>
        {loading ? 'در حال استنتاج...' : 'استنتاج'}
      </button>
      {result && <p className={styles.result}>{result}</p>}
      {error && <p className={styles.error}>{error}</p>}
    </form>
  );
};

export default InferencingForm;