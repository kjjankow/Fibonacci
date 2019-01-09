# Project Euler #2 - Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.



newSum = 0      # Sum starts at 0
origNum = 0     # First num in sequence
nextNum = 1     # Second num in sequence
numCount = 0    # Used for counting iterations
evenTerms = 0   # Used for summing only the even terms


while newSum < 4000000:
        newSum = origNum + nextNum
        origNum = nextNum
        nextNum=newSum
        if newSum > 4000000:
            break
        numCount += 1
        if newSum % 2 == 0:
            evenTerms += newSum
        # print(newSum)
        print(evenTerms)



