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
 
dif_trials = int(input("How many different numbers of trials are there?"))
noTrials = []
for i in range (dif_trials):
    noTrials.append(input("Input a number of trials"))


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

#generating expected frequencies from geometric distribution
expected_frequencies = []
i = 0 
while i < (dif_trials-1):
    print(((1-p)**(int(noTrials[i])-1))*p*grand_total)
    expected_frequencies.append(((1-p)**(int(noTrials[i])-1))*p*grand_total)
    i+=1
    print("i", i)
    print("no_trials", noTrials[i])
#final one is for when the number of trials is noTrials[last]+
else:
    print((((1-p)**(int(noTrials[i])-1)))*grand_total)
    expected_frequencies.append(((1-p)**(int(noTrials[i])-1))*grand_total)

print("expected frequencies")
print (expected_frequencies)

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
