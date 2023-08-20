from typing import List

class trie_node:
    def __init__(self, data, children = None, is_end = False, is_root = False):
        self.data = data
        self.children = []
        self.is_end = is_end
        self.is_root = is_root
    
    def create_node(self, data: List):
        # print(data)
        for child in self.children:
            if child.data == data[0]:
                child.create_node(data[1:])
                return
        if len(data) == 1: 
            new_node = trie_node(data[0], is_end = True)
            self.children.append(new_node)
            return
        else:
            new_node = trie_node(data[0], is_end = True)
            self.children.append(new_node)
            new_node.create_node(data[1:])
            return 
        
class trie:
    def __init__(self):
        self.root = trie_node(None, is_root = True)
    
    def add_data(self, data):
        self.root.create_node(data)

    def display(self):
        queue = []
        queue.append((self.root, 0))
        line = ""
        prev_level = 0
        while queue:
            curr_trie_node, level = queue.pop(0)
            if level > prev_level:
                print(line)
                line = ""
            for child in curr_trie_node.children:
                line += child.data
                queue.append((child, level + 1))
            prev_level = level
        return


# def main():
#     print("HELLO")
#     test_trie = trie()
#     test_trie.add_data("hello")
#     return

# main()
    
