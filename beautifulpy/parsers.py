   #lark grammars for parsing specific types of code
import re
from rich import print
from lark import Lark,Visitor, Transformer, v_args
from lark.lexer import Lexer, Token
#python tokenizer,lexer and visitor
class pythonVisitor(Visitor):
    def check(self,tree):
        assert tree.data == "variable"
        print(tree.children[0])
class pythonLexer(Lexer):
    def __init__(self,lexer_conf):
        pass
    def lex(self, data):
        for obj in data:
            if isinstance(obj,str):
                yield Token("STR",obj)

python_tokenizer = Lark("""
    %import common (WORD, ESCAPED_STRING,NUMBER,CNAME)
    integer.0: NUMBER
    !comment.3: /#.*/
    !decorator: "@" WORD "."+ (WORD|method)
    !from_import.2: "from" (WORD|CNAME) "import" (WORD|CNAME ",")+
    !import: "import" WORD
    !keyword: "if" | "elif" | "else" | "and" | "or" | "not"
    !boolean.1: "True" | "False"
    variable: WORD "=" 
    !for_loop.1: "for" WORD "in" (method|variable) ":"
    !conditional_statement.1: (keyword (boolean|variable|string|integer)+ comparitive_operator (boolean|variable|string|integer))* ":"+
    !function_def.1: "def" (WORD|CNAME) "(" (WORD|CNAME)* ")" ":" 
    !comparitive_operator: "==" | "!=" | ">" | "<" | ">=" | "<="
    operator: "+" | "-" | "*" | "/" | "%" | "**"
    string: ESCAPED_STRING
    list: WORD|CNAME "=" "[" (string|boolean|integer|WORD|CNAME)* "]"
    !method: ((WORD|CNAME)|".")*  "("+ (string|boolean|integer|WORD|CNAME|"."|","|"("|")")* ")"+
    tree: branch
    branch: (variable|keyword|boolean|string|integer|operator|comparitive_operator|comment|function_def|method|list|conditional_statement|for_loop|import|from_import|decorator)* ":"*
    %ignore " "
    %ignore "\\n"
""",start="tree",lexer = pythonLexer)

#parses a line with a condition (note to self to fix typing for floats since they are parsed as integers instead)

#wip javascript parser
#javascript_parser = Lark("""
#            %import (WORD, ESCAPED_STRING,NUMBER,CNAME)
#            variable: ("let"|"var"|"const") WORD "="
#            start:variable
#""")
with open("../samples.py","r") as file:
    for line in file:
        pythonVisitor().visit(python_tokenizer.parse(line))
text = """
let variable = 1;
var variable2 = 3;

function add(){
console.log(variable1+variable2)
}

"""
