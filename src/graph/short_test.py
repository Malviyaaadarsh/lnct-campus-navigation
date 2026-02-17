# Testing the shortest path functionality using Dijkstra's algorithm
from src.data.nodes import node_mapping, reverse_mapping
from src.graph.graph_builder import build_adjacency_list
from src.data.edges import edges
from src.graph.shortest_path import dijkstra_path, dijkstra_path_length

graph = build_adjacency_list(edges)

source = "LNCT Main Gate"
destination = "Central Library"

start = reverse_mapping[source]
end = reverse_mapping[destination]

path = dijkstra_path(graph, start, end)
distance = dijkstra_path_length(graph, start, end)

path_names = [node_mapping[node] for node in path]

print(f"Shortest path from {source} to {destination}:")
print(" -> ".join(path_names))
print(f"Total distance: {distance} meters")
