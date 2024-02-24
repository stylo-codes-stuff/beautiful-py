from lark import Lark
parser = Lark("""
start:    ("\n"|word)*
word:     (PRE1|PRE2) SUFFIX? "\n"

PRE1:     /FQ(?!NNOM)/
PRE2:     /FQN(?!O)/
SUFFIX:   "NOM"
""")

parser.parse("FQNOM")