import heapq

def shortest_path(graph, start, end):
    # Initialize distances dictionary with infinite values
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Initialize priority queue with (distance, node) tuples
    priority_queue = [(0, start)]
    
    # Initialize dictionary to keep track of the previous node in the path
    previous_nodes = {}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes.get(current_node)
            return path[::-1]
        
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return []

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start = 'A'
end = 'D'

result = shortest_path(graph, start, end)
print(result)  # Output: ['A', 'B', 'C', 'D']