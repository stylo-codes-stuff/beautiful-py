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

import parsers
import rich
from lark import Visitor, Transformer,Token

python_requirements = []
import_trees = []
supported_languages = ["python","javascript"]
class get_import_statements(Visitor):
    def import_stmt(self, tree):
        assert tree.data == "import_stmt"
        import_trees.append(tree.children[0])
class get_imports(Visitor):
    def name(self,tree):
        assert tree.data == "name"
        python_requirements.append(tree.children[0])
"""returns a list of imports for the given file."""
def get_requirements(file,language):
    python_requirements.clear()
    import_trees.clear()

    with open(file,"r") as file:
        tree = parsers.python.parse(file.read())
        get_import_statements().visit(tree)
        for tree in import_trees:
            get_imports().visit(tree)
        for token in python_requirements:
            print(token.value)
            python_requirements[python_requirements.index(token)] = token.value
    return python_requirements
def parse(file, language):
    if language not in supported_languages:
        raise Exception("unsupported language")
