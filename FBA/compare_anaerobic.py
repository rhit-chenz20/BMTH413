import pandas as pd

file_path = "msb201165-s2.xls"

df = pd.read_excel(file_path, sheet_name="Table 1", header=None, skiprows=2)

column_a = df.iloc[:, 0]
column_bf = df.iloc[:, 57]

essential = column_a[column_bf == "E"]
non_e = column_a[column_bf == "N"]

# print(essential)
# print(non_e)

print(column_a)

essential_com = "result_single_209_egenes_found_no_oxygen.csv"

essential_com = pd.read_csv(essential_com,skiprows=1).iloc[:, 1]
essential_com.loc[len(essential_com.index)] = "b0003"

# print(essential_com)

print(essential_com)
com_result = essential_com[essential_com.isin(column_a)]

true_p = essential_com[essential_com.isin(essential)]
num_tp = len(true_p)

false_p = essential_com[essential_com.isin(non_e)]
num_fp = len(false_p)



print(com_result)
# print(false_p)



