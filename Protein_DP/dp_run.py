from dp_func import calculate_S_matrix, align_two_sequence

rho_values = [0.3]
num_digits = 4

f = open("prot_data.txt", "r")
protein_eigen_value = []
for x in f:
    protein_eigen_value.append(x)

for rho in rho_values:
    for i, prot1 in enumerate(protein_eigen_value):
        for j, prot2 in enumerate(protein_eigen_value):
            alignment_score = align_two_sequence(prot1, prot2, rho, num_digits = 4)