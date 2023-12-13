from dp_func import calculate_S_matrix, create_dp_table

test1 = [0.3, 0.5, 0.1, 0.03]
test2 = [0.6, 0.3, 0.001, 0.4, 0.7, 0.9]

s_matrix_result = calculate_S_matrix(test1, test2)
for i, v1 in enumerate(test1):
    for j, v2 in enumerate(test2):
        assert(s_matrix_result[i][j] == abs(v1-v2)/abs(v1+v2))
        
dp_table = create_dp_table(s_matrix_result)
assert(len(dp_table) == len(test1)+1)
assert(len(dp_table[0]) == len(test2)+1)

