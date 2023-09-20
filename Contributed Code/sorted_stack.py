class SortedStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        temp_stack = []
        while self.stack and self.stack[-1] < val:
            temp_stack.append(self.stack.pop())
        self.stack.append(val)
        while temp_stack:
            self.stack.append(temp_stack.pop())
    
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
