import { Router } from 'express';
import { getSampleData } from '../controllers/sampleController';

const router = Router();

// تعریف مسیر GET برای دریافت داده‌های نمونه
router.get('/sample', getSampleData);

export default router;