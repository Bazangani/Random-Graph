#( Metropolice Hasting method)

# walk through the network randomly
import random
import sys
number_of_walk=100
sum_node=values[init_node]

node=init_node
nei=[]

for i in range (number_of_walk): 
    
    nei=list(G.neighbors(node))
    degree=G.degree(nei)
    
    p=[]
    max_list=[]
    

    
    for neibour in nei:
        
        # prob of moving to other nodes
        prob_each_nei=1/(max(degree[node],degree[neibour]))        
        p.append(prob_each_nei)
        
        # stay at same place
        deg_node=G.degree(node)
        max_degree=max(deg_node,degree(neibour))
        max_list.append(max_degree)
        
    a=1
    max_list_new=[a/d for d in max_list]
    
    
    
    max_list_sum=0
    for element in max_list_new:
        max_list_sum=max_list_sum+element

    p_stay= 1- max_list_sum
    nei.append(node)
    p.append(p_stay)
    
        
    random_node=random.choices(nei,p)
    if random_node[0] != node:
        node=random_node[0]
    
        
    sum_node=sum_node+values[node]
    
avg=sum_node/number_of_walk   
    
    
print(avg) 