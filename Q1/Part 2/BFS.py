import sys
from Rounds import problem_state

def runBFS(g, intial_state):
	sys.stdout = open("BFS.txt", "w")
	p = g.BFS(intial_state)
	if len(p):
		g.printPath(p, problem_state)
	else:
		print("Optimum Solution Not Found")
