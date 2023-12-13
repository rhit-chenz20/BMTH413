
class dp_cell():
    def __init__(self):
        self.value = 0

def calculate_S_matrix(pro1_eigen_v, pro2_eigen_v):
    result = []
    for i, v1 in enumerate(pro1_eigen_v):
        r1 = []
        for j, v2 in enumerate(pro2_eigen_v):
            r1.append(calculate_S_i_j(v1, v2))
        result.append(r1)
    return result

def calculate_S_i_j(v1, v2):
    return abs(v1-v2)/abs(v1+v2)

def align_two_sequence(seq1, seq2, rho):
    s_matrix = calculate_S_matrix(seq1, seq2)
    dp_table = create_dp_table(s_matrix)
    
def create_dp_table(s_matrix):
    dp_table = [[dp_cell()]*(len(s_matrix[0])+1) for i in range(len(s_matrix)+1)]
    return dp_table

def rule_1(i, j, rho, V):
    pass

def rule_2():
    pass

def rule_3():
    pass