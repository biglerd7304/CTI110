# tuition increase
# 10-9-18
# CTI-110 P4HW3 - Tuition Increase
# Daniel Bigler
#

def main ():
    #tuition is variable
    tuition = 8000
    #start loop
    for year in range (1,6):
        #do math
        tuition = tuition * 1.03
        #print year number and amount
        print ("Year", year, "\t", format (tuition, ',.2f'))
main()
