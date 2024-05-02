from lark import Lark
import os
import time
from lark.indenter import PythonIndenter
import rich
test = Lark.open("beautifulpy/grammars/test.lark",parser="lalr")

# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],parser='lalr', postlex=PythonIndenter(), start='file_input',maybe_placeholders=False)
#reminder that the keep all tokens param keeps tokens generated from using predifined strings inside of rules such as ones for curly braces and commas
ECMAscript = Lark.open("beautifulpy/grammars/javascriptECMA.lark",start="file_input", parser="lalr",keep_all_tokens=True,debug=True)
html = Lark.open("beautifulpy/grammars/html.lark",start="file_input",parser="lalr")
css = Lark.open("beautifulpy/grammars/css.lark",start="file_input",parser="lalr")
#for filename in os.listdir("/workspaces/beautiful-py/tests/test262-parser-tests/pass"):
#    f = os.path.join("/workspaces/beautiful-py/tests/test262-parser-tests/pass", filename)
#    # checking if it is a file
#    if os.path.isfile(f):
#        with open(f,"r") as file:
#            tokens = ECMAscript.parse(file.read())
#            time.sleep(.2)
#            rich.print(tokens)
