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

def bestfirst(start, goal):
   
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[start], 0, start, [start]))
    visited[start] = straight_line[start]
    
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
       
        if vertex == goal:
            return heuristic, cost, path
        
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = straight_line[next_node]
            if next_node not in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))

def main():
    print('Enter Starting city:',end = ' ')
    source_node = input().strip()
    print('Enter Destination city:',end = ' ')
    dest_node = input().strip()
    
    if source_node not in GRAPH or dest_node not in GRAPH:
        print('City does not exist or not found.')
    else:
        print('\nBest First Search Path: ')
        heuristic, cost, optimal_path = bestfirst(source_node,dest_node)
        print('Path Cost =', cost)
        print(' -> '.join(city for city in optimal_path))

if __name__ == '__main__':
    main()
