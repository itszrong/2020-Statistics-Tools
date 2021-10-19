import math
data = []

print("Chi squared test for geometric distribution.")

#to allow for input for probability in either fraction or decimal
def convert_fraction_decimal():
    print("Do you want to input the probability in fractions?")
    fraction_or_not = input()
    if fraction_or_not.lower() == "yes":
        print("This is a fraction to decimal conversion")
        numerator = float(input("Input the numerator"))
        denominator = float(input("Input the denominator"))
        p = numerator/denominator
        print("The probability of success is", p)
    else:
        p = float(input("Input the probability in decimals"))
    return (p)
p = convert_fraction_decimal()
no_trials = int(input("How many trials are run?"))

#generating table and values that need to be calculated
dif_successes = int(input("How many different numbers of successes are there?"))
noSucesses = []
for i in range (dif_successes):
    noSucesses.append(int(input("Input a number of success")))

#intialising size of table for observables
columns = int(input("How many columns are there?"))
rows = int(input("How many rows are there?"))
array_of_row_sum = []
array_of_column_sum =[]
grand_total = 0

#initialising array for column restraints in order to create n dimensional array
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
print("Grand total is", grand_total)

print("The data given")
for r in data:
    for c in r:
        print(c,end = " ")
    print()

#define comb function for binomial coefficient
def comb(n, k):
    coefficient = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return coefficient

#generating expected frequencies from binomial distribution
expected_frequencies = []
i = 0 
trialsSuccess = 0
expected_frequencies_sum = 0
while i < (dif_successes-1):
    trialsSuccess = grand_total*(comb(no_trials, noSucesses[i]))*(p**noSucesses[i])*((1-p)**(n-noSucesses[i]))    
    print (trialsSuccess)
    expected_frequencies.append(trialsSuccess)
    expected_frequencies_sum += trialsSuccess/grand_total
    i+=1
    print("i", i)
    print("no_Success", noSucesses[i])
else:
    j = noSucesses[i]-1
    trialsSuccess = grand_total*comb(no_trials, j)*(p**j)*((1-p)**(n-j))
    print("expected frequencies sum", expected_frequencies_sum)
    final = (1-expected_frequencies_sum)*grand_total
    expected_frequencies.append(final)

print("expected frequencies")
print (expected_frequencies)

#another method to print expected frequencies when its dimensionality is > 1
"""
for r in expected_frequencies:
    for c in r:
        print(c,end = " ")
    print()
"""

#difference array
difference_array= []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append((data[i][j]-expected_frequencies[j]))
    difference_array.append(row)

print("difference")
for r in difference_array:
    for c in r:
        print(c,end = " ")
    print()

#chi squared array and calculations
chi_squared_terms= []
for i in range(rows):
    row = []
    for j in range(columns):
        print("i is ", i, "j is ", j)
        print (data[i][j])
        row.append((data[i][j]-expected_frequencies[j])**2/expected_frequencies[j])
    chi_squared_terms.append(row)

#print chi squared array
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

print("chi squared is", chi_squared, "and the number of degrees of freedom is", (columns-1),".")
