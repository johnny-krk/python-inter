#data = input('podaj mail:')
#print(data)

import re
#można tez
#from typing import Match

text = """The car was moving across the street.
Maybe, the traffic was heavy?!"""
print("Ala \n ma kota")
#ale można raw string zrobić:
print(r"Ala \n ma kota")

#pattern: str = r"The"
pattern: str = r"the"
print(dir(re))

result: re.Match = re.search(pattern, text)
print(result)
print(result.span())
print(result.start())
print(result.end())
print(text[result.start():result.end()])
print(result.group())


for found_match in re.finditer(pattern, text):
    print(found_match.span())



