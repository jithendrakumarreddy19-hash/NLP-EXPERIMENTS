class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def parse_tree(s):
    if s == "ab":
        root = Node("S")
        root.children = [Node("a"), Node("b")]
        return root

    if s[0] == 'a' and s[-1] == 'b':
        root = Node("S")
        root.children = [Node("a"), parse_tree(s[1:-1]), Node("b")]
        return root

def print_tree(node, level=0):
    print(" " * level + node.value)
    for child in node.children:
        print_tree(child, level+2)

# Test
tree = parse_tree("aaabbb")
print_tree(tree)