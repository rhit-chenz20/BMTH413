# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:59:35 2024

@author: gollapjr
"""
def generate_superblock_a_coordinates(samp_input):
    y_blocks = samp_input['a']['y']
    x_blocks = samp_input['a']['x']
    ori_sequence = [int(digit) for digit in samp_input['ori']]

    coordinates = []
    current_x, current_y = 0, 0

    # Add coordinates for y and x blocks
    for y_block, x_block in zip(y_blocks, x_blocks):
        for i in range(y_block[0], y_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1
        for i in range(x_block[0], x_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1

    # Add any remaining y blocks
    for y_block in y_blocks[len(x_blocks):]:
        for i in range(y_block[0], y_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1

    return coordinates

def find_zero_separator_ranges(samp_input):
    # Combine and sort all block ranges
    blocks = sorted(samp_input['a']['y'] + samp_input['a']['x'], key=lambda x: x[0])
    ori_sequence = samp_input['ori']
    zero_separators = []

    # Identify zero separators between blocks
    last_end = -1
    for start, end in blocks:
        if last_end != -1 and start - last_end > 1:  # Gap found
            gap_sequence = ori_sequence[last_end + 1:start]
            if all(bit == '0' for bit in gap_sequence):  # All zeros in the gap
                zero_separators.append((last_end + 1, start - 1))
        last_end = end

    return zero_separators

# Sample input
samp_input = {
    'a': {'x': [(3, 3), (7, 7), (9, 11), (13, 13)], 'y': [(0, 2), (6, 6), (8, 8), (12, 12), (16, 16)]},
    'b': {'x': [(20, 22), (24, 28), (32, 32), (46, 46), (48, 48)], 'y': [(17, 17), (23, 23), (29, 29), (33, 37), (47, 47)]},
    'ori': '1011001111011100110010111010110011000100000000111'
}

# Generate coordinates for superblock A and find zero separator ranges
coordinates_a = generate_superblock_a_coordinates(samp_input)
zero_separators = find_zero_separator_ranges(samp_input)



def insert_zero_separators(coordinates_a, zero_separators):
    arr = coordinates_a[:]  # Make a copy to avoid altering the original list directly
    
    for i in zero_separators:
        fXPos = arr[i[0]-1][0]  # First X position is based on the coordinate before the separator
        lXPos = arr[i[0]][0]    # Last X position is based on the first coordinate of the separator
        yPos = 1  # Y position starts at 1 above the block preceding the separator
        h = int((i[1] - i[0] + 1) / 2)  # Halfway point for the separator
        
        # Insert ascending part of the separator
        for k in range(i[0], i[0] + h):
            insert_index = arr.index((fXPos, yPos-1)) + 1 if yPos > 1 else k
            arr.insert(insert_index, (fXPos, yPos))
            yPos += 1
        
        # Adjust yPos for descending part
        yPos -= 1

        # Insert descending part of the separator
        for j in range(i[0] + h, i[1] + 1):
            insert_index = arr.index((lXPos, yPos+1)) if yPos < h else j
            arr.insert(insert_index, (lXPos, yPos))
            yPos -= 1

    return arr
# Assuming coordinates_a and zero_separators are defined from previous steps
updated_coordinates_with_separators = insert_zero_separators(coordinates_a, zero_separators)
print(updated_coordinates_with_separators)

