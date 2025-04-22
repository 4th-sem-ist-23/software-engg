def dfs(graph , s_vertex , visited=None):
    if visited is None:
        visited = set()
    visited.add(s_vertex)
    print("Visiting Vertex : ",s_vertex)
    
    for next_vertex in graph[s_vertex] - visited:
        dfs(graph , next_vertex , visited)


graph = {
	'0' : {'1','2'},
	'1' : {'3'},
	'2' : {'4'},
	'3' : set(),
	'4' : set()
}

s_vertex = '0'

print("Graph Structure : ")
for vertex , neg in graph.items():
    print(f"{vertex} : {neg}")
    
dfs(graph , s_vertex)