
class dp_cell():
    def __init__(self):
        self.value = 0
        self.parent = []
    
    def __repr__(self):
        return str(self.value)

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

def initiate_dp_table(dp_table, rho):
    dp_table[0][0].value = 0
    for i in range(1, len(dp_table)):
        dp_table[i][0].value = dp_table[i-1][0].value + rho
        dp_table[i][0].parent.append(dp_table[i-1][0])
    for j in range(1, len(dp_table[0])):
        dp_table[0][j].value = dp_table[0][j-1].value + rho
        dp_table[0][j].parent.append(dp_table[0][j-1])

def align_two_sequence(seq1, seq2, rho):
    s_matrix = calculate_S_matrix(seq1, seq2)
    dp_table = create_dp_table(s_matrix)
    initiate_dp_table(dp_table, rho)
    build_dp_table(dp_table, rho, s_matrix)
    
  
def build_dp_table(dp_table, rho, s_matrix):
    for i in range(1, len(dp_table)):
        for j in range(1, len(dp_table[0])):
            cur_cell = dp_table[i][j]
            val1 = rule_1(i,j,rho, dp_table, s_matrix)
            val2 = rule_2(i,j,rho, dp_table, s_matrix)
            val3 = rule_3(i,j,rho, dp_table, s_matrix)
            val = min(val1, val2, val3)
            cur_cell.value = val
            if(val1 == val):
                cur_cell.parent.append(dp_table[i-1][j])
            if(val2 == val):
                cur_cell.parent.append(dp_table[i][j-1])
            if(val3 == val):
                cur_cell.parent.append(dp_table[i-1][j-1])
  
def create_dp_table(s_matrix):
    dp_table = []
    for i in range(len(s_matrix)+1):
        dp_table.append([dp_cell() for j in range(len(s_matrix[0]))])
    return dp_table

def rule_1(i, j, rho, V, S):
    return V[i-1][j].value + rho

def rule_2(i, j, rho, V, S):
    return V[i][j-1].value + rho

def rule_3(i, j, rho, V, S):
    return V[i-1][j-1].value + S[i-1][j-1]