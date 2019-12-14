import community
import networkx as nx
import matplotlib.pyplot as plt



Graph = nx.karate_club_graph()

# Compute the partition of the graph nodes which maximises the modularity (or try..) using the Louvain heuristices
partition = community.best_partition(Graph)

# Plot, color nodes using community structure


values = [partition.get(node) for node in Graph.nodes()]
nx.draw_spring(Graph, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show()

#compute modularity of graph

mod = community.modularity(partition,Graph)

# try to change the modularity
dendrogram = community.generate_dendrogram(Graph)

partitions = community.partition_at_level(dendrogram, len(dendrogram)-1 )

values = [partitions.get(node) for node in Graph.nodes()]
nx.draw_spring(Graph, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show()

mod = community.modularity(partitions,Graph)


