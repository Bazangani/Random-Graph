import numpy as np
from random import choice
import random
import sys


# 1. Generate large graph
G=nx.barabasi_albert_graph(10000,3,seed=None)
# number of nodes eguals to 10000


# assign values to each nodes (weight of the nodes)
values= np.random.uniform(-1,0,10000)

#1. choose a random node (initialization)
init_node=choice(list(G.nodes))

degree=G.degree()


# init values 
number_of_walk=100
sum_node=values[init_node]
node=init_node


for i in range (number_of_walk): 
    
    nei=list(G.neighbors(node))

  
    node=random.choice(nei)
    sum_node=sum_node+values[node]
    
avg=sum_node/number_of_walk   
    
    
print("estimated avg of the wights: ",avg) 

print("the avg wights of graph: ",np.mean(values))


