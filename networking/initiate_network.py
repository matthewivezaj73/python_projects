#Importing a library.
import networkx
#Initiating a network with no node and no edges.
network = networkx.Graph()
#Creating a list.
nodes = ["hello", "world", 1, 2, 3]
#Adding the nodes.
for node in nodes:
    network.add_node(node)
#Adding edges.
network.add_edge("hello", "world")
network.add_edge(1,2)
network.add_edge(1,3)