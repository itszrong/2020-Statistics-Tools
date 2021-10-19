import math
print(math.factorial(4))



"""dif_trials = 5
noTrials = [1,2,3,4,7]
expected_frequencies = []
p = 1/3

i=0
j=0
grand_total = 52
while i < (dif_trials-1):
    print(((1-p)**(int(noTrials[i])-1))*p*grand_total)
    expected_frequencies.append(((1-p)**(int(noTrials[i])-1))*p*grand_total)
    i+=1
    print("i", i)
    print("no_trials", noTrials[i])
    j = int(noTrials[i])-1
else:
    while ((1-p)**(j))*grand_total < 5 :
        j-=1
        print(((1-p)**(j))*grand_total)
        print("j is number of failures so number of trials > j =", j)
    else:
        print (((1-p)**j)*grand_total)
        expected_frequencies.append(((1-p)**j)*grand_total)

print("expected frequencies", expected_frequencies)"""