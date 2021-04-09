def isHappyNumber(n):
    r = s = 0
    while (n>0):
        r = n%10;
        s = s + (r*r);
        n = n//10;
    return s;
num = int(input("Enter a number: "))
result = num
while (result!=1 and result!=4):
    result = isHappyNumber(result)
if (result == 1):
    print(str(num) + " is a happy number")
elif (result == 4):
    print(str(num) + " is not a happy number")
