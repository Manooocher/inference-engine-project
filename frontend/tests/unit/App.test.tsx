import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '../../src/App';

describe('App Component', () => {
  it('should render welcome message', () => {
    // رندر کردن کامپوننت App
    const { getByText } = render(<App />);
    // بررسی اینکه پیام خوش‌آمدگویی به درستی رندر شده است
    expect(getByText('Welcome to the Inference Engine Project')).toBeInTheDocument();
  });
});