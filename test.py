grammar = open("/workspaces/beautiful-py/beautifulpy/grammars/javascriptECMA.lark","r")
txt_file = open("test.txt","w")
import re
text = grammar.read()
test = ""
print(re.search("\"{\"",text))
matches = re.finditer("{",text)

match_indexes = [(m.start(0), m.end(0)) for m in re.finditer("{",text)]
quoted_match_indexes = [(m.start(0), m.end(0)) for m in re.finditer("\"{\"",text)]
print(quoted_match_indexes)
for match in match_indexes:
    print(match)