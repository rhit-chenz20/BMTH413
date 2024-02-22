# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:59:35 2024

@author: gollapjr
"""
samp_input={'a': {'x': [(3, 3), (7, 7), (9, 11), (13, 13)], 'y': [(0, 2), (6, 6), (8, 8), (12, 12), (16, 16)]}, 'b': {'x': [(20, 22), (24, 28), (32, 32), (46, 46), (48, 48)], 'y': [(17, 17), (23, 23), (29, 29), (33, 37), (47, 47)]}, 'ori': '1011001111011100110010111010110011000100000000111'}

def generate_superblock_a_coordinates(samp_input):
    # Extract block information and ori sequence from input
    y_blocks = samp_input['a']['y']
    x_blocks = samp_input['a']['x']
    ori_sequence = [int(digit) for digit in samp_input['ori']]

    # Initialize coordinates list and current position
    coordinates = []
    current_x, current_y = 0, 0

    # Alternate between y and x blocks, starting with y
    for y_block, x_block in zip(y_blocks, x_blocks):
        # Add coordinates for y block
        for i in range(y_block[0], y_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1

        # Add coordinates for x block
        for i in range(x_block[0], x_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1

    # Add any remaining y blocks
    for y_block in y_blocks[len(x_blocks):]:
        for i in range(y_block[0], y_block[1] + 1):
            coordinates.append((current_x, current_y if ori_sequence[i] == 1 else 0))
            current_x += 1

    return coordinates

# Generate coordinates for superblock 'a'
coordinates_a = generate_superblock_a_coordinates(samp_input)
print(coordinates_a)
print(len(coordinates_a)
      )

