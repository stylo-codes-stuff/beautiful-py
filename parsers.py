
from rich import print
from lark import Lark
from lark import Transformer
statement = Lark("""
    %import common (WORD,ESCAPED_STRING,NUMBER)
    %import python (comp_op)
    !string: ESCAPED_STRING
    !operator: comp_op
    !variable: WORD
    !bool.2: "True" | "False"
    !keyword: "if" | "elif" | "else" | "and" | "or" | "not"
    ?condition: (keyword (bool|variable|string|NUMBER)+ operator (bool|variable|string|NUMBER))+ ":"
    %ignore " "
    %ignore "\\n"
""", start="condition")
variable = Lark("""
    %import common (WORD,ESCAPED_STRING,NUMBER)
    !name: WORD
    !bool.2: "True" | "False"
    !string: ESCAPED_STRING
    !integer: NUMBER
    variable: name "=" (string|bool|integer)
    %ignore " "
""",start = "variable")
# Tree('start', [Token('NAME', 'hello')])
statement_parser= statement.parse('if "hello" == True and world == False :')
variable_parser = variable.parse('hello = "world"')
print(statement_parser)
print(variable_parser)
