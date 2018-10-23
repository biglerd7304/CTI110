# converts feet to inches
# 10-23-18
# CTI-110 P5T2_FeetToInches 
# Daniel Bigler
#

#constant for inches per foot
Inches_per_foot = 12
#main function
def main():
    #get number of feet
    feet = int(input("Enter number of feet: "))

    #convert to inches
    print(feet, "feet equals", feet_to_inches(feet), "inches.")

#Coverts feet to inches
def feet_to_inches(feet):
    return feet * Inches_per_foot

#call main function
main()
