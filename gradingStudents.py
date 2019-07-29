#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(0, len(grades)):
        if grades[i] < 38 or grades[i] > 99:
            continue

        rem=grades [i] % 5
        if rem >= 3:
            tmp=grades[i] + (5 - rem)
            grades[i]=tmp
    return grades
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#HackerLand University has the following grading policy:
#Every student receives a in the inclusive range from 0 to 100.
#Any less than 40 is a failing grade.
#Sam is a professor at the university and likes to round each student's according to these rules:
#If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
#If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
#For example, grade=84 will be rounded to 85 but grade=29 will not be rounded because the rounding would result in a number that is less than 40.
#Given the initial value of for each of Sam's students, write code to automate the rounding process. For each , round it according to the rules above and print the result on a new line.
#Input Format
#The first line contains a single integer denoting (the number of students).
#Each line i of the n subsequent lines contains a single integer, grade[i], denoting student 's grade.
#Constraints 1 <= n <=60 ; 0<= grade[i] <=100
#Output Format
#For each of the grades, print the rounded grade on a new line.
