from sym_def import BNF, TokenType, NonTerminal

"""
产生式列表，用来构建语法树
"""
ExpressionTable = [
    BNF(-1, (-1)),  # 占用YACC第0条生成式的下标
    BNF(
        NonTerminal.program,
        (
            NonTerminal.declaration_list,
        )
    ),
    BNF(
        NonTerminal.declaration_list,
        (
            NonTerminal.declaration_list,
            NonTerminal.declaration,
        )
    ),
    BNF(
        NonTerminal.declaration_list,
        (
            NonTerminal.declaration,
        )
    ),
    BNF(
        NonTerminal.declaration,
        (
            NonTerminal.var_declaration,
        )
    ),
    BNF(
        NonTerminal.declaration,
        (
            NonTerminal.fun_declaration,
        )
    ),
    BNF(
        NonTerminal.var_declaration,
        (
            NonTerminal.type_specifier,
            TokenType.ID,
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.var_declaration,
        (
            NonTerminal.type_specifier,
            TokenType.ID,
            TokenType.LBRACKET,
            TokenType.NUM,
            TokenType.RBRACKET,
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.type_specifier,
        (
            TokenType.INT,
        )
    ),
    BNF(
        NonTerminal.type_specifier,
        (
            TokenType.VOID,
        )
    ),
    BNF(
        NonTerminal.fun_declaration,
        (
            NonTerminal.type_specifier,
            TokenType.ID,
            TokenType.LPAREN,
            NonTerminal.params,
            TokenType.RPAREN,
            NonTerminal.compound_stmt,
        )
    ),
    BNF(
        NonTerminal.params,
        (
            NonTerminal.param_list,
        )
    ),
    BNF(
        NonTerminal.params,
        (
            TokenType.VOID,
        )
    ),
    BNF(
        NonTerminal.param_list,
        (
            NonTerminal.param_list,
            TokenType.COMMA,
            NonTerminal.param,
        )
    ),
    BNF(
        NonTerminal.param_list,
        (
            NonTerminal.param,
        )
    ),
    BNF(
        NonTerminal.param,
        (
            NonTerminal.type_specifier,
            TokenType.ID,
        )
    ),
    BNF(
        NonTerminal.param,
        (
            NonTerminal.type_specifier,
            TokenType.ID,
            TokenType.LBRACKET,
            TokenType.RBRACKET,
        )
    ),
    BNF(
        NonTerminal.compound_stmt,
        (
            TokenType.LBRACE,
            NonTerminal.local_declarations,
            NonTerminal.statement_list,
            TokenType.RBRACE,
        )
    ),
    BNF(
        NonTerminal.local_declarations,
        (
            NonTerminal.local_declarations,
            NonTerminal.var_declaration,
        )
    ),
    BNF(
        NonTerminal.local_declarations,
        (
        )
    ),
    BNF(
        NonTerminal.statement_list,
        (
            NonTerminal.statement_list,
            NonTerminal.statement,
        )
    ),
    BNF(
        NonTerminal.statement_list,
        (
        )
    ),
    BNF(
        NonTerminal.statement,
        (
            NonTerminal.expression_stmt,
        )
    ),
    BNF(
        NonTerminal.statement,
        (
            NonTerminal.compound_stmt,
        )
    ),
    BNF(
        NonTerminal.statement,
        (
            NonTerminal.selection_stmt,
        )
    ),
    BNF(
        NonTerminal.statement,
        (
            NonTerminal.iteration_stmt,
        )
    ),
    BNF(
        NonTerminal.statement,
        (
            NonTerminal.return_stmt,
        )
    ),
    BNF(
        NonTerminal.expression_stmt,
        (
            NonTerminal.expression,
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.expression_stmt,
        (
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.selection_stmt,
        (
            TokenType.IF,
            TokenType.LPAREN,
            NonTerminal.expression,
            TokenType.RPAREN,
            NonTerminal.statement,
        )
    ),
    BNF(
        NonTerminal.selection_stmt,
        (
            TokenType.IF,
            TokenType.LPAREN,
            NonTerminal.expression,
            TokenType.RPAREN,
            NonTerminal.statement,
            TokenType.ELSE,
            NonTerminal.statement,
        )
    ),
    BNF(
        NonTerminal.iteration_stmt,
        (
            TokenType.WHILE,
            TokenType.LPAREN,
            NonTerminal.expression,
            TokenType.RPAREN,
            NonTerminal.statement,
        )
    ),
    BNF(
        NonTerminal.return_stmt,
        (
            TokenType.RETURN,
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.return_stmt,
        (
            TokenType.RETURN,
            NonTerminal.expression,
            TokenType.SEMI,
        )
    ),
    BNF(
        NonTerminal.expression,
        (
            NonTerminal.var,
            TokenType.ASSIGN,
            NonTerminal.expression,
        )
    ),
    BNF(
        NonTerminal.expression,
        (
            NonTerminal.simple_expression,
        )
    ),
    BNF(
        NonTerminal.var,
        (
            TokenType.ID,
        )
    ),
    BNF(
        NonTerminal.var,
        (
            TokenType.ID,
            TokenType.LBRACKET,
            NonTerminal.expression,
            TokenType.RBRACKET,
        )
    ),
    BNF(
        NonTerminal.simple_expression,
        (
            NonTerminal.additive_expression,
            NonTerminal.relop,
            NonTerminal.additive_expression,
        )
    ),
    BNF(
        NonTerminal.simple_expression,
        (
            NonTerminal.additive_expression,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.LT,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.LE,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.RT,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.RE,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.EQ,
        )
    ),
    BNF(
        NonTerminal.relop,
        (
            TokenType.NEQ,
        )
    ),
    BNF(
        NonTerminal.additive_expression,
        (
            NonTerminal.additive_expression,
            NonTerminal.addop,
            NonTerminal.term,
        )
    ),
    BNF(
        NonTerminal.additive_expression,
        (
            NonTerminal.term,
        )
    ),
    BNF(
        NonTerminal.addop,
        (
            TokenType.PLUS,
        )
    ),
    BNF(
        NonTerminal.addop,
        (
            TokenType.MINUS,
        )
    ),
    BNF(
        NonTerminal.term,
        (
            NonTerminal.term,
            NonTerminal.mulop,
            NonTerminal.factor,
        )
    ),
    BNF(
        NonTerminal.term,
        (
            NonTerminal.factor,
        )
    ),
    BNF(
        NonTerminal.mulop,
        (
            TokenType.TIMES,
        )
    ),
    BNF(
        NonTerminal.mulop,
        (
            TokenType.OVER,
        )
    ),
    BNF(
        NonTerminal.factor,
        (
            TokenType.LPAREN,
            NonTerminal.expression,
            TokenType.RPAREN,
        )
    ),
    BNF(
        NonTerminal.factor,
        (
            NonTerminal.var,
        )
    ),
    BNF(
        NonTerminal.factor,
        (
            NonTerminal.call,
        )
    ),
    BNF(
        NonTerminal.factor,
        (
            TokenType.NUM,
        )
    ),
    BNF(
        NonTerminal.call,
        (
            TokenType.ID,
            TokenType.LPAREN,
            NonTerminal.args,
            TokenType.RPAREN,
        )
    ),
    BNF(
        NonTerminal.args,
        (
            NonTerminal.arg_list,
        )
    ),
    BNF(
        NonTerminal.args,
        (
        )
    ),
    BNF(
        NonTerminal.arg_list,
        (
            NonTerminal.arg_list,
            TokenType.COMMA,
            NonTerminal.expression,
        )
    ),
    BNF(
        NonTerminal.arg_list,
        (
            NonTerminal.expression,
        )
    ),
]
