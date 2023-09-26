def tsp_nearest_neighbor(dist):
    n = len(dist)

    for row in dist:
        if len(row) != n:
            raise ValueError("행렬은 n x n 이어야 합니다.")
    
    visited = [False] * n
    tour = [0]  # Start from city 0
    visited[0] = True
    total_distance = 0
    
    for _ in range(n - 1):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None
        
        for i in range(n):
            if not visited[i] and dist[current_city][i] < min_distance:
                min_distance = dist[current_city][i]
                nearest_city = i
        
        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance
    
    # Return to the starting city
    total_distance += dist[tour[-1]][0]
    tour.append(0)
    
    return total_distance, tour

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance, tour = tsp_nearest_neighbor(distances)
print("Minimum Distance:", min_distance)
print("Tour:", tour)
