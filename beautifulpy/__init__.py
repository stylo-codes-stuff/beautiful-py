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




 
 
from parsers import tokenizer
import re
import rich
def get_indent_level(line):
    count = re.findall(r'\s', line)
    return len(count)
    for line in test:
        print(get_indent_level(line))
def tree(file,pretty = False):
    with open(file,"r") as file:
        if pretty == True:
            for line in file:
                line = tokenizer.parse(line)
                print(line)
        if pretty == False:
            for line in file:
                print(tokenizer.parse(line))
def parse(element):
    pass
tree("../samples.py",pretty=True)
