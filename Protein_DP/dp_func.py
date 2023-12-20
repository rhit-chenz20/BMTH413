
class dp_cell():
    def __init__(self):
        self.value = 0
        self.parent = []
    
    def __repr__(self):
        return str(self.value)

def calculate_S_matrix(pro1_eigen_v, pro2_eigen_v, num_digits):
    result = []
    for i, v1 in enumerate(pro1_eigen_v):
        r1 = []
        for j, v2 in enumerate(pro2_eigen_v):
            r1.append(calculate_S_i_j(v1, v2), num_digits)
        result.append(r1)
    return result

def calculate_S_i_j(v1, v2, num_digits):
    return round(abs(v1-v2)/abs(v1+v2), num_digits)

def initiate_dp_table(dp_table, rho, num_digits):
    dp_table[0][0].value = 0
    for i in range(1, len(dp_table)):
        dp_table[i][0].value = round(dp_table[i-1][0].value + rho, num_digits)
        dp_table[i][0].parent.append(dp_table[i-1][0])
    for j in range(1, len(dp_table[0])):
        dp_table[0][j].value = round(dp_table[0][j-1].value + rho, num_digits)
        dp_table[0][j].parent.append(dp_table[0][j-1])

def align_two_sequence(seq1, seq2, rho, num_digits):
    s_matrix = calculate_S_matrix(seq1, seq2, num_digits)
    dp_table = create_dp_table(s_matrix)
    initiate_dp_table(dp_table, rho, num_digits)
    build_dp_table(dp_table, rho, s_matrix, num_digits)
    
def build_dp_table(dp_table, rho, s_matrix, num_digits):
    for i in range(1, len(dp_table)):
        for j in range(1, len(dp_table[0])):
            cur_cell = dp_table[i][j]
            val1 = rule_1(i,j,rho, dp_table, s_matrix, num_digits)
            val2 = rule_2(i,j,rho, dp_table, s_matrix, num_digits)
            val3 = rule_3(i,j,rho, dp_table, s_matrix, num_digits)
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
        dp_table.append([dp_cell() for j in range(len(s_matrix[0])+1)])
    return dp_table

def rule_1(i, j, rho, V, S, num_digits):
    if(num_digits == -1):
        return V[i-1][j].value + rho
    return round(V[i-1][j].value + rho, num_digits)

def rule_2(i, j, rho, V, S, num_digits):
    if(num_digits == -1):
        V[i][j-1].value + rho
    return round(V[i][j-1].value + rho, num_digits)

def rule_3(i, j, rho, V, S, num_digits):
    if(num_digits == -1):
        V[i-1][j-1].value + S[i-1][j-1]
    return round(V[i-1][j-1].value + S[i-1][j-1], num_digits)