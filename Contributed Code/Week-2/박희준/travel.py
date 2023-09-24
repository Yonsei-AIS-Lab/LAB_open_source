def tsp_nearest_neighbor(dist):
    num_cities = len(dist) # change n -> num_cities
    visited = [False] * num_cities
    tour = [0]  # Start from city 0
    visited[0] = True
    total_distance = 0
    
    for _ in range(num_cities - 1):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None
        
        for candidate_city in range(num_cities): # change i -> candidate_city
            if not visited[candidate_city] and dist[current_city][candidate_city] < min_distance:
                min_distance = dist[current_city][candidate_city]
                nearest_city = candidate_city
        
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
