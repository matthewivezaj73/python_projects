#Importing a library.
import networkx
from networkx.drawing.nx_agraph import write_dot
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
#Adding attributes to a node.
network.add_node(1,myattribute="foo")
#Accessing the node.
print(network.nodes[1]["myattribute"])
#Adding an attribute to the edges.
network.add_edge("node1","node2",myattribute="attribute of an edge")
#Adding attributes to edges once they've been added.
network.edge["node1"]["node2"]["myattribute"] = "attribute of an edge"
#Using the edge dictionary to access node attributes the other way around.
network.edge["node1"]["node2"]["myattribute"] = 321
print(network.edge["node2"]["node1"]["myattribute"])
#Specifying the network we want to save.
network.add_edge("hello", "world")