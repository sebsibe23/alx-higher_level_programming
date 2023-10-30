#!/usr/bin/python3
"""Module for task 10 of project 0x08.
"""

import sys

def solve_nqueens(num_of_queens):
    # Helper function to check if a queen can be placed at a certain position
    def can_place_queen(position, occupied_positions):
        for occupied_position in range(len(occupied_positions)):
            # Check if there's a queen in the same row or on the same diagonal
            if occupied_positions[occupied_position] == position or \
                occupied_positions[occupied_position] - occupied_position == position - len(occupied_positions) or \
                occupied_positions[occupied_position] + occupied_position == position + len(occupied_positions):
                return False
        return True

    # Recursive function to place queens on the board
    def place_queens(num_of_queens, current_index, occupied_positions, solutions):
        if current_index == num_of_queens:  # All queens are placed
            solutions.append(occupied_positions[:])
            return
        for i in range(num_of_queens):  # For each column
            if can_place_queen(i, occupied_positions):  # Check if queen can be placed here
                occupied_positions.append(i)  # Place queen at this position
                place_queens(num_of_queens, current_index + 1, occupied_positions, solutions)  # Recurse for next queen
                occupied_positions.pop()  # Remove queen from this position

    solutions = []
    place_queens(num_of_queens, 0, [], solutions)  # Start placing queens from the first row
    return solutions

def main():
    if len(sys.argv) != 2:  # Check for correct number of arguments
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        num_of_queens = int(sys.argv[1])  # Try to convert argument to an integer
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if num_of_queens < 4:  # Check if size of board is large enough
        print("N must be at least 4")
        sys.exit(1)

    all_solutions = solve_nqueens(num_of_queens)  # Solve the N Queens problem
    for solution in all_solutions:  # Print all solutions
        formatted_solution = [[i, pos] for i, pos in enumerate(solution)]
        print(formatted_solution)

if __name__ == "__main__":
    main()

