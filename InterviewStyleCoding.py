import random

#variables
randomNums = []
numOfNums = 0

#while loop to make sure that only 50 numbers are generated at a time
while numOfNums != 50:

    #creation of random number which is added to the array each time
    randomNum = random.randint(1,10)

    #if the number generated is equal to 7 the numbe is added and then the whole array is printed and then 
    #overwritten to be empty again and then added to
    if randomNum == 7:
        randomNums.append(randomNum)
        print(randomNums)
        randomNums = []

    #if the number is not 7, then the random number generated is just added to the array
    else:
        randomNums.append(randomNum)

    #counter is incremented to make sure only 50 numbers are generated
    numOfNums+=1

#final array is printed to ensure that all numbers are printed regardless on whether there is a 7 or not
print(randomNums)