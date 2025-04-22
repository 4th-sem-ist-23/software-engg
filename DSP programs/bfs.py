def bfs(s_vertex , graph):
    queue = []
    visited = set()
    queue.append(s_vertex)
    visited.add(s_vertex)
    
    while queue:
        c_vertex = queue.pop(0)
        print(c_vertex , end=" ")
        
        for neg in graph[c_vertex]:
            if neg not in visited:
                queue.append(neg)
                visited.add(neg)

graph = {
	'A' : ['B' , 'C'],
	'B' : ['D'],
	'C' : ['E'],
	'D' : [],
	'E' : []
}

s_vertex = 'A'

print("Graph structure : ")
for vertex , neg in graph.items():
    print(vertex , neg)

print("Visited Vertices : ")
bfs(s_vertex , graph)

    