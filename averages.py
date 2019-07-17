ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
agesSum = sum(ages)
agesAverage = agesSum / len(ages)
print("The average of the ages provided is " + str(agesAverage) + ".")

ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
total = 0
for i in range(len(ages)):
    total = total + ages[i]
agesAverage = total / len(ages)
print("The average of the ages provided is " + str(agesAverage) + ".")
