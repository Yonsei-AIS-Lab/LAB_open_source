class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1

    def search(self, word):
        if not word:
            return False
        
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        if not prefix:
            return False
            
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix):
        if not prefix:
            return []
        
        def dfs(node, path):
            suggestions = []
            if node.is_end_of_word:
                suggestions.append(path)
            
            for char, child_node in node.children.items():
                suggestions.extend(dfs(child_node, path + char))
            
            return suggestions

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        suggestions = dfs(node, prefix)
        suggestions.sort(key=lambda x: (-self.get_frequency(x), x))
        return suggestions[:3]

    def get_frequency(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        return node.frequency

# Example usage:
if __name__ == "__main__":
    select = 1
    trie = Trie()
    trie.insert("apple")
    trie.insert("appetizer")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")
    trie.insert("ball")
    trie.insert("batman")

    while(select != 0):
        print("~~~~~~~~~~~~~~~~~~")
        print("Choose an action.")
        print("1. Insert")
        print("2. Search")
        print("3. Starts with")
        print("4. Autocomplete")
        print("0. Stop")
        select = int(input("Selection: "))
        if (select == 1):
            insert = input("Insert a string into the trie: ")
            while(insert != ''):
                trie.insert(insert)
                insert = input("Insert a string into the trie: ")
                print("(Press enter to stop inserting.)")
        elif (select == 2):
            search = input("Search from the trie: ")
            if (trie.search(search)):
                print("The word is in the trie")
            else:
                print("The word is not in the tree")
        elif (select == 3):
            startsWith = input("Search if there is a word that starts with: ")
            if (trie.startsWith(startsWith)):
                print("Yes, there is!")
            else:
                print("Nothing starts with", startsWith)
        elif (select == 4):
            autoComplete = input("Autocomplete: ")
            print(trie.autocomplete(autoComplete))
        elif (select == 0):
            break
        else:
            print("Invalid input.")