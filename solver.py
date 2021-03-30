import copy
from cube import RubiksCube
from util import Node, QueueFrontier

def main():

    # Init the cube
    print("Start:")
    cube = RubiksCube()
    cube.show()
    
    # Shuffle the cube
    moves = ["F", "R", "Ui", "D", "D"]
    print("Rotating:", moves)
    for move in moves:
        cube.rotate(move)
    cube.show()

    # Check if cube is finished
    if cube.isFinished():
        print("Finished!")
    else:
        print("Solving...")
    
    # Init a frontier with the shuffled cube as start
    start = Node(state=cube, parent=None, action=None)
    frontier = QueueFrontier()  # queue is FIFO; performs a Breadth First Search
    frontier.add(start)

    # Keep looping until a solution is found
    while True:

        # Choose the first node from the frontier
        node = frontier.remove()
        
        # Add neighbors to the frontier
        possibleMoves = ["U", "F", "L", "R", "D", "B", "Ui", "Fi", "Li", "Ri", "Di", "Bi"]
        for move in possibleMoves:
            
            # Try a move
            neighborCube = copy.deepcopy(node.state)
            neighborCube.rotate(move)

            # This move fixed the cube?
            if neighborCube.isFinished():
                moves = []
                moves.append(move)
                while node.parent is not None:
                    moves.append(node.action)
                    node = node.parent
                moves.reverse()
                print("Solved! Moves:", moves)
                print("Nodes:", len(frontier.frontier))
                return moves

            # No moves fixed the cube; keep going
            else:
                child = Node(state=neighborCube, parent=node, action=move)
                frontier.add(child)



if __name__ == "__main__":
    main()