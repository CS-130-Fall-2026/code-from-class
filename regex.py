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

## Regex that matches all letters, spaces, numbers, and periods:
diff_regex = r"([a-z]|[A-Z]| |\.|[0-9])*"
print(re.fullmatch(diff_regex, address))
print(re.fullmatch(diff_regex, "class"))

print(re.fullmatch(regex, "123-456-7890 other text"))

## Does the above regex match phone?
print("Does diff_regex match phone?", re.fullmatch(diff_regex, phone))

print("\n ---- New regex ---")

new_regex = r"\d*-\d*-\d*"
print("new regex who dis:", re.fullmatch(new_regex, phone))

ssn = "123-23-4567"
two_dashes = "--"

print("ssn:", re.fullmatch(new_regex, ssn))
print("two dashes:", re.fullmatch(new_regex, two_dashes))

regex_phone = r"\d\d\d-\d\d\d-\d\d\d\d"
regex_phone = r"\d{3}-\d{3}-\d{4}"

print("\n ----- Only match phone numbers -----")
print("phone:", re.fullmatch(regex_phone, phone))
print("ssn:", re.fullmatch(regex_phone, ssn))
print("two dashes:", re.fullmatch(regex_phone, two_dashes))


## r before strings => raw string
## raw strings do not escape any characters
## Therefore, r"\n" is just the characters \ and n, not a newline
print("\n ----- Raw strings")
print(r"hi\nhi")
print("hi\nhi")
print(regex_phone)

print("\n ---- List filtering")
numbers = ["134-524-6575", "01-12-21", "233-457-1213", "12312412321-1234123124-12312312",
           "--", "hello world", "413-555-6667", "John"]

phone_numbers = [x for x in numbers if re.fullmatch(regex_phone, x) != None]
print(phone_numbers)

print("\n ----- Find first occurrence")
## We have a long text, and want to find the first phone number:
text = """Call Jerry at 123-456-1234 or Samantha at 555-555-5555(home)
or 123-456-6788ext1234(work). We need more text here to make it interesting."""

## re.search finds the first match in the text and returns a Match object
ph = re.search(regex_phone, text)
print("The matched string:", ph.group())
print("The start index of the match:", ph.start())
print("The end index of the match:", ph.end())

print(re.search(new_regex, text))

print("\n ------- find all")

## What if we want all of the phone numbers in the string?
list_of_phones = re.findall(regex_phone, text)
print("All phone numbers:", list_of_phones)


list_of_phones = re.findall(new_regex, text)
print("All phone numbers again?:", list_of_phones)

nums_and_dashes = "123-55-66666-77-8888-999-123456-12345677"
print("Not Overlapping!", re.findall(new_regex, nums_and_dashes))

print("\n------ With extension")

## ? at end means: match previous thing or empty string
## If you want to use parentheses for expression grouping,
## you need to put ?: right at the start, otherwise
## they're treated as a "capture group"

regex_ext = r"\d{3}-\d{3}-\d{4}(?:ext\d*)?"
print("phones with extensions:", re.findall(regex_ext, text))

print("\n ---- From lab")

target = "ham"
# regex_target = "h.*a.*m"

regex_target = ""
for c in target:
    regex_target += c + r".*"

regex_target = regex_target[:-2]

print(re.search(regex_target, text))