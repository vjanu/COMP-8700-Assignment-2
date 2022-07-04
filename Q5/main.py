#COMP-8700
#Assignment-2
from statistics import mean, stdev
from random import choice

def steepest_ascent_hill_climbing(problem, allow_sideways=False, max_sideways=100):
    def get_min_cost_queen(node, problem):
        children = node.get_children()
        children_cost = [problem.Calculate_heuristic(child) for child in children]
        min_cost = min(children_cost)

        best_child = choice([child for child_index, child in enumerate(children) if children_cost[
            child_index] == min_cost])
        return best_child

    node = problem.start_state
    node_cost = problem.Calculate_heuristic(node)
    path = []
    sideways_moves = 0

    while True:
        path.append(node)
        best_child = get_min_cost_queen(node, problem)
        best_child_cost = problem.Calculate_heuristic(best_child)

        if best_child_cost > node_cost:
            break
        elif best_child_cost == node_cost:
            if not allow_sideways or sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_child
        node_cost = best_child_cost

    return {'outcome': 'success' if problem.goal_test(node) else 'failure',
            'solution': path,
            'problem': problem}

def calculate_avg_pathcost(result_list, key):
    results = [result[key] for result in result_list]
    if len(result_list) == 1:
        return {'mean': result_list[0][key], 'sd': 0}
    elif not result_list:
        return {'mean': 0, 'sd': 0}
    return {'mean': mean(results), 'sd': stdev(results)}

def print_results(results):
    column_width = 30
    column_width_data = 15

    def print_data_row(row_title, data_string, data_func, results):
        nonlocal column_width, column_width_data
        row = (row_title + '\t').rjust(column_width)
        result_groups = iter(results)
        next(result_groups)
        for result_group in result_groups:
            row += data_string.format(**data_func(result_group)).ljust(column_width_data)
        print(row)



    num_iterations = len(results[0])

    print('\t'.rjust(column_width) +
          'Successes'.ljust(column_width_data) +
          'Failures'.ljust(column_width_data))

    print_data_row('Success/Failure Rate:',
                   '{percent:.1%}',
                   lambda x: {'percent': len(x) / num_iterations},
                   results)

    print_data_row('Average number of steps:',
                   '{mean:.0f}',
                   lambda x: calculate_avg_pathcost(x, 'path_length'),
                   results)

def execute_Random_Search(results, Avg_restarts):
    column_width = 30
    column_width_data = 15

    def print_data_row(row_title, data_string, data_func, results):
        nonlocal column_width, column_width_data
        row = (row_title + '\t').rjust(column_width)
        result_groups = iter(results)
        next(result_groups)
        for result_group in result_groups:
            row += data_string.format(**data_func(result_group)).ljust(column_width_data)
        print(row)

    num_iterations = len(results[0])

    print('\t'.rjust(column_width) +
          'Successes'.ljust(column_width_data) +
          'Failures'.ljust(column_width_data))

    print_data_row('Success/Failure Rate:',
                   '{percent:.1%}',
                   lambda x: {'percent': len(x) / num_iterations},
                   results)

    print_data_row('Average number of steps:',
                   '{mean:.0f}',
                   lambda x: calculate_avg_pathcost(x, 'path_length'),
                   results)

def execute_algorithm(problem_set, search_function):
    results = []

    for problem_num, problem in enumerate(problem_set):
        result = search_function(problem)
        result['path_length'] = len(result['solution']) - 1
        results.append(result)
    results = [results,
               [result for result in results if result['outcome'] == 'success'],
               [result for result in results if result['outcome'] == 'failure']]

    if 'NoRestarts' in results[0][00]:
        ran_restarts = []
        for result in results[0]:
            ran_restarts.append(result['NoRestarts'])
        Avg_restarts = mean(ran_restarts)
        execute_Random_Search(results, Avg_restarts)
    else:
        print_results(results)


def hill_climbing(queens_state):
    print('\nSteepest-ascent Hill Climbing:')
    execute_algorithm(queens_state, steepest_ascent_hill_climbing)

    print('\nSteepest-ascent Hill Climbing with Sideway moves:')
    execute_algorithm(queens_state, lambda x: steepest_ascent_hill_climbing(x, allow_sideways=True))

from queens import QueensProblem

queens_state = [QueensProblem() for _ in range(1000)]
hill_climbing(queens_state)
