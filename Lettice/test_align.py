# -*- coding: utf-8 -*-
"""
@author: gollapjr

"""

import random
import math

def calculate_hh_pairs(x_block, y_block):
    hh_pairs = 0
    for x in x_block:
        for y in y_block:
            
            if (x[0] == y[0] and abs(x[1] - y[1]) == 1) or (x[1] == y[1] and abs(x[0] - y[0]) == 1):
                hh_pairs += 1
    return hh_pairs

def simulated_annealing(x_blocks, y_blocks, temp, cooling_rate):
    if not x_blocks or not y_blocks:
        return [], 0

    current_solution = y_blocks.copy()
    best_solution = y_blocks.copy()
    best_score = calculate_hh_pairs(x_blocks, y_blocks)

    while temp > 0.1:
        
        new_solution = current_solution.copy()
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        
        current_score = calculate_hh_pairs(x_blocks, current_solution)
        new_score = calculate_hh_pairs(x_blocks, new_solution)

         
        if new_score > current_score or random.random() < math.exp((new_score - current_score) / temp):
            current_solution = new_solution.copy()
            if new_score > best_score:
                best_solution = new_solution.copy()
                best_score = new_score

      
        temp *= 1 - cooling_rate

    return best_solution, best_score

def align_protein_blocks(input_data):
    output = {}
    total_hh_pairs = 0
    total_unpaired_hs = 0

    
    initial_temp = 10000
    cooling_rate = 0.003

    for superblock in ['a', 'b']:
        x_blocks = input_data[superblock]['x']
        y_blocks = input_data[superblock]['y']

        
        optimal_alignment, hh_pairs = simulated_annealing(x_blocks, y_blocks, initial_temp, cooling_rate)
        total_hh_pairs += hh_pairs
        total_unpaired_hs += len(x_blocks) + len(y_blocks) - 2 * hh_pairs

        
        output[superblock] = {
            "optimal_alignment": optimal_alignment,
            "hh_pairs": hh_pairs
        }

    return output, total_hh_pairs, total_unpaired_hs

#sample input
input_data = {
    "a": {"x": [(2, 6)], "y": []},
    "b": {"x": [], "y": [7, 7]},
}

#run alignment optimization
output, total_hh_pairs, total_unpaired_hs = align_protein_blocks(input_data)

# Print output
print(output, total_hh_pairs, total_unpaired_hs)
