""" Question 1: 1)	Write a program which will find numbers which are divisible by 7
    but not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained
    should be printed in a comma-separated sequence on a single line."""

a = []

for i in range(2000,3200):
    if(i % 7 ==0) and (i % 5 != 0):
        a.append(str(i))

print(','.join(a))