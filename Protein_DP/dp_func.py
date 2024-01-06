
class dp_cell():
    def __init__(self, i, j, null_cell = 0):
        self.value = 0
        self.index = (i, j)
        self.parent = []
        self.is_null = null_cell
    
    def __repr__(self):
        if(self.is_null == 1):
            return "--"
        return str(self.index) + " " + str(self.value)

def calculate_S_matrix(pro1_eigen_v, pro2_eigen_v, num_digits):
    result = []
    for i, v1 in enumerate(pro1_eigen_v):
        r1 = []
        for j, v2 in enumerate(pro2_eigen_v):
            r1.append(calculate_S_i_j(v1, v2, num_digits))
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

def align_two_sequence(seq1, seq2, rho, num_digits, eigen1=None, eigen2=None, s_matrix = None):
    if(not s_matrix):
        s_matrix = calculate_S_matrix(eigen1, eigen2, num_digits)  
        # print("s matrix calculated")
    dp_table = create_dp_table(seq1, seq2)
    initiate_dp_table(dp_table, rho, num_digits)
    build_dp_table(dp_table, rho, s_matrix, num_digits)
    # print("dp table built")
    end_cell = dp_table[len(dp_table)-1][len(dp_table[0])-1]
    score = end_cell.value
    trace = []
    back_trace(end_cell, trace, debug = 0)
    # print("trace completed")
    seq1.reverse()
    seq2.reverse()
    alignment = produce_alignment(trace, seq1, seq2)
    align =  format_alignment(alignment)
    return (align, score)
    
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
  
def create_dp_table(seq1, seq2):
    dp_table = []
    for i in range(len(seq1)+1):
        dp_table.append([dp_cell(i, j) for j in range(len(seq2)+1)])
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

def back_trace(cell:dp_cell, trace_result:list, debug = 0):
    if(debug == 1):
        for x in trace_result:
            x.append(str(cell.index) + " " + str(cell.value) + "\n") 
        if (not cell.parent):
            return trace_result
        for p in cell.parent:
            result = back_trace(p, trace_result, debug)
        return result
    else:
        # for x in trace_result:
        trace_result.append(cell) 
        if (not cell.parent):
            return 
        if(len(trace_result)%100000==0):
            print("proceeding with tracing; finished "+str(len(trace_result[0])))
        # for p in cell.parent:
        back_trace(cell.parent[0], trace_result, debug)
        
def produce_alignment(trace_list, align1, align2):
    result = [[], []]
    ind1 = 0
    ind2 = 0
    null_sym = '-'
    for i in range(len(trace_list)-1):
        cell1 = trace_list[i]
        cell2 = trace_list[i+1]
        if(cell1.index[0] != cell2.index[0] and cell1.index[1] != cell2.index[1]):
            result[0].append(align1[ind1])
            result[1].append(align2[ind2])
            ind2 += 1
            ind1 += 1
        elif(cell1.index[0] == cell2.index[0]):
            result[0].append(null_sym)
            result[1].append(align2[ind2])
            ind2 += 1
        elif(cell1.index[1] == cell2.index[1]):
            result[0].append(align1[ind1])
            result[1].append(null_sym)
            ind1 += 1
    return result

def format_alignment(align):
    align[0].reverse()
    align[1].reverse()
    ali1 = []
    ali2 = []
    for x in align[0]:
        if(x=='-'):
            ali1.append('---')
        elif x<10:
            ali1.append(str(x)+"  ")
        elif x<100:
            ali1.append(str(x)+" ")
        else:
            ali1.append(str(x))
    for x in align[1]:
        if(x=='-'):
            ali2.append('---')
        elif x<10:
            ali2.append(str(x)+"  ")
        elif x<100:
            ali2.append(str(x)+" ")
        else:
            ali2.append(str(x))
    s1 = " ".join(ali1)
    s2 = " ".join(ali2)
    return [s1, s2]
    