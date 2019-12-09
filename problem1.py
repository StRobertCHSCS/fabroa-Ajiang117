'''
Name: The heating days tracker

Purpose:
to find the number of heating days in a amount of days

Author: Andrew Jiang

Date: Wednesday December 9th 2019
'''
# get the number of days from the user
numofdays = str(input("how many days would you like to track: "))

# get the temperatures of the amount of days
tempofdays = str(input("what are the heats for those days :"))
numofheatdays = 0
# find how many of the days are heating days
for tempofdays in range(15):
    numofheatdays = numofheatdays + 1

# print the number of heating days
print("Their are this many heating days: " + str(numofheatdays))
