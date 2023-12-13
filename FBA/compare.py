import pandas as pd

# Specify the file path
file_path = "msb201165-s2.xls"  # Make sure the file extension is correct (xlsx or xls)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path, sheet_name="Table 13", header=None, skiprows=3)

column_f = df.iloc[3:, 7]  # Column F (0-based index)
column_g = df.iloc[3:, 8]  # ColumnI (0-based index)
# Extract column F and column G starting from row 4
column_h = df.iloc[3:, 7]  # Column F (0-based index)
column_i = df.iloc[3:, 8]  # ColumnI (0-based index)
column_j = df.iloc[3:, 9]  # Column F (0-based index)
column_k = df.iloc[3:, 10]  # ColumnI (0-based index)

column_l = df.iloc[3:, 11]  # Column F (0-based index)
column_m = df.iloc[3:, 12]  # ColumnI (0-based index)


# Filter rows where column G is "Yes"
filtered_data = column_h[column_i == "Yes"]
filtered_data_2 = column_j[column_k == "Yes"]
filtered_data_3 = column_l[column_m == "Yes"]
filtered_data_4 = column_f[column_g == "Yes"]


glucose_essential =  pd.concat([filtered_data, filtered_data_2, filtered_data_4], axis=0, ignore_index=True)
glycerol_essential =  pd.concat([filtered_data, filtered_data_3, filtered_data_4], axis=0, ignore_index=True)


glycerol_essential = glycerol_essential.reset_index(drop=True)

# Print or process the filtered data
print(glucose_essential)
# print(glycerol_essential)



# Specify the file path
file_path = "result_single_216_egenes_found.csv"

file_path1 = "result_single_209_egenes_found_no_oxygen.csv"

# Read column B, skip the first row
file_path = pd.read_csv(file_path,skiprows=1).iloc[:, 1]
file_path1 = pd.read_csv(file_path1,skiprows=1).iloc[:, 1]

positive = file_path[file_path.isin(file_path1)]
print(positive)
print(len(positive)/len(file_path))

