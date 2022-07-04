from Constants import Direction

MAX_M = 30
MAX_C = 30
CAP_BOAT = 20
CNST = None


class State(object):

	def __init__(self, missionaries, cannibals, dir, missionariesPassed, cannibalsPassed, level, CONSTS,moves):
		self.missionaries = missionaries
		self.cannibals = cannibals
		self.dir = dir
		self.action = ""
		self.level = level
		self.missionariesPassed = missionariesPassed
		self.cannibalsPassed = cannibalsPassed
		self.CONSTANTS = CONSTS

		self.moves = moves

		global MAX_M
		global MAX_C
		global CAP_BOAT
		global CNST

		if not CONSTS is None:
			CNST = CONSTS

			MAX_M = CONSTS.MAX_M
			MAX_C = CONSTS.MAX_C
			CAP_BOAT = CONSTS.CAP_BOAT

	def successors(self):
		listSuccessor = []
		if not self.isValid() or self.isGoalState():
			return listSuccessor
		if self.dir == Direction.LEFT_TO_RIGHT:
			sgn = -1
			direction = "from the left side to the right side"
		else:
			sgn = 1
			direction = "back from the left side to the right side"
		for i in self.moves:
			(m, c) = i
			self.addValidSuccessors(listSuccessor, m, c, sgn, direction)
		return listSuccessor

	def addValidSuccessors(self, listSuccessor, m, c, sgn, direction):
		newState = State(self.missionaries + sgn * m, self.cannibals + sgn * c, self.dir + sgn * 1,
							self.missionariesPassed - sgn * m, self.cannibalsPassed - sgn * c, self.level + 1,
							self.CONSTANTS,self.moves)
		if newState.isValid():
			newState.action = " Bring %d missionaries and %d cannibals %s." % (m, c, direction)
			listSuccessor.append(newState)

	def isValid(self):
		
		if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > MAX_M or self.cannibals > MAX_C or (
				self.dir != 0 and self.dir != 1):
			return False

		if (self.cannibals > self.missionaries > 0) or (
				self.cannibalsPassed > self.missionariesPassed > 0): 
			return False

		return True

	def isGoalState(self):
		return self.cannibals == 0 and self.missionaries == 0 and self.dir == Direction.RIGHT_TO_LEFT

	def __repr__(self):
		return "%s\n\n %d Round (%d, %d, %d, %d, %d)" % (
			self.action, self.level+1, self.missionaries, self.cannibals, self.dir, self.missionariesPassed,
			self.cannibalsPassed)

	def __eq__(self, other):
		return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.dir == other.dir

	def __hash__(self):
		return hash((self.missionaries, self.cannibals, self.dir))

	def __ne__(self, other):
		return not (self == other)


problem_state = State(-1, -1, Direction.RIGHT_TO_LEFT, -1, -1, 0, CNST,None)

