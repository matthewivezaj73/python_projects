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
#Adding attributes to a node.
network.add_node(1,myattribute="foo")
#Accessing the node.
print(network.nodes[1]["myattribute"])
#Adding an attribute to the edges.
network.add_edge("node1","node2",myattribute="attribute of an edge")
["node2"]["myattribute"] = "attribute of an edge"