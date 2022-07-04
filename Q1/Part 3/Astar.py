#COMP-8700
#Assignment-2
import heapq

missionary_count = 3
cannibal_count = 3
boat_size = 2
heuristic_function = (missionary_count + cannibal_count) / boat_size

actions = []
for n in range(boat_size):
    actions.append((n+1, 0))
    actions.append((0, n+1))
    for a in range(n):
        actions.append((n+1-(a+1)%(n+1), (a+1)))

stack = []
checked = []

missionaries = missionary_count
cannibals = cannibal_count
boat = 'L'
parent = -1
action = -1
g = 0
h = (missionaries + cannibals)/boat_size
f = g + h

heapq.heappush(stack, (f, (missionaries, cannibals, boat, parent, action, g, h)))

z = 0
while any(stack):
    z = z + 1
    item = heapq.heappop(stack)[1]
    
    if item[2] == 'R' and item[0] + item[1] == 0:
        checked.append(item)
        print('\nEnded after checking {0} nodes'.format(z))
        break
    
    if heuristic_function * 4 < item[5]:
        checked.append(checked[0]) 
        print('\nEnded after checking {0} nodes'.format(z))
        break
    parent = len(checked)
    checked.append(item)
    g = item[5] + 1
    boat = 'R' if item[2] == 'L' else 'L'
    for i, a in enumerate(actions):
        action = i
     
        if boat == 'R':
            missionaries = item[0] - a[0]
            cannibals = item[1] - a[1]
            R_M = missionary_count - item[0] + a[0]
            R_C = cannibal_count - item[1] + a[1]
        if boat == 'L':
            missionaries = item[0] + a[0]
            cannibals = item[1] + a[1]
            R_M = missionary_count - item[0] - a[0]
            R_C = cannibal_count - item[1] - a[1]
    
        if missionaries > missionary_count:
            pass
        elif cannibals > cannibal_count:
            pass
        elif R_M > missionary_count:
            pass
        elif R_C > cannibal_count:
            pass
        elif cannibals > missionaries and missionaries > 0:
            pass
        elif R_C > R_M and R_M > 0:
            pass
     
        else:
            h = (missionaries + cannibals)/boat_size
            f = g + h
            heapq.heappush(stack, (f,(missionaries, cannibals, boat, parent, action, g, h)))


path = []
node = checked[-1]
parent = node[3]
path.append(node)
if parent == -1:
    print('Optimal path cannot be found')
else:
    while parent != -1:
        node = checked[parent]
        parent = node[3]
       
        if node[4] != -1:
            path.append(node)
              

    print('\nPossible Moves using A* search')
    print('-------------------------------------')
    for i, node in enumerate(path):
        direction = 'right' if node[2] == 'R' else 'left'
        action = actions[node[4]]
        message = 'Move {0}: Bring {1} missionaries and {2} cannibals to the {3}'.format(
            i+1, action[0], action[1], direction)
        print(message)
    print('\n')