def PAM(T): # Preferential Attachment Model
    # input : number of nodes
    degree=np.zeros(T)
    nodes=np.arange(0,T)
    adjency=np.zeros((T,T))
    
    for i in range (0,T):
        if i==0:
            degree[i]=2
            adjency[i,i]=2
        else:
            
            degree[i]=1
            
            
            # compute the probabilty 
            p2_array=degree/(2*T+1)
            
            
            # connect node to the node by choosing a random number based on the probability
            random_node=random.choices(nodes,p2_array)
            degree[random_node]=degree[random_node]+1
            
            
            # compute the adjency matrix of graph 
            adjency[random_node,i]=(adjency[random_node,i])+1
            adjency[i,random_node]=(adjency[i,random_node])+1
            
            
    return adjency,degree
    # return adjency matrix and degree matrix of PAM graph
    