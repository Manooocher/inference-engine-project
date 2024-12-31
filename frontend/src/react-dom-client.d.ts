// اعلام یک ماژول جدید به نام 'react-dom/client'
declare module 'react-dom/client' {
  // وارد کردن نوع ReactNode از کتابخانه React
  import { ReactNode } from 'react';
  // وارد کردن نوع Root از کتابخانه react-dom
  import { Root } from 'react-dom';

  // تعریف یک اینترفیس برای تابع CreateRoot
  interface CreateRoot {
    // تابع CreateRoot که یک عنصر HTML یا DocumentFragment و یک شیء اختیاری برای تنظیمات را می‌پذیرد و یک Root برمی‌گرداند
    (container: Element | DocumentFragment, options?: { hydrate?: boolean }): Root;
  }

  // صادر کردن تابع createRoot به عنوان یک CreateRoot
  export const createRoot: CreateRoot;
}