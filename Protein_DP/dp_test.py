from dp_func import calculate_S_matrix, create_dp_table, initiate_dp_table, build_dp_table, back_trace

test1 = [0.3, 0.5, 0.1, 0.03]
test2 = [0.6, 0.3, 0.001, 0.4, 0.7, 0.9]
num_digits = 2

# s_matrix_result = calculate_S_matrix(test1, test2, num_digits)
# for i, v1 in enumerate(test1):
#     for j, v2 in enumerate(test2):
#         assert(s_matrix_result[i][j] == abs(v1-v2)/abs(v1+v2))
        
# dp_table = create_dp_table(s_matrix_result)
# assert(len(dp_table) == len(test1)+1)
# assert(len(dp_table[0]) == len(test2))

s_matrix = [[0.1,0.2,0.8, 0.7, 1.2],
            [0.5, 0.4, 0.2, 0.1, 0.5],
            [0.2 ,0.3, 0.1, 0.2 ,0.2],
            [0.8, 0.7 ,0.6, 0.1, 0.1]]

rho = 0.3
dp_table = create_dp_table(s_matrix)

initiate_dp_table(dp_table, rho, num_digits)

build_dp_table(dp_table, rho, s_matrix, num_digits)

expected = [[0.00, 0.30, 0.60, 0.90, 1.20, 1.50],
            [0.30, 0.10, 0.40, 0.70, 1.00, 1.30],
            [0.60, 0.40, 0.50, 0.60, 0.80, 1.10],
            [0.90, 0.70, 0.70, 0.60, 0.80, 1.00],
            [1.20, 1.00, 1.00, 0.90, 0.70, 0.90]]

# print(dp_table)

for i in range(len(expected)):
    for j in range(len(expected[0])):
        assert dp_table[i][j].value==expected[i][j], str(i) +" " + str(j)+ " excpeted: " + str(expected[i][j])+" but got " + str(dp_table[i][j].value)
    
end_cell = dp_table[len(dp_table)-1][len(dp_table[0])-1]
trace = back_trace(end_cell, [[]])

for r in trace:
    for x in r:
        print(x)
