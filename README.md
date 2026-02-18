# LNCT Campus Navigation   [Live Link](https://lnct-campus-navigation.onrender.com/)

Interactive campus navigation system built using Graph Theory and Dijkstra’s Algorithm.  
The system models campus locations as a weighted graph and computes the shortest path between checkpoints with visual static map route highlighting.

## Features

- Graph-based modeling of campus locations
- Custom implementation of Dijkstra’s shortest path algorithm using priority queue 
- Adjacency list graph structure
- Interactive source and destination selection
- Visual path rendering using Matplotlib
- Node index reference table
- Web interface built using Gradio
- Deployable web application

## Tech Stack

- Python
- Matplotlib
- Gradio

### Project Structure 

src/
├── data/ # nodes and edges
├── graph/ # graph builder + shortest path algorithm
├── visualization/ # plotting graph 
└── ui/ # gradio web interface
README.md
app.py
requirements.txt
.gitignore

### How It Works

1. Campus checkpoints are modeled as graph nodes.
2. Paths between checkpoints are weighted edges.
3. Dijkstra’s algorithm computes the shortest path.
4. The route is visualized on a plotted campus graph.
5. A node reference table helps users interpret index numbers.
