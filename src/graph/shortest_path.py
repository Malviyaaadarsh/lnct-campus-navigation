import heapq
import math

def dijkstra_path(graph, source, target):
    """
    Returns the shortest path between source and target.
    """
    distances = {node: math.inf for node in graph}
    previous = {node: None for node in graph}

    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == target:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = target
    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    if path[0] != source:
        raise ValueError("No path found between nodes")

    return path


def dijkstra_path_length(graph, source, target):
    """
    Returns only the shortest distance.
    """
    path = dijkstra_path(graph, source, target)

    total_distance = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i + 1]:
                total_distance += weight
                break

    return total_distance






