#COMP-8700
#Assignment-2
from Rounds import problem_state
import time

class Utility:

	def __init__(self):

		self.bfs_parent = {}
		self.dfs_parent = {}

		self.expandedBFS = 0
		self.expandedDFS = 0

	def BFS(self, s):
		self.expandedBFS = 0
		self.bfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}
		s.level = 0
		queue = [s]
		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)

			if u.isGoalState():
				print("Expanded Node Count: " + str(self.expandedBFS))
				print("Explored Node Count: " + str(visited.__len__()))
				queue.clear()
				self.bfs_parent[problem_state] = u
				return self.bfs_parent

			for v in reversed(u.successors()):
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[(v.missionaries, v.cannibals, v.dir)] = True

		return {}

	def DFS(self, s):
		self.expandedDFS = 0
		self.dfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}

		start_time = time.time()
		stack = [s]
		while stack:
			u = stack.pop()
			self.expandedDFS += 1

			if u.isGoalState():
				print("Expanded Node Count: " + str(self.expandedDFS))
				print("Explored Node Count: " + str(visited.__len__()))
				self.dfs_parent[problem_state] = u
				stack.clear()
				return self.dfs_parent

			t = time.time() - start_time
				

			for v in u.successors():
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					visited[(v.missionaries, v.cannibals, v.dir)] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return {}

	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None: 
			return
		if tail == problem_state: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
