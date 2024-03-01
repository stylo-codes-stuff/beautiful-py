from lark import Token, Lark

from lark.indenter import PythonIndenter
import rich
# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],parser='lalr', postlex=PythonIndenter(), start='file_input',maybe_placeholders=False)
javascript = Lark.open("beautifulpy/grammars/javascript.lark",start="file_input")

with open("tests/python_test.py","r") as file:
    rich.print(python.parse(file.read()))