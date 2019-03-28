# Determine if entered number is prime
# 10-25-18
# CTI-110 P5HW1 - Prime Numbers
# Daniel Bigler
#

def main():
    #tn is the input test number
    tn = int(input("Enter a number to see if it is prime: "))
    if tn == 1:
        print(tn, "isn't prime or composite")
    elif tn == 0:
        print(tn, "isn't prime or composite")
    elif tn < 0:
        print(tn, "negative numbers aren't prime")
    else:
        is_prime(tn)
def is_prime(tn):
    #take a number and see what it's divisable by, if it can't be
    #divided then it increases by one and continues. Once it can be
    #evenly divided it checks what it is divided by and if it matches
    #the input number(makes it all the way to initial number)
    #then it is prime, if it's divisable by and stops at a smaller
    #number then it isn't prime
    dividing_number = 1
    X = 1
    while X > 0:
        dividing_number = dividing_number + 1
        X = (tn % dividing_number)
    if dividing_number == tn:
        print(tn, "is prime")
    else:
        print(tn, "isn't a prime number")
main()
