from dp_func import calculate_S_matrix, align_two_sequence
import csv

rho_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
rho_values = [0.3]
num_digits = 4

f = open("prot_data.txt", "r")
protein_eigen_value = []
for x in f:
    li = x.split(': ')[1].split(', ')
    li = [float(idx) for idx in li[:len(li)-1]]
    protein_eigen_value.append(li)
f.close()

f = open("dna_data.txt", "r")
seq_data = []
for x in f:
    li = [*x]
    seq_data.append(li[:len(li)-1])
f.close()
test = 3
is_test = False

for rho in rho_values:
    f = open("alignment_data_rho_"+str(rho)+"_2_t.txt", "w")
    csvfile = open("scores_rho_"+str(rho)+"_2_t.csv", 'w', newline='')
    csvwriter = csv.writer(csvfile)
    # header = []
    # csvwriter.writerow(header)
    num = 0
    for i, prot1 in enumerate(protein_eigen_value):
        if(i>test and is_test):
            break
        f.write("seq "+ str(i+1))
        f.write("\n")
        r = []
        for j in range(len(protein_eigen_value)):
            if(j>test and is_test):
                break
            # if(j!=i):
            prot2 = seq_data[j]
            num+=1
            if(num%100==0):
                print(str(num)+" seq is compared")
            ([a1, a2], score) = align_two_sequence(list(range(1, len(prot1)+1)), list(range(1, len(prot2)+1)), rho, num_digits, protein_eigen_value[i], protein_eigen_value[j])
            f.write(str(i+1)+"+"+str(j+1)+ " score: " + str(score) +"\n")
            f.write(a1+"\n")
            f.write(a2+"\n")
            r.append(score)
            # else:
            #     r.append('')
        csvwriter.writerow(r)

f.close()
csvfile.close()