#write a program to find the reverse of the given number
'''num=int(input("enter a number:"))
rev=0
while num>0:
    rev=rev*10+num%10;
    num//=10
print("reverse number is",rev)'''

def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

def ispalindrome(num):
    return num==reverse(num)

print(reverse(123))
<<<<<<< HEAD
print(ispalindrome(1235))
=======
print(ispalindrome(1234))
>>>>>>> 105dbd1ad10ee4857bc54a538ccf4dd3905aa1af

print(reverse(121))
print(ispalindrome(121))

def getpalindromes(start,end):
    res=""
    for i in range(1,end+1):
        if ispalindrome(i):
            res=res+str(i)+","
    return res

print(getpalindromes(1,10000))
        



    
