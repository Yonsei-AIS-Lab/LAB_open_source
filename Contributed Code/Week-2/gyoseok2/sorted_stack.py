import bisect
class SortedStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        #코드 단순화 및 시간 복잡도 개선
        bisect.insort(self.stack, val, key=lambda x: -x)
    
    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()
    
    def display(self):
        print(self.stack)

# Example usage:
if __name__ == "__main__":
    sorted_stack = SortedStack()
    sorted_stack.push(5)
    sorted_stack.push(10)
    sorted_stack.push(2)
    sorted_stack.push(8)
    sorted_stack.push(1)
    
    print("Original Stack:")
    sorted_stack.display()
    
    print("Pop smallest element:", sorted_stack.pop())
    
    print("After popping smallest element:")
    sorted_stack.display()
