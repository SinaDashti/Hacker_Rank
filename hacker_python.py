################################################################################
                                      #Q
################################################################################
# Read an integer N.
# Without using any string methods, try to print the following:
# 123...N
# Note that "..." represents the values in between.
# Input Format
# The first line contains an integer N.
# Output Format
# Output the answer as explained in the task.
# Sample Input
# 3
# Sample Output
# 123
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     n = int(input())
#     i = 1
#     while i<=n:
#         print(i,end='')
#         i+=1
################################################################################
# print(*range(1, int(input())+1), sep='')
################################################################################
                                      #Q
################################################################################
# Let's learn about list comprehensions! You are given three integers X, Y and  Z
# representing the dimensions of a cuboid along with an integer N.
# You have to print a list of all possible coordinates given by (i, j, k) on a 3D
# grid  where the sum of i + j+ k is not equal to N. Here, 0<=i<=X;0<=j<=Y;0<=k<=Z
#
# Input Format
# Four integers X,Y,Z and N each on four separate lines, respectively.
# Constraints
# Print the list in lexicographic increasing order.
# Sample Input
# 1
# 1
# 1
# 2
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
# Concept
# You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. This example might help.
# Example: You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.
# python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) ar = [] p = 0 for i in range ( x + 1 ) : for j in range( y + 1): if i+j != n: ar.append([]) ar[p] = [ i , j ] p+=1 print ar
# Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:
# python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
# Sample Input
# 2
# 2
# 2
# 2
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0],
# [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1],
# [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     print (
#         [ [ i, j, k] for i in range( x + 1)
#                     for j in range( y + 1)
#                     for k in range( z + 1)
#                     if ( ( i + j + k) != n )]
#     )
# other way of getting input
# x,y,z,n = [input() for i in range(4)]
# x, y, z, n = (int(input()) for _ in range(4))
################################################################################
                                      #Q
################################################################################
# Given the participants' score sheet for your University Sports Day, you are
# required to find the runner-up score. You are given n scores. Store them in a
# list and find the score of the runner-up.
# Input Format
# The first line contains n. The second line contains an array A[] of n integers
# each separated by a space.
# Constraints:
# 2<=n<=10
# -100<=A[]<=-100
# Output Format
# Print the runner-up score.
# Sample Input
# 5
# 2 3 6 6 5
# Sample Output
# 5
# Explanation
# Given list is [2,3,6,6,5] . The maximum score is 6, , second maximum is 5.
# Hence, we print  5 as the runner-up score.
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr = list(set(arr))
#     arr.pop(arr.index(max(arr)))
#     print(max(arr))
################################################################################
# i = int(input())
# lis = list(map(int,raw_input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print max(lis)
################################################################################
                                      #Q
################################################################################
# nested-list-English
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     li = []
#     out = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         li.append([name, score])
#
# li.sort(key=lambda li:li[1])
# first_min = li[0][1]
# new = li[1:]
# for student, mark in new:
#     if mark == first_min:
#         continue
#     elif mark > first_min:
#         idx = new.index([student,mark])
#         out.append(student)
#         if idx < len(new) - 1:
#             if new[idx][1] < new[idx + 1][1]:
#                 break
# out.sort()
# for item in out:
#     print(item)

# print('\n'.join(a for a in sorted(out)))
################################################################################
# out.sort()
#
# sorted(out)
# ['a','b','c']
################################################################################
# n = int(input())
# marksheet = [[input(), float(input())] for _ in range(n)]
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
################################################################################
################################################################################
                                      #Q
################################################################################
# finding-the-percentage-English
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
# print('%.2f' %(sum(student_marks[query_name])/3))
################################################################################
# query_scores = student_marks[query_name]
# print('{0:.2}'.format(sum(student_marks[query_name])/(len(query_scores))))
################################################################################
                                      #Q
################################################################################
# python-lists-English
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     N = int(input())
#     li = []
#     for _ in range(N):
#         name, *elm = input().split()
#         if name != "print" :
#             name += "("+ ",".join(elm) +")"
#             eval("li."+name)
#         else:
#             print(li)
#
# if __name__ == '__main__':
#     N = int(input())
#     li = []
#     for _ in range(N):
#         name, *elm = input().split()
#         if name != "print" :
#             eval('li.{0}{1}'.format(name,tuple(map(int,elm))))
#         else:
#             print(li)
################################################################################
                                      #Q
################################################################################
# python-tuples-English
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     print(hash(integer_list))
################################################################################
                                      #Q
################################################################################
# decorators-2-name-directory-English
################################################################################
                                     #A
################################################################################
# def person_lister(f):
#     def inner(people):
#         # complete the function
#         return map(f, sorted(people, key=lambda x: int(x[2])))
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')
################################################################################
# decorators example
# def my_decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper
#
# def hi_arash():
#     print("hi Arash!")
#
# the decoration happend here, passing an existing function and reassigning it
# to itself. decorator wrap a function and allow other functional code around it.
# hi_arash = my_decorator(hi_arash)
#
# >>> hi_arash
# <function __main__.my_decorator.<locals>.wrapper()>
#
# >>> hi_arash()
# before function
# hi Arash!
# after function
################################################################################
                                      #Q
################################################################################
# itertools-permutations-English
################################################################################
                                     #A
################################################################################
# from itertools import permutations
# p = input().split()
# print('\n'.join(map(lambda i: ''.join(i),permutations(sorted(p[0]),int(p[1])))))
# print(*[''.join(i) for i in permutations(sorted(p[0]),int(p[1]))],sep='\n')
################################################################################
                                      #Q
################################################################################
# itertools-combinations-English
################################################################################
                                     #A
################################################################################
# from itertools import combinations
# p = input().split()
# print(*[''.join(item) for lis in [combinations(sorted(p[0]),i)
#                                   for i in range(1,int(p[1])+1)]
#                                   for item in lis],sep='\n')

# more readable
# l = [combinations(sorted(p[0]),i) for i in range(1,int(p[1])+1)]
# print(*[''.join(item) for lis in l for item in lis],sep='\n')
################################################################################
                                      #Q
################################################################################
# itertools-combinations-with-replacement-English
################################################################################
                                     #A
################################################################################
# from itertools import combinations_with_replacement
# p = input().split()
# print(*[''.join(i) for i in combinations_with_replacement(sorted(p[0]),int(p[1]))],sep = '\n')
################################################################################
                                      #Q
################################################################################
# compress-the-string-English
################################################################################
                                     #A
################################################################################
# from itertools import groupby
# p = input()
# groups = [list(g) for k, g in groupby(p)]
# keys = [k for k, g in groupby(p)]
# gr_len = [len(i) for i in groups]
# print(*tuple(zip(gr_len,map(int,keys))))
#
# print(*tuple(zip(list(map(len,(list(g) for k, g in groupby(p)))),map(int,[k for k, g in groupby(p)]))))
################################################################################
# print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
# print(' '.join(('({}, {})'.format(len(list(g)), x) for x,g in groupby(input()))))
################################################################################
################################################################################
                                      #Q
################################################################################
# iterables-and-iterators-English
################################################################################
################################################################################
                                     #A
################################################################################
# import itertools as it
# N = int(input())
# li = input().split()
# K = int(input())
# C = list(it.combinations(li, K))
# print('%.3f' % float(len([i for i in C if 'a' in i])/len(C)))
################################################################################
# from itertools import combinations
# N = int(input())
# L = input().split()
# K = int(input())
# C = list(combinations(L, K))
# F = filter(lambda c: 'a' in c, C)
# print("{0:.3}".format(len(list(F))/len(C)))
################################################################################
                                      #Q
################################################################################
# swap-case-English
################################################################################
################################################################################
                                     #A
################################################################################
# def swap_case(s):
#     return (''.join([i.lower() if i.isupper() else i.upper() for i in s]))
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
#
# print(*map(lambda ch : ch.lower() if ch.isupper() else ch.upper(), input()), sep="")
################################################################################
                                      #Q
################################################################################
# 
################################################################################
################################################################################
                                     #A
################################################################################
