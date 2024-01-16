from plot import get_data

data, index = get_data()

f1 = [0 ,2, 3, 6 , 10, 14, 15, 17, 25, 26, 42, 43]
f2 = [1, 9, 11, 18, 20, 22, 28, 33, 41]
f3 = [4, 5, 8, 13, 19, 21, 23, 35, 36, 37, 38, 39]
f4 = [7, 12, 16, 31, 32, 34, 40]
f5 = [24, 27, 29, 30]
true_list = [f1, f2, f3, f4, f5]

total_num_pairs = 946
pos_num_pairs = 195
neg_num_pairs = total_num_pairs - pos_num_pairs
pos_num_pairs_f1 = 66
len_f1 = 12
pos_num_pairs_f2 = 36
len_f2 = 9
pos_num_pairs_f3 = 66
len_f3 = 12
pos_num_pairs_f4 = 21
len_f4 = 7
pos_num_pairs_f5 = 6
len_f5 = 4

def test_pair_in_same_list(pair, lists):
    for lst in lists:
        if pair[0] in lst and pair[1] in lst:
            return True
    return False

def calculate_tpr_and_fpr(clusters):
    clustered_pairs = []
    for cluster in clusters:
        for i in range(len(cluster)):
            for j in range(i + 1, len(cluster)):
                pair = (cluster[i], cluster[j])
                clustered_pairs.append(pair)

    true_num = 0
    false_num = 0
    false_pairs = []
    for p in clustered_pairs:
        if(test_pair_in_same_list(p, true_list)):
            true_num+=1
        else:
            false_num += 1
            false_pairs.append(p)
    print(false_pairs)
    return (true_num/pos_num_pairs, false_num /neg_num_pairs)