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

python_requirements = []
javascript_requirements = []
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
class get_imports(Visitor):
    def name(self,tree):
        assert tree.data == "name"
        python_requirements.append(tree.children[0])
"""returns a list of imports for the given file."""
def get_requirements(file,language, filter_builtins = False):
    if language == "python":
        if pathlib.Path(file).suffix != ".py" :
            raise Exception(f"The file you are trying to parse is of type ${pathlib.Path(file).suffix} not py")
        python_requirements.clear()
        import_trees.clear()
        with open(file,"r") as file:
            tree = parsers.python.parse(file.read())
            get_import_statements().visit(tree)
            for tree in import_trees:
                get_imports().visit(tree)
            for token in python_requirements:
                if filter_builtins == True:
                    if token.value not in sys.stdlib_module_names:
                        print("yes")
                        python_requirements[python_requirements.index(token)] = token.value
                    if token.value in sys.stdlib_module_names:
                        python_requirements[python_requirements.index(token)] = ""
                if filter_builtins == False:
                    python_requirements[python_requirements.index(token)] = token.value
        return python_requirements
def parse(file, language):
    if language not in supported_languages:
        raise Exception(f"unsupported language, please use a language from the list below\n{supported_languages}")
    



print(get_requirements("tests/python_test.py","python"))