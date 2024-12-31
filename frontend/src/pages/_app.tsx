import React from 'react';
import { AppProps } from 'next/app';

// کامپوننت سفارشی MyApp برای Next.js
const MyApp = ({ Component, pageProps }: AppProps) => {
  return <Component {...pageProps} />;
};

export default MyApp;