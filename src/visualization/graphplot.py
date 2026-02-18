import matplotlib.pyplot as plt

def plot_campus_graph(graph, node_positions, path=None):
    fig, ax = plt.subplots(figsize=(7, 5))

    for node, neighbors in graph.items():
        x1, y1 = node_positions[node]
        for neighbor, _ in neighbors:
            x2, y2 = node_positions[neighbor]
            ax.plot([x1, x2], [y1, y2], color="gray", linewidth=0.8, alpha=0.6)

    for node, (x, y) in node_positions.items():
        ax.scatter(x, y, color="lightgreen", s=120, edgecolors="black", zorder=3)
        ax.text(x, y, str(node), fontsize=8, ha="center", va="center", zorder=4)

    if path:
        for i in range(len(path) - 1):
            x1, y1 = node_positions[path[i]]
            x2, y2 = node_positions[path[i + 1]]
            ax.plot([x1, x2], [y1, y2], color="red", linewidth=2, zorder=5)

    ax.set_title("LNCT Campus Navigation Graph", fontsize=14)
    ax.axis("off")
    return fig