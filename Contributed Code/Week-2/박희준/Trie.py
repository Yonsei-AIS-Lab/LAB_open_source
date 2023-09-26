class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False # is_end_of_work 변수는 단어가 끝나는지 나타내기 위해 사용되는 변수
        self.frequency = 0 # frequency 변수는 Trie에서 단어의 빈도를 세기 위한 변수

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        
        node = self.root
        # Trie에 단어를 삽입하는 함수
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # 마지막 노드인 것을 표시하고 frequency를 증가하기
        node.is_end_of_word = True
        node.frequency += 1

    def search(self, word):
        if not word:
            return False
        
        node = self.root
        # Trie에서 단어를 찾는 함수
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        if not prefix:
            return False
            
        node = self.root
        # Trie가 prefix로 시작하는지 확인하는 함수
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
    trie = Trie()
    trie.insert("apple")
    trie.insert("appetizer")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")
    trie.insert("ball")
    trie.insert("batman")

    print("Search 'app':", trie.search("app"))
    print("Starts with 'app':", trie.startsWith("app"))

    print("Autocomplete suggestions for 'app':", trie.autocomplete("app"))
