import { Request, Response } from 'express';

// کنترلر برای دریافت داده‌های نمونه
export const getSampleData = (req: Request, res: Response) => {
  res.json({ message: 'This is sample data' });
};