# Calculate percentage of Males and Females in a group
# 9-6-18
# CTI-110 P2HW2 - Male Female Percentage
# Daniel Bigler
#


# enter the number of males
total_males = float( input('Enter the number of males in the group: '))

# enter the number of females
total_females = float( input('Enter the number of females: '))

# add togther to get total number of people
total_people = total_males + total_females

# males divided by total to get percent
percent_males = (total_males / total_people) * 100

# females divided by total to get percent
percent_females = (total_females / total_people) * 100

#display results of math
print('The percent of males is ', format (percent_males, ',.1f'), '%')
print('The percent of females is ', format (percent_females, ',.1f'), '%')
