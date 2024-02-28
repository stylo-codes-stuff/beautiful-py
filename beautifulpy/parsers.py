from lark import Token, Lark
from lark.reconstruct import Reconstructor
from lark.indenter import PythonIndenter
import rich

# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],
                                        parser='earley', postlex=PythonIndenter(), start='file_input',
                                        maybe_placeholders=False    # Necessary for reconstructor
                                        )

SPACE_AFTER = set(',+-*/~@<>="|:')
SPACE_BEFORE = (SPACE_AFTER - set(',:')) | set('\'')
                       
#wip javascript parser
#javascript_parser = Lark("""
#            %import (WORD, ESCAPED_STRING,NUMBER,CNAME)
#            variable: ("let"|"var"|"const") WORD "="
#            start:variable
#""")
with open("./samples.py","r") as file:
        rich.print(python.parse(file.read()))
text = """
let variable = 1;
var variable2 = 3;

function add(){
console.log(variable1+variable2)
}

"""
