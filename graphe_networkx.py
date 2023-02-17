import networkx as nx
import matplotlib.pyplot as plt

# Define the MDP as a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node('A', label='State A')
G.add_node('B', label='State B')
G.add_node('C', label='State C')
G.add_node('D', label='State D')
G.add_node('E', label='State E')

# Add edges to the graph
G.add_edge('A', 'B', label='Action 1', weight=0.3)
G.add_edge('A', 'C', label='Action 2', weight=0.7)
G.add_edge('B', 'D', label='Action 1', weight=1.0)
G.add_edge('C', 'E', label='Action 2', weight=0.5)
G.add_edge('C', 'D', label='Action 1', weight=0.5)

# Set node positions for visualization
pos = nx.spring_layout(G)

# Draw the graph
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, nx.get_node_attributes(G, 'label'))
nx.draw_networkx_edges(G, pos, width=2)

edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()

