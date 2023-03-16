from collections import deque

# Define the initial state
initial_state = "_________"

# Define the goal states
goal_states = [
    # Horizontal wins
    "XXX______",
    "___XXX___",
    "______XXX",
    # Vertical wins
    "X__X__X__",
    "_X__X__X_",
    "__X__X__X",
    "X___X___X",
    # Diagonal wins
    "__X_X_X__",
]

# Define the operators
def get_next_states(state, player): # state is the current state of the game, player is the current player
    next_states = [] # next_states stores the next states
    for i in range(len(state)): # for each position in the state
        if state[i] == "_": # if the position is empty
            next_state = state[:i] + player + state[i+1:] # add the player to the position
            next_states.append(next_state) # add the next state to the next_states list
    return next_states # return the next_states list

# Implement BFS
def bfs(initial_state, goal_states): # initial_state is the current state of the game
    visited = set() # visited stores the states that have been visited
    queue = deque([(initial_state, "X"), (initial_state, "O")]) # queue stores the states that have not been visited
    while queue: # while the queue is not empty
        state, player = queue.popleft() # get the next state and player
        if state in visited:
            continue
        visited.add(state) # add the state to the visited set
        if state in goal_states:
            return state
        next_states = get_next_states(state, player) # get the next states from the current state and player
        for next_state in next_states:
            queue.append((next_state, "X" if player == "O" else "O")) # add the next state and player to the queue if the state has not been visited
    return None

# Visualize the state space
def visualize_state_space():
    # visited stores the states that have been visited
    visited = set()
    # queue stores the states that have not been visited
    queue = deque([(initial_state, "X"), (initial_state, "O")])
    # while the queue is not empty
    while queue:
        # get the next state and player
        state, player = queue.popleft()
        # check if the state has been visited
        if state in visited:
            continue
        visited.add(state) # add the state to the visited set
        print(state[:3]+"\n") # print the first row
        print(state[3:6]+"\n")   # print the second row
        print(state[6:]+"\n")   # print the third row
        print(f"Player: {player}") # print the player
        print("____________________") # print a line to separate the states

        next_states = get_next_states(state, player) # get the next states from the current state and player
        for next_state in next_states: # for each next state
            queue.append((next_state, "X" if player == "O" else "O")) # add the next state and player to the queue if the state has not been visited

# Visualize the BFS with each state and player
def visualize_bfs():
    # visited stores the states that have been visited
    visited = set()
    # queue stores the states that have not been visited
    queue = deque([(initial_state, "X"), (initial_state, "O")]) # (state, player) tuple 
    # while the queue is not empty
    while queue:
        # get the next state and player
        state, player = queue.popleft() # (state, player) tuple
        # check if the state has been visited
        if state in visited:
            # if the state has been visited,
            continue
        # if the state has not been visited,
        visited.add(state) # add the state to the visited set
        print(f"{state[:3]}\n{state[3:6]}\n{state[6:]} ({player}) \n\n") # print the state and player
        next_states = get_next_states(state, player) # get the next states from the current state and player
        for next_state in next_states: # for each next state
            queue.append((next_state, "X" if player == "O" else "O")) # add the next state and player to the queue if the state has not been visited

# Implement the play game function to play tic-tac-toe with the computer

def play_game():
    # stae stores the current state of the game or initial state
    state = initial_state
    player = "X" # X always starts first
    while True: # infinite loop
        # print the current state of the game
        print(f"Current state: ")
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        # check if the current state is a goal state
        if state in goal_states:
            # print the winner
            print(f"{state} is a goal state. {player} wins!")
            break
        # get the next move from Bfs algorithm
        next_move = bfs(state, goal_states)
        # check if there is a next move
        if next_move is None:
            # print no more moves
            print("No more moves. It's a tie!")
            break
        # update the state with the next move and change the player
        state = next_move
        player = "O" if player == "X" else "X"

# Run the game 
if __name__ == "__main__":
    visualize_state_space()
    # visualize_bfs()
    play_game()
