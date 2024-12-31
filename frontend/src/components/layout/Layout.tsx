import React from 'react';

// تعریف نوع Props برای کامپوننت Layout
interface LayoutProps {
  children: React.ReactNode;
}

// کامپوننت Layout که به عنوان قالب اصلی صفحات استفاده می‌شود
const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout">
      {/* هدر سایت */}
      <header>
        <h1>موتور استنتاج منطقی</h1>
      </header>
      {/* محتوای اصلی که از طریق props دریافت می‌شود */}
      <main>{children}</main>
      {/* فوتر سایت */}
      <footer>
        <p>پروژه استنتاج گزاره - رفع تکلیف درس مبانی ریاضی استاد آقایی - ۱۴۰۲</p>
      </footer>
    </div>
  );
};

export default Layout;