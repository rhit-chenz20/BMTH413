import pandas as pd
from copy import deepcopy

# Specify the file path
file_path = "msb201165-s2.xls"  # Make sure the file extension is correct (xlsx or xls)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name="Table 13", header=None, skiprows=3)

# column_f = df.iloc[3:, 7]  # Column F (0-based index)
# column_g = df.iloc[3:, 8]  # ColumnI (0-based index)
# # Extract column F and column G starting from row 4
# column_h = df.iloc[3:, 7]  # Column F (0-based index)
# column_i = df.iloc[3:, 8]  # ColumnI (0-based index)
# column_j = df.iloc[3:, 9]  # Column F (0-based index)
# column_k = df.iloc[3:, 10]  # ColumnI (0-based index)

# column_l = df.iloc[3:, 11]  # Column F (0-based index)
# column_m = df.iloc[3:, 12]  # ColumnI (0-based index)


column_o = df.iloc[:, 14]  # Column F (0-based index)
column_p = df.iloc[:, 15]  # ColumnI (0-based index)
column_q = df.iloc[:, 16]  # Column F (0-based index)
column_r = df.iloc[:, 17]  # ColumnI (0-based index)

column_s = df.iloc[:, 18]  # Column F (0-based index)
column_t = df.iloc[:, 19]  # ColumnI (0-based index)
column_u = df.iloc[:, 20]  # Column F (0-based index)
column_v = df.iloc[:, 21]  # ColumnI (0-based index)

# Filter rows where column G is "Yes"
tp = list(filter(lambda x: isinstance(x,str), column_o))
fp = list(filter(lambda x: isinstance(x,str), column_p))
fn = list(filter(lambda x: isinstance(x,str), column_q))
tn = list(filter(lambda x: isinstance(x,str), column_r))


tp_gly = list(filter(lambda x: isinstance(x,str), column_s))
fp_gly = list(filter(lambda x: isinstance(x,str), column_t))
fn_gly = list(filter(lambda x: isinstance(x,str), column_u))
tn_gly = list(filter(lambda x: isinstance(x,str), column_v))

fp.extend(tn)
glucose_essential_ex =  fp
tp.extend(fn)
glucose_non_essential_ex = tp

fp_gly.extend(tn_gly)
glycerol_essential_ex = fp_gly
tp_gly.extend(fn_gly)
glycerol_non_essential_ex = tp_gly

total = deepcopy(fp)
total.extend(tp)

# Specify the file path
file_path = "result_single_216_egenes_found.csv" # glucose aerobic
# file_path = "result_single_202_egenes_found_glycerol.csv"

# file_path1 = "result_single_209_egenes_found_no_oxygen.csv"

# # Read column B, skip the first row
glucose_essential_com = pd.read_csv(file_path,skiprows=1).iloc[:, 1]
# glycerol_essential_com = pd.read_csv(file_path,skiprows=1).iloc[:, 1]

# positive = file_path[file_path.isin(file_path1)]
# print(positive)
# print(len(positive)/len(file_path))

glucose_essential_com.loc[len(glucose_essential_com.index)] = "b0003"

true_p = glucose_essential_com[glucose_essential_com.isin(glucose_essential_ex)]
num_true_p = len(true_p)


# false_p = glucose_essential_com[not glucose_essential_com.isin(glucose_essential_ex)]
# print(true_p)
# print(glucose_essential_com)

print("true pos ratio",num_true_p/(len(glucose_essential_com)))

# print(false_p)
print("false pos ratio",(len(glucose_essential_com)-num_true_p)/(len(glucose_essential_com)))

true_p = list(true_p)
# print(len(total))
non_essential_com = list(filter(lambda x: x not in true_p, total))

# print(len(non_essential_com))

true_false = list(filter(lambda x: x in glucose_non_essential_ex,non_essential_com))
num_true_false = len(true_false)

print("true neg ratio",num_true_false/(len(non_essential_com)))
print("false neg ratio",1-num_true_false/(len(non_essential_com)))

print("accurate ratio", (num_true_false+num_true_p)/len(total))

print(len(glucose_essential_com)-num_true_p, len(non_essential_com)-num_true_false)
print(num_true_p/len(total), (len(glucose_essential_com)-num_true_p)/len(total), num_true_false/len(total), (len(non_essential_com)-num_true_false)/len(total))