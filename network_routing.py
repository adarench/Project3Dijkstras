import heapq

def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    previous_nodes = {node: None for node in graph}
    
    pq = [(0, source)] 

    while pq:
        #pop node with shortest distance 
        current_distance, current_node = heapq.heappop(pq)

        if current_node == target:  # early stop if it finishes 
            break
        #check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # only take the best path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # set new path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[target]


def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    previous_nodes = {node: None for node in graph}
    
    pq = [(0, source)]

    while pq:
        #smallest distance
        current_distance, current_node = min(pq, key=lambda x: x[0])
        pq.remove((current_distance, current_node))

        if current_node == target:  #stop early if we need
            break

        #check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # take best path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                pq.append((distance, neighbor))

    # set new path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[target]
