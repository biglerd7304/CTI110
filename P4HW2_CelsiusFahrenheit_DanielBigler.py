# table of Celsius temp. 0-20, and their fahrenheit equivalents
# 10-9-18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Daniel Bigler
#

def main ():
    #title
    print("Celsius","\t", "Fahrenheit")
    #numbers, math, and format
    for temp in range(0,21):
        fah = (temp * (9/5)) + 32
        print(temp, "\t\t", format (fah, ',.1f'))
main()
