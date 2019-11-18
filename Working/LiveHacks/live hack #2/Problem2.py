'''
Name : The class bonus detector

Purpose:
 to see if the classroom gets a bonus for improving the average

Author: Andrew Jiang

Date: Monday November 18th 2019
'''

# get midterm average
midterm = float(input("Enter the midterm average:"))
# get final average
final = float(input("Enter the midterm average:"))

# find the difference between the midterm and the final averages
change = (final - midterm)

# find out how much money is earned
if change > 10 amtearned = 600
if change < 10 and change > 5 amtearned = 300
if change < 5 and change > 1 amtearned = 100
if change < 1 amtearned = 0


# print how much is earned by the class
if change > 10 print("Congratualtions, the cash bonus is $" + str(amtearned))
if change < 1 print("Sorry, no cash bonus for your class")
