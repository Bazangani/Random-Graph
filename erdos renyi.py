def erdos_renyi (n,p):
	#input: n number of node  p: probability of attachment 

    adj_matrix=np.zeros((n,n))
    for i in range (n):
        for j in range (i):
            adj_matrix[i,j]=(rd.random()<p)*1
            adj_matrix[j,i]=adj_matrix[i,j] # undicrected graph 
    return adj_matrix
    # return adjency matrix of edors_renyi