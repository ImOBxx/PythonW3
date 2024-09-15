import re

# String to be checked
string1 = "ABCDEFabcdef123450"
string2 = "*&%@#!}{"

# Compile a regular expression to match any character that is not a-z, A-Z, or 0-9
charRe = re.compile(r'[^a-zA-Z0-9]')

# Search the string for disallowed characters
result1 = not bool(charRe.search(string1))
result2 = not bool(charRe.search(string2))

# Print results
print(result1)  # Expected: True
print(result2)  # Expected: False
