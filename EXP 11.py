# Grammar:
# S -> aSb | ab

def parse_S(s):
    if s == "ab":
        return True
    if len(s) > 2 and s[0] == 'a' and s[-1] == 'b':
        return parse_S(s[1:-1])
    return False

# Test
string = "aaabbb"
print("Accepted" if parse_S(string) else "Rejected")