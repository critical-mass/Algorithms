array = [2, 3, 7, 8, 10]

multiplication_table = []
for num1 in array:
    row = []
    for num2 in array:
        row.append(num1 * num2)
    multiplication_table.append(row)

for row in multiplication_table:
    print(row)
