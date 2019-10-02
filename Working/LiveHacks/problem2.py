'''
Name: How Much chicken does everyone get?

Purpose:
 This code tells you how many pieces of chicken each student gets and
how many pieces of chicken Mr Fabroa gets.

Author: Andrew Jiang

Date: Wednesday October 2nd 2019
'''
# get amount of chicken from user
chicken = float(input("Enter the amount of chicken pieces "))
# get amount of students that tare eating chickent
students = float(input("Enter the number of students: "))

# compute how much chicken each student gets
chicken_per_student = chicken / students

# compute how much chicken mr fabroa gets
chicken_for_MrFabroa = chicken % students

# show how much chicken each student gets and how much chicken Mr Fabroa gets
print(chicken_per_student)
print(chicken_for_MrFabroa)
