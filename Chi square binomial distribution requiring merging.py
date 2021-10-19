import math
data = []

print("Chi squared test for geometric distribution.")

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
        p = input("Input the probability in decimals")
    return (p)
p = convert_fraction_decimal()
no_trials = int(input("How many trials are run?"))

dif_successes = int(input("How many different numbers of successes are there?"))
noSucesses = []
for i in range (dif_successes):
    noSucesses.append(int(input("Input a number of success")))


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
    expected_frequencies_sum += trialsSuccess
    i+=1
    print("i", i)
    print("no_Success", noSucesses[i])
else:
    j = noSucesses[i]-1
    while grand_total*comb(no_trials, j)*(p**j)*((1-p)**(n-j)) < 5:
        j-=1
    else:    
        final = (1-expected_frequencies_sum)*grand_total
        expected_frequencies.append(final)

"""
#generating expected frequencies
expected_frequencies = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(array_of_row_sum[i]*array_of_column_sum[j]/grand_total)
    expected_frequencies.append(row)
"""

print("expected frequencies")
print (expected_frequencies)
"""
for r in expected_frequencies:
    for c in r:
        print(c,end = " ")
    print()
"""
#chi_squared array
chi_squared_terms= []
for i in range(rows):
    row = []
    for j in range(columns):
        print("i is ", i, "j is ", j)
        print (data[i][j])
        row.append((data[i][j]-expected_frequencies[j])**2/expected_frequencies[j])
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

print("chi squared is", chi_squared, "and the number of degrees of freedom is", (columns-1),".")
