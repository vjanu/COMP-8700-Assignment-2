#COMP-8700
#Assignment-2
from queue import PriorityQueue
total_player = 0


def trace_path(goal):
    print("Goal state")
    path = list()
    node = goal
    while node.parent != None:
        path.append(node)
        node = node.parent
    path.append(node)
    while path:
        print(path.pop().state)
    print("\n")


class Problem(object):

    def __init__(self, initial, goal=None):

        self.initial = initial
        self.goal = goal

    def actions(self, state):
        ans = list()
        if state[4] == 'L':
            if(state[0] >= 2):
                if ((state[1] <= (state[0]-2)) or state[0] == 2) and (state[3] <= (state[2]+2)):
                    ans.append([state[0] - 2, state[1], state[2]+2, state[3], 'R'])
            if(state[1] >= 2):
                if ((state[2] >= (state[3] +2)) or state[2] == 0):
                    ans.append([state[0], state[1]-2, state[2], state[3]+2, 'R'])
            if(state[0] >= 1):
                if ((state[1] <= (state[0]-1)) or state[0] == 1) and (state[3] <= (state[2]+1)):
                    ans.append([state[0] - 1, state[1], state[2]+1, state[3], 'R'])
            if(state[1] >= 1):
                if (state[2] >= (state[3] +1)) or state[2] == 0:
                    ans.append([state[0], state[1]-1, state[2], state[3]+1, 'R'])
            if((state[0] >= 1 and state[1] >= 1)) and ((state[3]+1) <= (state[2]+1)):
                ans.append([state[0]-1, state[1]-1, state[2]+1, state[3]+1, 'R'])
        else:
            if(state[2] >= 2):
                if (state[3] <= (state[2]-2) or state[2] == 2) and (state[1] <= (state[0]+2)):
                    ans.append([state[0] + 2, state[1], state[2]-2, state[3], 'L'])
            if(state[3] >= 2):
                if state[0] >= (state[1] +2) or state[0] == 0:
                    ans.append([state[0], state[1]+2, state[2], state[3]-2, 'L'])
            if(state[2] >= 1):
                if (state[3] <= (state[2]-1) or state[2] == 1) and (state[1] <= (state[0]+1)):
                    ans.append([state[0] + 1, state[1], state[2]-1, state[3], 'L'])
            if(state[3] >= 1):
                if state[0] >= (state[1] +1) or state[0] == 0:
                    ans.append([state[0], state[1]+1, state[2], state[3]-1, 'L'])
            if(state[2] >= 1 and state[3] >= 1) and ((state[0]+1) <= (state[1]+1)):
                ans.append([state[0]+1, state[1]+1, state[2]-1, state[3]-1, 'L'])

        return ans

    def result(self, state, action):
        return action

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state,
                                           action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]

    memf.cache = {}
    return memf

def best_first_graph_search(problem, f):
    f = memoize(f)
    node = Node(problem.initial)
    frontier = PriorityQueue(f)
    explored = list()
    while frontier:
        node = frontier.get()
        print("Current Node:", node.state)
        if problem.goal_test(node.state):
            trace_path(node)
            return node
        explored.append(node.state)
        print("Explored Nodes:", explored)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
        temp_front = list()
        for e in frontier.heap:
            val, node = e
            temp_front.append(node.state)
        print("Separation Nodes:", temp_front)
        print("\n")
    return None

def heuristic(n):
        return (n.state[0]+n.state[1]-1)/2

def greedy_best_first_graph_search(problem, h=None):
    h = memoize(h or problem.h)
    return best_first_graph_search(problem, lambda n: h(n))


if __name__ == "__main__":
    
    missionary_count = 3
    cannibal_count = 3
    total_player = missionary_count + cannibal_count

    print("Greedy Best First Search Algorithm:")
    greedy_best_first_graph_search(Problem([missionary_count,cannibal_count, 0, 0, 'L'], [0,0, missionary_count,cannibal_count,'R']), heuristic)

