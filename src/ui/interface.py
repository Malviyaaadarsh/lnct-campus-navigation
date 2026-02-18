import gradio as gr

from src.data.nodes import node_mapping, node_positions, reverse_mapping
from src.data.edges import edges
from src.graph.graph_builder import build_adjacency_list
from src.graph.shortest_path import dijkstra_path, dijkstra_path_length
from src.visualization.graphplot import plot_campus_graph

GRAPH = build_adjacency_list(edges)
NODE_NAMES = list(node_mapping.values())

def find_shortest_path(source_name, destination_name):
    if source_name == destination_name:
        return None, "Source and destination are the same."

    source = reverse_mapping[source_name]
    destination = reverse_mapping[destination_name]

    try:
        path = dijkstra_path(GRAPH, source, destination)
        distance = dijkstra_path_length(GRAPH, source, destination)

        fig = plot_campus_graph(
            GRAPH,
            node_positions,
            path=path,
        )

        path_names = " → ".join(node_mapping[n] for n in path)

        text_output = (
            f"Shortest Distance: {distance} meters Approximately\n\n"
            f"Path:\n{path_names}"
        )

        return fig, text_output

    except Exception as ex:
        return None, str(ex)

with gr.Blocks(title="LNCT Campus Navigation") as app:
    gr.Markdown("## LNCT Campus Navigation ")
    gr.Markdown('Select a source and destination to find the shortest path across the LNCT campus. The map will display the route, and the text box will provide distance and path details.')
    with gr.Row():
        source = gr.Dropdown(
            choices=NODE_NAMES,
            label="Source"
        )
        destination = gr.Dropdown(
            choices=NODE_NAMES,
            label="Destination"
        )
    find_btn = gr.Button("Find Shortest Path")

    graph_output = gr.Plot(label="Campus Map")
    text_output = gr.Textbox(label="Route Information", lines=6)

    find_btn.click(
        fn=find_shortest_path,
        inputs=[source, destination],
        outputs=[graph_output, text_output]
    )
    
    gr.Markdown("### Location Index Reference")
    gr.Markdown("Refer to the following table for node indices and their corresponding locations:")
    for i in range(0, len(NODE_NAMES), 5):
        table_data = []
        for j in range(5):
            idx = i + j
            if idx < len(NODE_NAMES):
                table_data.append(f"{idx+1}: {NODE_NAMES[idx]}")
            else:
                table_data.append("")
        gr.Markdown("  |  ".join(table_data))
