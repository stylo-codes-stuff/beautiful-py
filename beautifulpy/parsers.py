   #lark grammars for parsing specific types of code
import re
from rich import print
from lark import Lark
from lark import Transformer
from lark import Visitor
#tokenizes a whole line of code for parsing
tokenizer = Lark("""
    %import common (WORD, ESCAPED_STRING,NUMBER,CNAME)
    integer.0: NUMBER
    !comment.3: ("#" WORD+)
    !decorator: "@" WORD "."+ (WORD|method)
    !from_import.2: "from" (WORD|CNAME) "import" (WORD|CNAME ",")+
    !import: "import" WORD
    !keyword: "if" | "elif" | "else" | "and" | "or" | "not"
    !boolean.1: "True" | "False"
    variable: WORD
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
""",start="tree")

#parses a line with a condition (note to self to fix typing for floats since they are parsed as integers instead)
statement = Lark("""
    %import common (WORD,ESCAPED_STRING,NUMBER)
    %import python (comp_op)
    !integer.0: NUMBER
    !string: ESCAPED_STRING
    !operator: comp_op
    !variable: WORD
    !bool.2: "True" | "False"
    !float.2: (NUMBER "." NUMBER)
    !keyword: "if" | "elif" | "else" | "and" | "or" | "not" |
    ?condition: (keyword (bool|variable|string|integer|float)+ operator (bool|variable|string|integer|float))+ ":"
    %ignore " "
    %ignore "\\n"
""", start="condition")

#parses a line with a variable declaration returning the name and type in a lark tree.
# if the line is an object declaration, returns the module/class and the passed parameters
variable = Lark("""
    %import common (WORD,ESCAPED_STRING,NUMBER)
    !name: WORD
    !bool.2: "True" | "False"
    !string: ESCAPED_STRING
    !integer: NUMBER
    class:
    variable: name "=" (string|bool|integer)
    %ignore " "
""",start = "variable")

method = Lark("""
    %import common (WORD,ESCAPED_STRING,NUMBER)
    method: WORD
    start: method
    """)

statement_parser= tokenizer.parse('if "hello" == "goodbye" and world == 1.2 :')
test = open("test.txt","w")
line = tokenizer.parse('if "hello" == "goodbye" and world == 1.2 :')
with open("../samples.py","r") as file:
    for line in file:
        line = tokenizer.parse(line)
        print(line)
        test.write(f"{str(line)}\n")
print(statement_parser)