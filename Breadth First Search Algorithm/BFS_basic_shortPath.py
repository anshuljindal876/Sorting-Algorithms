## Breadth-First Search (BFS) Algorithm for getting shortest path in Undirected Graph

import queue as Q
import math as M

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
        G[items[0]]['distance'] = M.inf                     ## Initialize each node's distance as infinity
    
    return G, num

"""
Function implements BFS algorithm to explore the graph.
Additionaly, shortest distance between starting node and current node is found ad stored at respective location in dictionary.
"""
def BFS(G, n, s):
    q = Q.Queue(maxsize = n)
    q.put(s)
    G[s]['distance'] = 0
    G[s]['isVisited'] = True
    
    while(not q.empty()):
        v = q.get()
        for w in G[v]['edges']:
            if(not G[w]['isVisited']):
                G[w]['isVisited'] = True
                q.put(w)
                G[w]['distance'] = G[v]['distance'] + 1

    return graph

if __name__ == '__main__':
    graph, numNodes = readGraph('testBFS2.txt')
    startingNode = 0
    
    graph = BFS(graph, numNodes, startingNode)
    
    for i in graph.items():
        i[1].pop('isVisited', None)     ## The isVisited flag is of no use now
        print(i)
