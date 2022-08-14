goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)


def expand_node(node, nodes):
    expanded_nodes = [create_node(move_left(node.state), node, "Left", node.depth + 1, 0),
                      create_node(move_right(node.state), node, "Right", node.depth + 1, 0),
                      create_node(move_up(node.state), node, "Up", node.depth + 1, 0),
                      create_node(move_down(node.state), node, "Down", node.depth + 1, 0)]
    expanded_nodes = [node for node in expanded_nodes if node.state is not None]
    return expanded_nodes


def move_left(state):
    index = state.index(0)
    cpy_state = state.copy()
    if index not in [0, 3, 6]:
        cpy_state[index], cpy_state[index - 1] = cpy_state[index - 1], cpy_state[index]
        return cpy_state
    return None


def move_right(state):
    index = state.index(0)
    cpy_state = state.copy()
    if index not in [2, 5, 8]:
        cpy_state[index], cpy_state[index + 1] = cpy_state[index + 1], cpy_state[index]
        return cpy_state
    return None


def move_up(state):
    index = state.index(0)
    cpy_state = state.copy()
    if index not in [0, 1, 2]:
        cpy_state[index], cpy_state[index - 3] = cpy_state[index - 3], cpy_state[index]
        return cpy_state
    return None


def move_down(state):
    index = state.index(0)
    cpy_state = state.copy()
    if index not in [6, 7, 8]:
        cpy_state[index], cpy_state[index + 3] = cpy_state[index + 3], cpy_state[index]
        return cpy_state
    return None


def bfs(start, goal, limit):
    startNode = create_node(start, None, None, 0, 0)
    nodes = [startNode]
    visited = []
    cost = 0
    traversed = 0

    while nodes:
        check = False
        node = nodes.pop(0)
        traversed += 1
        if node.state == goal:
            return cost, node, traversed
        for i in visited:   # checking if node is already visited or not
            if i.state == node.state:
                check = True
        if check:   # if node is already visited then ignore it
            continue
        visited.append(node)
        expanded_nodes = expand_node(node, nodes)
        nodes.extend(expanded_nodes)
        cost += len(expanded_nodes)
        if cost > limit:    # if maximum number of moves crossed
            return -1, None, -1
    return None


def printBoard(Path):   # function to print the board
    for i in Path:
        print("")
        if i.parent is not None:
            print("Moving: ", i.operator)
        else:
            print("STARTING THE GAME.")
        print(i.state[0], i.state[1], i.state[2])
        print(i.state[3], i.state[4], i.state[5])
        print(i.state[6], i.state[7], i.state[8])
    print("GOAL STATE ACHIEVED.")


def main():
    starting_state = []
    print("Enter elements of 3x3 board")
    for i in range(0, 9):
        print("Enter Element No", i + 1, ": ", end='')
        starting_state.append(int(input()))
    limit = int(input("Enter maximum number of moves: "))

    if len(starting_state) == 9:
        cost, result, traversed = bfs(starting_state, goal_state, limit)
        if result is None:
            if cost == -1:
                print("\nMaximum limit of moves reached. Can't find solution.")
            else:
                print("No solution found.")
        elif result.depth == 0:
            print("\nStart node was the goal!")
            print("No of correct pieces = 0\nNo of nodes traversed = 1\nNo of moves utilized = 0")
        else:
            moves = result.depth
            path = []
            while result.parent is not None:
                path.insert(0, result)
                result = result.parent
            path.insert(0, create_node(starting_state, None, None, 0, 0))
            printBoard(path)
            print("No of correct pieces = ", moves, "\nNo of nodes traversed = ", traversed, "\nNo of moves utilized = ", cost)

    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
