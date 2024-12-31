grammar logic_grammar;

// Parser Rules
formula
    : quantifiedFormula
    | binaryFormula
    | unaryFormula
    | atom
    | '(' formula ')'
    ;

quantifiedFormula
    : QUANTIFIER VARIABLE formula
    ;

binaryFormula
    : atom binaryOpRest*
    ;

binaryOpRest
    : BINARY_OP formula
    ;

unaryFormula
    : NOT formula
    ;

atom
    : PREDICATE ('(' term (',' term)* ')')?
    ;

term
    : VARIABLE
    | CONSTANT
    ;

// Lexer Rules
QUANTIFIER: 'forall' | 'exists' ;
BINARY_OP: 'and' | 'or' | 'implies' ;
NOT: 'not' ;
PREDICATE: [a-zA-Z]+ ;
VARIABLE: [a-z] ;
CONSTANT: [A-Z] ;
WS: [ \t\r\n]+ -> skip ;