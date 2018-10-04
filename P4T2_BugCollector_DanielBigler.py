# Calculate amount of bugs collected over five days
# 10-4-18
# CTI-110 P4T2 - Bug Collector
# Daniel Bigler
#

def main():
    #set total to zero
    bug_total = 0
    #set up how many days, continue to add to total every day
    for day in range(1,6):
        print("How many bugs were collected on day", day)
        bugs_collected = int(input())
        bug_total = bug_total + bugs_collected
    #finished math, display total
    print("You colledcted", bug_total, "over five days")
    
main()
