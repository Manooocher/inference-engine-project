import { Request, Response, NextFunction } from 'express';

// میان‌افزار برای لاگ کردن درخواست‌ها
const logger = (req: Request, res: Response, next: NextFunction) => {
  console.log(`${req.method} ${req.path}`);
  next();
};

export default logger;