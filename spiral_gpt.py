def create_spiral_matrix(size, word):
    matrix = [[' ' for _ in range(size)] for _ in range(size)]

    if size % 2 == 0:
        # If the size is even, start in the lower half of the matrix
        start_row = size // 2
        start_col = size // 2 - 1
    else:
        # If the size is odd, start at the center
        start_row = size // 2
        start_col = size // 2

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0

    for letter in word:
        matrix[start_row][start_col] = letter
        next_row, next_col = start_row + directions[direction_index][0], start_col + directions[direction_index][1]

        # Check if the next position is out of bounds or already filled
        if (next_row < 0 or next_row >= size or next_col < 0 or next_col >= size or matrix[next_row][next_col] != ' '):
            direction_index = (direction_index + 1) % 4
            next_row, next_col = start_row + directions[direction_index][0], start_col + directions[direction_index][1]

        start_row, start_col = next_row, next_col

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

# Example usage:
side_length = 5
input_word = "HELLO"
matrix = create_spiral_matrix(side_length, input_word)
print_matrix(matrix)



create_spiral_matrix(3, "COPYRIGHt")  # ➞ [
#   ["G", "H", "T"],
#   ["I", "C", "O"],
#   ["R", "Y", "P"]
# ]