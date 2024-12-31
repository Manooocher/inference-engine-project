import antlr4
from antlr4 import CommonTokenStream, InputStream
from .logic_grammarLexer import logic_grammarLexer
from .logic_grammarParser import logic_grammarParser


# کلاس LogicTreeVisitor برای پیمایش درخت نحوی و تبدیل آن به JSON
class LogicTreeVisitor:
    def __init__(self):
        self.json_tree = {}  # ساختار اولیه JSON

    # متدی برای بازدید از گره‌های درخت نحوی
    def visit(self, tree, parser):
        # اگر گره فرزند ندارد، مقدار متن آن گره بازگردانده می‌شود
        if tree.getChildCount() == 0:
            return tree.getText()
        
        # دریافت نام Rule فعلی از گرامر
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        
        # مدیریت گره‌های مربوط به quantifiedFormula (عبارات کوانتیده)
        if rule_name == 'quantifiedFormula':
            return {
                'type': 'quantifier',  # نوع گره
                'quantifier': tree.getChild(0).getText(),  # نوع کوانتور (forall یا exists)
                'variable': tree.getChild(1).getText(),  # متغیر کوانتیده
                'formula': self.visit(tree.getChild(2), parser)  # فرمول داخلی
            }
        
        # مدیریت گره‌های مربوط به binaryFormula (عبارات دوتایی)
        elif rule_name == 'binaryFormula':
            return {
                'type': 'binary',  # نوع گره
                'operator': tree.getChild(1).getText(),  # عملگر (and, or, implies)
                'left': self.visit(tree.getChild(0), parser),  # سمت چپ عملگر
                'right': self.visit(tree.getChild(2), parser)  # سمت راست عملگر
            }
        
        # مدیریت گره‌های مربوط به unaryFormula (عبارات تک‌تایی)
        elif rule_name == 'unaryFormula':
            return {
                'type': 'unary',  # نوع گره
                'operator': 'not',  # عملگر not
                'formula': self.visit(tree.getChild(1), parser)  # فرمول داخلی
            }
        
        # مدیریت گره‌های مربوط به atom (پیش‌فرض یا محمولات)
        elif rule_name == 'atom':
            if tree.getChildCount() > 1:
                # اگر گره شامل محمول باشد
                terms = []
                for i in range(2, tree.getChildCount() - 1):  # پردازش آرگومان‌های محمول
                    if tree.getChild(i).getText() != ',':
                        terms.append(self.visit(tree.getChild(i), parser))
                return {
                    'type': 'predicate',  # نوع گره
                    'name': tree.getChild(0).getText(),  # نام محمول
                    'terms': terms  # آرگومان‌ها
                }
            return {
                'type': 'proposition',  # گزاره ساده
                'name': tree.getChild(0).getText()  # نام گزاره
            }
        
        # در صورت عدم انطباق، بازدید از فرزند اول گره
        return self.visit(tree.getChild(0), parser)

# تابعی برای پردازش ورودی منطقی و تبدیل آن به JSON
def parse_logic_formula(input_string):
    # ایجاد Lexer و Parser از ورودی
    input_stream = InputStream(input_string)  # تبدیل ورودی به جریان ورودی
    lexer = logic_grammarLexer(input_stream)  # Lexer
    stream = CommonTokenStream(lexer)  # جریان توکن‌ها
    parser = logic_grammarParser(stream)  # Parser
    
    # تجزیه ورودی و ایجاد درخت نحوی
    tree = parser.formula()
    
    # تبدیل درخت نحوی به JSON با استفاده از کلاس LogicTreeVisitor
    visitor = LogicTreeVisitor()
    json_tree = visitor.visit(tree, parser)
    
    return json_tree  # بازگرداندن خروجی JSON