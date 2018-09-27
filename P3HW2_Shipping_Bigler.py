# CTI-110 
# P3HW2 - Shipping Charges 
# Daniel Bigler 
# 9-27-18
#

# input
Weight = int(input('Enter the weight of the package to see the shipping carges: '))
# determine the range for each price
if Weight <= 2:
    print('The shipping charge is $1.50')
elif Weight <= 6:
    print('The shipping charge is $3.00')
elif Weight <= 10:
    print('The shipping charge is 4.00')
else:
    print('The shipping charge is 4.75')
