data = []

columns = int(input("How many columns are there?"))
rows = int(input("How many rows are there?"))
array_of_row_sum = []
array_of_column_sum =[]
grand_total = 0

#initialising array for column restraints
for n in range(columns):
    array_of_column_sum.append(0)

#initialising the observed data and restraints
for i in range(rows):
    row = []
    row_sum = 0
    for j in range(columns):
        #generating data matrix
        print("Input a the value with the place (", i+1 ,",", j+1 ,") in the data.")
        value_at_place = int(input())
        row.append(value_at_place)

        #calculating restraints
        row_sum += value_at_place
        grand_total += value_at_place
        array_of_column_sum[j] += value_at_place

    array_of_row_sum.append(row_sum) #calculates restraints for each row
    data.append(row)

#check
print (data)
print(array_of_row_sum)
print(array_of_column_sum)
print("Grand total is", grand_total)

print("The data given")
for r in data:
    for c in r:
        print(c,end = " ")
    print()

#generating expected frequencies
expected_frequencies = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(array_of_row_sum[i]*array_of_column_sum[j]/grand_total)
    expected_frequencies.append(row)

print("expected frequencies")
for r in expected_frequencies:
    for c in r:
        print(c,end = " ")
    print()

#difference array
difference_array= []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append((data[i][j]-expected_frequencies[i][j]))
    difference_array.append(row)

print("difference")
for r in difference_array:
    for c in r:
        print(c,end = " ")
    print()

#chi_squared array
chi_squared_terms= []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append((data[i][j]-expected_frequencies[i][j])**2/expected_frequencies[i][j])
    chi_squared_terms.append(row)

print("Chi-squared terms")
for r in chi_squared_terms:
    for c in r:
        print(c,end = " ")
    print()

chi_squared = 0
#calculating chi squared
for i in range(rows):
    for j in range(columns):
        chi_squared += chi_squared_terms[i][j]

print("chi squared is", chi_squared, "and the number of degrees of freedom is", rows*columns-(rows+columns-1),".")

