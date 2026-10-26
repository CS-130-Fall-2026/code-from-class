import re

phone = "204-502-3828"
address = "198 College Hill Rd."

regex = r"[0-9]*-[0-9]*-[0-9]*"

## re.fullmatch tells you whether the given string is in the language
## of the regular expression. If so, it returns a Match object;
## otherwise, it returns None

m = re.fullmatch(regex, phone)
print("Matches phone?", m)
print("Matched string:", m.group())

m2 = re.fullmatch(regex, address)
print("Matches address?", m2)

info = "204-502-3828 is my phone number"
m3 = re.fullmatch(regex, info)
print("Matches address?", m3)

diff_regex = r"([a-z]|[A-Z]| |\.|[0-9])*"
print(re.fullmatch(diff_regex, address))
print(re.fullmatch(diff_regex, "class"))

