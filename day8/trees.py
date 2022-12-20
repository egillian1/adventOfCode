file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]

def parse_line(line, trees):
    tree_row = []
    for tree in line:
        tree_row.append(int(tree))
    
    trees.append(tree_row)
    
def is_tree_visible(trees, row_idx, column_idx, row_length, column_length):
    current_tree = trees[row_idx][column_idx]

    top_visible = True
    bottom_visible = True
    left_visible = True
    right_visible = True   

    # Visibility from the top
    for i in reversed(range(row_idx)):
        top_visible = top_visible and (trees[i][column_idx] < current_tree)

    # Visibility from the bottom
    for i in range(row_idx + 1, row_length):
        bottom_visible = bottom_visible and (trees[i][column_idx] < current_tree)
    
    # Visibility from the left
    for i in reversed(range(column_idx)):
        left_visible = left_visible and (trees[row_idx][i] < current_tree)

    # Visibility from the right
    for i in range(column_idx + 1, column_length):
        right_visible = right_visible and (trees[row_idx][i] < current_tree)

    return top_visible or bottom_visible or left_visible or right_visible

# Parse the tree input into a matrix
trees = []
for line in stripped:
    if len(line) == 0:
        break

    parse_line(line, trees)

# Calculate the amount of visible trees
row_length = len(trees[0])
column_length = len(trees)
total_visible = 0
for row_idx in range(row_length):
    for column_idx in range(column_length):
        if is_tree_visible(trees, row_idx, column_idx, row_length, column_length):
            total_visible += 1

print(total_visible)
