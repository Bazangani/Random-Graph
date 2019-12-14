# Estimate the number of edges (Tour base estimation)
import time


G=nx.barabasi_albert_graph(200,10,seed=None)



init_node=max(dict(G.degree()).items(), key = lambda x : x[1])[0] # node with the biggest degree
number_of_walk=100000

k=0
t_i=[]

t_start = time.time()
node_list=[]
node_list.append(last_node)

for walk in range (number_of_walk):
    nei=list(G.neighbors(init_node))
    new_node=random.choice(nei)
    node_list.append(new_node)
    
    if new_node == 4:
        t_end=time.time()
        duration=t_end-t_start
        t_i.append(duration)
        k=k+1
        
    t0=time.time
    
sum_t=0
for t in t_i:
    sum_t=sum_t+t
t_hat=((1/k)*sum_t)*100


d_i=G.degree(init_node)

E=(d_i*t_hat)/2 # Estimate number of edges with random walk 
