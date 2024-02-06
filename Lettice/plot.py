import matplotlib.pyplot as plt

# Import specific functions from the protein_alignment module
from test_align import calculate_hh_pairs, simulated_annealing, align_protein_blocks

# Import the input_data dictionary from the input_data module
# from block import get_blocked_data

input_data = {
    "a": {"x": [(2, 6)], "y": []},
    "b": {"x": [], "y": [7, 7]},
}

output, total_hh_pairs, total_unpaired_hs = align_protein_blocks(input_data)

print(output)

# Assuming output is the result from align_protein_blocks
optimal_a = output['a']['optimal_alignment']
optimal_b = output['b']['optimal_alignment']

# Extract x and y coordinates
x_coords_a, y_coords_a = zip(*optimal_a) if optimal_a else ([], [])
x_coords_b, y_coords_b = zip(*optimal_b) if optimal_b else ([], [])


# Create plot
plt.figure(figsize=(10, 10))

# Plot the points for superblock 'a'
plt.scatter(x_coords_a, y_coords_a, c='red', label='Superblock A')

# Plot the points for superblock 'b'
plt.scatter(x_coords_b, y_coords_b, c='blue', label='Superblock B')

# Add grid, legend, and labels
plt.grid(True)
plt.legend()
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Optimal Alignment of Protein Blocks')

# Show plot
plt.show()
