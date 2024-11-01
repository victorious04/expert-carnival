factors = []
usernum = int(input("Please enter a number: "))

for x in range (1, usernum+1):
    if usernum % x == 0:
        factors.append(x)

if len(factors) > 2:
    print(f"the factors of {usernum} are: {factors}")
else:
    print("Prime Number")

    """
    For this program, I thinnk the variable names are appropriate and make sense, making readibility easy for others
    It also is quite simple which makes it easy to follow through for those who may not be experienced in programming
    To improve this code, I think I could include a while loop to check if the user wants to continue entering numbers 
    rather than the program just ending after each number that is entered
    I also think that adding in input validation such as presence checks and integer check could also help the program 
    to be more robust than it is now.
    """