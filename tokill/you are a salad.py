def calculateTotalSum(*arguments):
    totalSum = 0
    for number in arguments:
        totalSum += number
    return totalSum


# function call
print(type(calculateTotalSum(5, 4, 3, 2, 1)))
print(calculateTotalSum(5, 4, 3, 2, 1))
