class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드를 저장하기 위한 딕셔너리
        self.is_end_of_word = False # 단어의 끝인지 여부를 나타내는 플래그
        self.frequency = 0  # 해당 단어의 등장 빈도수를 저장하는 변수

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 루트 노드 생성

    def insert(self, word):
        if not word:
            return
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()    # 문자가 없다면 새로운 노드 생성 진행
            node = node.children[char]  # 다음 노드로 이동
        node.is_end_of_word = True  # 단어의 끝 표시
        node.frequency += 1     # 단어의 빈도수 증가, 같은 단어가 여러 번 들어오면 빈도수는 계속해서 증가

    def search(self, word):
        if not word:
            return False
        
        node = self.root
        for char in word:
            if char not in node.children:
                return False    # 문자가 없으면 검색 실패
            node = node.children[char]
        return node.is_end_of_word  # 단어의 끝인지 여부 반환 / 단어의 끝이라면 True 반환

    def startsWith(self, prefix):
        if not prefix:
            return False
            
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False    # 접두어가 없으면 검색 실패
            node = node.children[char]
        return True # 접두어가 존재함

    def autocomplete(self, prefix):
        if not prefix:
            return []
        
        def dfs(node, path):
            suggestions = []
            if node.is_end_of_word:
                suggestions.append(path)    # 단어의 끝에 도달하면 현재 경로를 제안 리스트에 추가
            
            for char, child_node in node.children.items():
                suggestions.extend(dfs(child_node, path + char))    # 모든 자식 노드에 대해 DFS 알고리즘 실행
            
            return suggestions

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []   # 주어진 접두어가 Trie에 존재하지 않으면 빈 리스트 반환

            node = node.children[char]

        suggestions = dfs(node, prefix) # 접두어의 마지막 노드부터 DFS 시작
        suggestions.sort(key=lambda x: (-self.get_frequency(x), x)) # 빈도수를 기준으로 내림차순 정렬
        return suggestions[:3]  # 상위 3개의 자동완성 제안 반환

    def get_frequency(self, word):  # 해당 문자가 Trie에서 얼마나 자주 나타내는지 확인하는 용도 / Trie는 중복 단어를 처리하는 데 효과적이며 단어의 등장 빈도수를 확인할 수 있다.
        node = self.root
        for char in word:
            node = node.children[char]
        return node.frequency   # 주어진 단어의 빈도수 반환

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

    print("Search 'app':", trie.search("app"))  # app이 Trie에 존재하는지 확인
    print("Starts with 'app':", trie.startsWith("app")) # app으로 시작하는 단어가 Trie에 존재하는지 확인

    print("Autocomplete suggestions for 'app':", trie.autocomplete("app"))  # app을 포함하는 자동완성 제안 결과 출력
