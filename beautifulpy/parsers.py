from lark import Lark
import os
from lark.indenter import PythonIndenter
import rich
# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],parser='lalr', postlex=PythonIndenter(), start='file_input',maybe_placeholders=False)
ECMAscript = Lark.open("beautifulpy/grammars/javascriptECMA.lark",start="file_input", parser="lalr")
html = Lark.open("beautifulpy/grammars/html.lark",start="file_input",parser="lalr")
css = Lark.open("beautifulpy/grammars/css.lark",start="file_input",parser="lalr")
mini_ECMAscript = Lark.open("beautifulpy/grammars/javascriptECMA_mincode.lark",start="file_input",parser="lalr")
for filename in os.listdir("/workspaces/beautiful-py/tests/test262-parser-tests/pass"):
    f = os.path.join("/workspaces/beautiful-py/tests/test262-parser-tests/pass", filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f,"r") as file:
            print(file)
            rich.print(ECMAscript.parse(file.read()))

