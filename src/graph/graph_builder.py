def build_adjacency_list(edges):
    adjacency_list = {}       

    for source, destination, distance in edges:
        if source not in adjacency_list:
            adjacency_list[source] = []
        if destination not in adjacency_list:
            adjacency_list[destination] = []
        adjacency_list[source].append((destination, distance))
        adjacency_list[destination].append((source, distance))
    return adjacency_list
    
if __name__ == "__main__":
    from src.data.edges import edges
    graph = build_adjacency_list(edges)
    for node, neighbors in graph.items():
        print(node, "->", neighbors)


 