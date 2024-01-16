import math

def calculate_unique_pairs_count(n):
    if n < 2:
        return 0
    return math.factorial(n) // (2 * math.factorial(n - 2))

# Replace 'n' with the actual number of elements in your list
n = 44  # Example value

f1 = [0 ,2, 3, 6, 10, 14, 15, 17, 25, 26, 42, 43]
f2 = [1, 9, 11, 18, 20, 22, 28, 33, 41]
f3 = [4, 5, 8, 13, 19, 21, 23, 35, 36, 37, 38, 39]
f4 = [7, 12, 16, 31, 32, 34, 40]
f5 = [24, 27, 29, 30]

n=len(f2)
unique_pairs_count = calculate_unique_pairs_count(n)

print(f"Number of unique pairs for {n} elements: {unique_pairs_count}")

n=len(f3)
unique_pairs_count = calculate_unique_pairs_count(n)

print(f"Number of unique pairs for {n} elements: {unique_pairs_count}")
n=len(f4)
unique_pairs_count = calculate_unique_pairs_count(n)

print(f"Number of unique pairs for {n} elements: {unique_pairs_count}")
n=len(f5)
unique_pairs_count = calculate_unique_pairs_count(n)

print(f"Number of unique pairs for {n} elements: {unique_pairs_count}")