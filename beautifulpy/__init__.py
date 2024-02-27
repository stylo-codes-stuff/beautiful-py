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




 
 
from parsers import python_tokenizer
import re
import rich
def get_indent_level(line):
    count = re.findall(r'\s', line)
    return len(count)
    for line in test:
        print(get_indent_level(line))
#prints asts for the given file. When pretty is true it uses rich to print the asts.
def tree(file,pretty = False):
    with open(file,"r") as file:
        if pretty == True:
            for line in file:
                line = python_tokenizer.parse(line)
                rich.print(line)
        if pretty == False:
            for line in file:
                line = tokenizer.parse(line)
                print(line)

def if_statement(file,parser):
    with open(file,"r") as file:
        for line in file:
            line = python_tokenizer.parse(line)
    
tree("../samples.py",pretty= True)