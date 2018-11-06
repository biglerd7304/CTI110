# Determine if entered number is prime
# 11-1-18
# CTI-110 P5HW1 - Prime Numbers
# Daniel Bigler
#
import math
def main():
    #tn is the input test number
    tn = int(input("Enter a number to see if it is prime: "))
    #calls is_prime, status is equal to it
    status = is_prime(tn)
    #if status is true the it prints it's prime
    if (status):
        print("number is prime")
    else:
        print("number isn't prime")
def is_prime(tn):
    status = False
    #0,1,and negative numbers aren't prime
    if(tn <=1):
        status = False
    #2 and 3 are prime
    elif(tn<=3):
        status = True
    #if greater than three go to checkNum
    else:
        status = checkNum(tn)
    return status
def checkNum(tn):
    status = True
    #checks if it can be evenly divided from
    #2 to the square root of the input number + 1
    for i in range(2,int(math.sqrt(tn)+1)):
        if(tn%i==0):
            status = False
    return status
main()
