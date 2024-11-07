GRAPH = {
    'City A': {'City B': 30, 'City C': 20, 'City D': 25},
    'City B': {'City A': 30, 'City E': 40, 'City F': 30, 'City G': 10},
    'City C': {'City A': 20, 'City E': 30},
    'City E': {'City B': 40, 'City C': 30},
    'City D': {'City A': 25, 'City F': 40},
    'City F': {'City B': 30, 'City D': 40, 'City G': 35},
    'City G': {'City B': 10, 'City F': 35}
}

straight_line = {
    'City A': 100,
    'City B': 10,
    'City C': 30,
    'City D': 40,
    'City E': 60,
    'City F': 35,
    'City G': 0  
}

from queue import PriorityQueue

def best_first_search(start, goal):
    queue = PriorityQueue()
    queue.put((straight_line[start], 0, start, [start]))
    visited = set()

    while not queue.empty():
        heuristic, cost, city, path = queue.get()
        
        if city == goal:
            return cost, path
        
        if city not in visited:
            visited.add(city)
            for neighbor, travel_cost in GRAPH[city].items():
                if neighbor not in visited:
                    queue.put((straight_line[neighbor], cost + travel_cost, neighbor, path + [neighbor]))

    return None, []  # Return None if no path is found

def main():
    start = input('Enter Starting city: ').strip()
    goal = input('Enter Destination city: ').strip()

    if start not in GRAPH or goal not in GRAPH:
        print('City does not exist or not found.')
    else:
        print('\nBest First Search Path:')
        cost, path = best_first_search(start, goal)
        if path:
            print('Path Cost =', cost)
            print(' -> '.join(path))
        else:
            print('No path found.')

if __name__ == '__main__':
    main()
