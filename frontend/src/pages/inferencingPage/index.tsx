import React from 'react';
import Layout from '../../components/layout/Layout';
import InferencingForm from '../../components/inferencingForm/InferencingForm';

// کامپوننت صفحه Inferencing
const InferencingPage: React.FC = () => {
  return (
    <Layout>
      <div className="inferencing-container">
        <h2>سیستم استنتاج</h2>
        <InferencingForm />
      </div>
    </Layout>
  );
};

export default InferencingPage;