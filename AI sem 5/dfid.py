from collections import defaultdict

class Graph:

	def __init__(self,vertices):

		self.V = vertices # Number of vertices
		self.graph = defaultdict(list)


	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DLS(self,src,target,maxDepth):

		if src == target : return True
		if maxDepth <= 0 : return False

		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False
		
	def IDDFS(self,src, target, maxDepth):
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False

# Create a graph
#        0
#      /   \
#     1      2
#    / \     | \
#   3   4   5   6

g = Graph (7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

for i in range(2):
	target = [5, 3]; maxDepth = [3,2]; src = 0

	if g.IDDFS(src, target[i], maxDepth[i]) == True:
		print ("Target "+str(target[i]) +" is reachable from source within max depth of "+str(maxDepth[i]))
	else :
		print ("Target "+str(target[i]) +" is NOT reachable from source within max depth of "+str(maxDepth[i]))



# from collections import defaultdict

# class Graph:

#     def __init__(self, vertices):
#         self.V = vertices  # Number of vertices
#         self.graph = defaultdict(list)
#         self.open_list = []
#         self.closed_list = []

#     def addEdge(self, u, v):
#         self.graph[u].append(v)

#     def DLS(self, src, target, maxDepth, currentDepth, path):
#         self.open_list.append((src, currentDepth, path))
#         if src == target:
#             self.closed_list.append((src, True, path))
#             return True
#         if maxDepth <= 0:
#             self.closed_list.append((src, False, path))
#             return False

#         for i in self.graph[src]:
#             if self.DLS(i, target, maxDepth - 1, currentDepth + 1, path + [i]):
#                 return True
#         self.closed_list.append((src, False, path))
#         return False

#     def IDDFS(self, src, target, maxDepth):
#         for i in range(maxDepth):
#             if self.DLS(src, target, i, 0, [src]):
#                 return True
#         return False


# g = Graph(7)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(2, 6)

# for i in range(2):
#     target = [5, 6]
#     maxDepth = [3, 2]
#     src = 0

#     if g.IDDFS(src, target[i], maxDepth[i]):
#         print(f"Target {target[i]} is reachable from source within a maximum depth of {maxDepth[i]}.")
#     else:
#         print(f"Target {target[i]} is NOT reachable from source within a maximum depth of {maxDepth[i]}.")

#     print("Open List: ", g.open_list)
#     print("Closed List: ", g.closed_list)
#     g.open_list = []
#     g.closed_list = []