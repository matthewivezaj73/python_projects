#Importing libraries.
import networkx
#Importing a function.
from networkx.drawing.nx_agraph import write_dot

# instantiate a network, add some nodes, and connect them
nodes = ["hello","world",1,2,3]
network = networkx.Graph()
#Printing out all of the nodes.
for node in nodes:
    network.add_node(node)
#Adding an edge.
network.add_edge("hello","world")
#Saving the node.
write_dot(network,"network.dot")