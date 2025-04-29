#
#  _______   _    _              _   _   _  __ __     __   ____    _    _        
# |__   __| | |  | |     /\     | \ | | | |/ / \ \   / /  / __ \  | |  | |       
#    | |    | |__| |    /  \    |  \| | | ' /   \ \_/ /  | |  | | | |  | |       
#    | |    |  __  |   / /\ \   | . ` | |  <     \   /   | |  | | | |  | |       
#    | |    | |  | |  / ____ \  | |\  | | . \     | |    | |__| | | |__| |       
#    |_|    |_|  |_| /_/    \_\ |_| \_| |_|\_\    |_|     \____/   \____/                                      
#          ______    ____    _____      _    _    _____   _____   _   _    _____ 
#         |  ____|  / __ \  |  __ \    | |  | |  / ____| |_   _| | \ | |  / ____|
#         | |__    | |  | | | |__) |   | |  | | | (___     | |   |  \| | | |  __ 
#         |  __|   | |  | | |  _  /    | |  | |  \___ \    | |   | . ` | | | |_ |
#         | |      | |__| | | | \ \    | |__| |  ____) |  _| |_  | |\  | | |__| |
#         |_|       \____/  |_|  \_\    \____/  |_____/  |_____| |_| \_|  \_____|
#                                           /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$ /$$$$$$$$ /$$   /$$ /$$      
#                                          | $$__  $$| $$_____/ /$$__  $$| $$  | $$|__  $$__/|_  $$_/| $$_____/| $$  | $$| $$      
#                                          | $$  \ $$| $$      | $$  \ $$| $$  | $$   | $$     | $$  | $$      | $$  | $$| $$      
#                                          | $$$$$$$ | $$$$$   | $$$$$$$$| $$  | $$   | $$     | $$  | $$$$$   | $$  | $$| $$      
#                                          | $$__  $$| $$__/   | $$__  $$| $$  | $$   | $$     | $$  | $$__/   | $$  | $$| $$      
#                                          | $$  \ $$| $$      | $$  | $$| $$  | $$   | $$     | $$  | $$      | $$  | $$| $$      
#                                          | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/   | $$    /$$$$$$| $$      |  $$$$$$/| $$$$$$$$
#                                          |_______/ |________/|__/  |__/ \______/    |__/   |______/|__/       \______/ |________/
#                                                                                                                                                                                                        
#                                                                                     /$$$$$$$  /$$     /$$              )  /   \  )
#                                                                                    | $$__  $$|  $$   /$$/             (  )    ) (
#                                                                                    | $$  \ $$ \  $$ /$$/              |  |  |  |
#                                                                                    | $$$$$$$/  \  $$$$/               _,..---..,_
#                                                                                    | $$____/    \  $$/            ,-"`    .'.    `"-,
#                                                                                    | $$          | $$            ((      '.'.'      ))
#                                                                                    | $$          | $$             `'-.,_   '   _,.-'`
#                                                                                    |__/          |__/         jgs   `\  `"""""`  /`
#                                                                                                                       `""-----""`
import sys
import parsers
import rich
import pathlib
from lark import Visitor, Transformer,Token

requirements = []
supported_languages = ["python","javascript"]
'''visitor classes for the get_requirements function'''
class get_import_statements(Visitor):
    import_trees = []
    #python tokens
    def import_from(self, tree):
        assert tree.data == "import_from"
        import_trees.append(tree.children[0])
    def import_name(self,tree):
        assert tree.data == "import_name"
        import_trees.append(tree.children[0])
# so this is why we initalized the list before the function was even declared yikes!!!!
#change this immediatley to have its own list
class get_imports(Visitor):
    def name(self,tree):
        assert tree.data == "name"
        requirements.append(tree.children[0])
"""returns a list of imports for the given file."""
def get_requirements(file,language, filter_builtins = False):
    #initalize requirements list variable
    #checks what extension the file should be parsed in and checks the files extension to make sure incorrect parameters weren't set
    if language == "python":
        if pathlib.Path(file).suffix != ".py" :
            raise Exception(f"The file you are trying to parse is of type ${pathlib.Path(file).suffix} not py")
        #opens file and begins parsing using the python grammar
        with open(file,"r") as file:
            #generates an abstract syntax tree and extracts import name tokens using visitors 
            tree = parsers.python.parse(file.read())
            get_import_statements().visit(tree)
            for tree in import_trees:
                get_imports().visit(tree)
            #after name tokens are extracted check if built in libraries need to be filtered and add them to the requirements list 
            for token in requirements:
                if filter_builtins == True:
                    if token.value not in sys.stdlib_module_names:
                        requirements[requirements.index(token)] = token.value
                    if token.value in sys.stdlib_module_names:
                        requirements[requirements.index(token)] = ""
                if filter_builtins == False:
                    python_requirements[requirements.index(token)] = token.value
        return requirements
def parse(file, language):
    if language not in supported_languages:
        raise Exception(f"unsupported language, please use a language from the list below\n{supported_languages}")
    



print(get_requirements("tests/python_test.py","python"))
