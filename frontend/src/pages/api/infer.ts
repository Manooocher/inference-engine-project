import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
  result: string;
  success: boolean;
};

// تابع ارزیابی عبارات منطقی
function evaluateLogicalExpression(expression: string): string {
  // حذف فاصله‌های اضافی
  const cleanExpression = expression.trim().toUpperCase();

  // بررسی عملگرها
  if (cleanExpression.includes('AND')) {
    const parts = cleanExpression.split('AND').map(part => part.trim());
    return `AND operation with operands: ${parts.join(' and ')}`;
  } else if (cleanExpression.includes('OR')) {
    const parts = cleanExpression.split('OR').map(part => part.trim());
    return `OR operation with operands: ${parts.join(' or ')}`;
  } else if (cleanExpression.includes('NOT')) {
    const operand = cleanExpression.replace('NOT', '').trim();
    return `NOT operation on: ${operand}`;
  }

  return 'Invalid expression - please use AND, OR, or NOT operators';
}

export default function handler(req: NextApiRequest, res: NextApiResponse<Data>) {
  try {
    if (req.method !== 'POST') {
      console.log('Invalid method:', req.method);
      return res.status(405).json({ result: 'Method not allowed', success: false });
    }

    const { expression } = req.body;
    console.log('Received expression:', expression);

    if (!expression || typeof expression !== 'string') {
      return res.status(400).json({
        result: 'Invalid input expression',
        success: false
      });
    }

    // ارزیابی عبارت منطقی
    const result = evaluateLogicalExpression(expression);
    console.log('Evaluation result:', result);
    
    return res.status(200).json({ 
      result,
      success: true 
    });

  } catch (error) {
    console.error('API Error:', error);
    return res.status(500).json({ 
      result: 'Server error', 
      success: false 
    });
  }
}