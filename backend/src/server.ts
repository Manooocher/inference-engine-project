import app from './app';
import dotenv from 'dotenv';

// بارگذاری تنظیمات محیطی از فایل .env
dotenv.config();

// استفاده از پورت از تنظیمات محیطی یا پورت 3000 به صورت پیش‌فرض
const PORT = process.env.PORT || 3000;

// راه‌اندازی سرور
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});