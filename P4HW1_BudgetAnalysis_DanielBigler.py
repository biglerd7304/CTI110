# deduct expences from a budget
# 10-4-18
# CTI-110 P4HW1 - Budget Analysis
# Daniel Bigler
#

def main():
    total = 0
    Continue = "yes";
    #enter budget
    print("What is your budget for month")
    budget = int(input())
    #start loop while continue equals "yes"
    while Continue == "yes":
        #enter expence and do math
        print("Input an expence amount")
        Spent = int(input())
        total = budget - Spent
        budget = total
        #want to continue loop or are you done
        print("Do you have any other expences, yes/no")
        Continue = input()
    #display amount and a message
    if total > 0:
        print("you have", total, "left in your budget.")
    elif total < 0:
        print("You spent", -total, "too much!")
    elif total == 0:
        print("You have net zero, right on budget.")
    else:
        print("?")

main()
