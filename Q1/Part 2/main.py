#COMP-8700
#Assignment-2
import sys
from Rounds import State, Direction
from Utility import Utility;
from BFS  import runBFS
from DFS  import runDFS
from Constants import CONST

print_output = sys.stdout

def genPossibleMoves(CAP_BOAT):
	moves = []
	for m in range(CAP_BOAT + 1):
		for c in range(CAP_BOAT + 1):
			if 0 < m < c:
				continue
			if 1 <= m + c <= CAP_BOAT:
				moves.append((m, c))
	return moves

def main():
	CNST = CONST(3, 3, 2)
	moves = genPossibleMoves(2)
	intial_state = State(CNST.MAX_M, CNST.MAX_C, Direction.LEFT_TO_RIGHT, 0, 0, 0, CNST, moves)

	print("\nExecuting BFS Algorithm on Missionary and Cannibal problem")
	runBFS(Utility(), intial_state)
	sys.stdout = print_output
	print("BFS Algorithm Executed")

	print("\nExecuting DFS Algorithm on Missionary and Cannibal problem")
	runDFS(Utility(), intial_state)
	sys.stdout = print_output
	print("DFS Algorithm Executed\n")

if __name__ == '__main__':
	main()
