import { getSampleData } from '../../src/controllers/sampleController';
import { Request, Response } from 'express';

describe('Sample Controller', () => {
  it('should return sample data', () => {
    // شبیه‌سازی درخواست و پاسخ
    const req = {} as Request;
    const res = {
      json: jest.fn()
    } as unknown as Response;

    // فراخوانی کنترلر
    getSampleData(req, res);

    // بررسی اینکه پاسخ به درستی داده شده است
    expect(res.json).toHaveBeenCalledWith({ message: 'This is sample data' });
  });
});