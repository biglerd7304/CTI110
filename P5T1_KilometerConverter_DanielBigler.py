# kilometer converter into miles
# 10-23-18
# CTI-110 P5T1_KilometerConverter 
# Daniel Bigler
#

# main gets distance and calls show_miles to convert
Conversion_factor = 0.6214

def main():
    #get distance
    Kilometers = float(input("Enter distance in kilometers: "))
    #display and convert
    show_miles(Kilometers)
#converts km from kilometers to miles and displays result
def show_miles(km):
    #calculate
    Miles = km * Conversion_factor
    #Display miles
    print(km, "kilometers is equal to", format(Miles, ".4f"), "miles")
#call main function
main()
