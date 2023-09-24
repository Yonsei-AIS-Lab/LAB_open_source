class TrieNode:
    def __init__(self):
        self.children = {}  # 현재 노드에서 가능한 다음 문자들을 저장
        self.is_end_of_word = False  # 이 노드가 단어의 끝인지를 나타냄
        self.frequency = 0  # 해당 단어의 출현 빈도
class Trie:
    def __init__(self):
        self.root = TrieNode() # root 노드 생성

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
        
        def dfs(node, path):# 깊이 우선 탐색으로 가능한 모든 단어를 찾아내는 함수
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
        suggestions.sort(key=lambda x: (-self.get_frequency(x), x)) # 출현 빈도와 알파벳 순으로 정렬
        return suggestions[:3] # 상위 세 개의 추천 단어 반환

    def get_frequency(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        return node.frequency


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
