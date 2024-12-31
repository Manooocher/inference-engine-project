import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// رندر کردن کامپوننت App در عنصر با شناسه root
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(<App />);