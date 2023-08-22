Graph = [(1,2,6), (2,3,2), (1,3,5), (2,4,3), (3,4,1)]
Vertex = [1,2,3,4]

def check_cycle(vertex, visited):
    for i in range(visited):
        if visited[i] == vertex:
            return True

def check_min(vertex):
    # Check Form List Of Connected Edges and Return The Minimum Distance Edge
    pass

def prims_algorithm(Graph):
    visited = list()
    mst = list()
    
    for i in range(Vertex):
        if check_cycle(Graph[i][1], visited):
            continue
        else:
            edge = check_min(Vertex[i])
            
            visited.append(Vertex)
            mst.append(edge)


            
        