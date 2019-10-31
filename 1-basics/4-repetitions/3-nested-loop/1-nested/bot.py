print("How many rows should I have")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

print("\n""Here I go:""\n")

for number_rows in range(0, rows, 1):
    for number_columns in range(0, columns, 1):
        print(":-)", end="")
    print()

print("\n""Done!")