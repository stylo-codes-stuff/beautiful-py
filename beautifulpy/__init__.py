import parsers
import re
test = open("../samples.py","r")
def get_indent_level(line):
    count = re.findall(r'\s', line)
    return len(count)
for line in test:
    print(get_indent_level(line))