## Breadth-First Search (BFS) Algorithm for getting connected components in Undirected Graph

import queue as Q

"""
Function reads the graph from external txt file and returs the graph in form of a dictionary, along with the number of nodes
"""
def readGraph(path):
    G = {}                                                  ## Create empty dictionary to store graph
    num = 0                                                 ## Counter for number of nodes
    file = open(path)                                       ## Open the file from input path
    data = file.readlines()
    
    for line in data:
        num += 1                                            ## number of lines = number of nodes
        items = line.split()                                ## Separate the string to individual characters
        items = [int(i) for i in items]                     ## Store the edge nodes as integers

        ## First value of each line in input file is the 'home node' and each value following it corresponds to those nodes with which 'home node' shares an edges
        G[items[0]] = {}                                    ## Initialize a new dictionary for each 'home node'
        G[items[0]]['edges'] = items[1 : len(items) + 1]    ## Store nodes corresponding to edges
        G[items[0]]['isVisited'] = False                    ## Initialize each node as unvisited
        G[items[0]]['component'] = -1                       ## Initialize each node's distance as -1
    
    return G, num

"""
Function implements BFS algorithm to explore the graph.
Additionally, assigns the component number to the respective nodes
"""
def BFS(G, n, s, componentNum):
    q = Q.Queue(maxsize = n)
    q.put(s)
    G[s]['isVisited'] = True
    G[s]['component'] = componentNum
    
    while(not q.empty()):
        v = q.get()
        for w in G[v]['edges']:
            if(not G[w]['isVisited']):
                G[w]['isVisited'] = True
                q.put(w)
                G[w]['component'] = componentNum

    return graph

"""
Function implements BFS algorithm to get connected components
BFS() is recursively called for each component
"""
def BFS_loop(G, n):
    componentNum = 0

    for s in G.keys():
        if(not G[s]['isVisited']):
            componentNum += 1
            G = BFS(G, n, s, componentNum)

    return G
    
if __name__ == '__main__':
    graph, numNodes = readGraph('testBFS_Comp.txt')
    startingNode = 1
    
    graph = BFS_loop(graph, numNodes)
    
    for i in graph.items():
        print(i)
