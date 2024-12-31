module.exports = {
  // استفاده از پیش‌تنظیم ts-jest برای TypeScript
  preset: 'ts-jest',
  // تنظیم محیط تست به jsdom برای تست‌های فرانت‌اند
  testEnvironment: 'jsdom',
  // الگوی جستجوی فایل‌های تست
  testMatch: ['**/tests/**/*.test.tsx']
};