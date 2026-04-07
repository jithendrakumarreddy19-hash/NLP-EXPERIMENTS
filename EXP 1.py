import re

text = "My email is example123@gmail.com"

# pattern for gmail
pattern = r"[a-zA-Z0-9._%+-]+@gmail\.com"

match = re.search(pattern, text)

if match:
    print("Gmail found:", match.group())
else:
    print("No Gmail found")