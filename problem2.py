'''
Name: The distance tracker

Purpose:
to  compute and output the number of days it took to pass 100 km  and average
distance driven per day as well as the number of days it took to pass 100 km.


Author: Andrew Jiang

Date: Wednesday December 9th 2019
'''
# find how much is travelled each day
travelled = array(input("Please enter how much travelled today: "))
totaltravelled = 0
# use a while loop to add the numbers in

while totaltravelled <= 99:
    totaltravelled = totaltravelled + travelled

while totaltravelled > 100:
    print("you have travelled 100 Km congrats")
