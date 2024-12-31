import express from 'express';
import sampleRoutes from './routes/sampleRoutes';
import logger from './middlewares/logger';

const app = express();

// استفاده از middleWare برای parse کردن JSON
app.use(express.json());

// استفاده از middleWare لاگ کردن درخواست‌ها
app.use(logger);

// استفاده از مسیرهای نمونه
app.use('/api', sampleRoutes);

// مسیر اصلی برای تست سرور
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

export default app;