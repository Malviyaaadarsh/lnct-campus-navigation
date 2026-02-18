from src.data import node_mapping, reverse_mapping, edges, node_positions
from src.graph import build_adjacency_list, dijkstra_path, dijkstra_path_length

graph = build_adjacency_list(edges)

def get_shortest_route(source_name, destination_name):
    if source_name not in reverse_mapping or destination_name not in reverse_mapping:
        raise ValueError("Invalid checkpoint selected")

    source = reverse_mapping[source_name]
    destination = reverse_mapping[destination_name]

    path = dijkstra_path(graph, source, destination)
    distance = dijkstra_path_length(graph, source, destination)

    path_names = [node_mapping[node] for node in path]

    return {
        "path_ids": path,
        "path_names": path_names,
        "distance": distance
    }


if __name__ == "__main__":
    result = get_shortest_route("LNCT Main Gate", "Central Library")
    print(result)





