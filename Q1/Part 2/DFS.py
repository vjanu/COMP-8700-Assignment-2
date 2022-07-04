#COMP-8700
#Assignment-2
import sys
from Rounds import problem_state

def runDFS(g, intial_state):
	sys.stdout = open("DFS.txt", "w")
	p = g.DFS(intial_state)
	if len(p):
		g.printPath(p, problem_state)
	else:
		print("Optimum Solution Not Found")