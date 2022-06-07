def fact(num):
 f=1
 for i in range(1,num+1):
    f=f*i
 print("The Factorial No of",num," value is",f)
def stringreverse(str):
 new=str[::-1]
 print("the reverse string of ",str, "is",new)
def prime():
 print("To find the prime number between the numbers")
 lower = int(input("enter the lower limit:"))
 upper = int(input("enter the upper limit:"))
 print("Prime numbers between", lower, "and", upper, "are:")
 for num in range(lower, upper + 1):
 # all prime numbers are greater than 1
    if num > 1:
      for i in range(2, num):
            if (num % i) == 0:
                break
    else:
        print(num)
def findstring():
 str=input("enter to find the value:")
 message = 'Python is a fun programming language'
 ss = message.find(str)
 print(ss)
fact(5)
stringreverse("hello")
prime()
findstring()