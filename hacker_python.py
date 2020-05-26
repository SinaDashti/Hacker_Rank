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
# python-string-split-and-join-English
################################################################################
################################################################################
                                     #A
################################################################################
# def split_and_join(line):
#     # write your code here
#     return ('-'.join(line.split(' ')))
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
################################################################################
                                      #Q
################################################################################
# find-a-string-English
################################################################################
################################################################################
                                     #A
################################################################################
# def count_substring(string, sub_string):
#     return len([i for i in range(len(string)) if string.startswith(sub_string, i)])
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
################################################################################
# string, substring = (input().strip(), input().strip())
# print(sum([ 1 for i in range(len(string)-len(substring)+1) \
#             if string[i:i+len(substring)] == substring]))
################################################################################
# def count_substring(string, sub_string):
#     count=0
#     #print(len(string),len(sub_string))
#     for i in range(0, len(string)-len(sub_string)+1):
#         if string[i] == sub_string[0]:
#             flag=1
#             for j in range (0, len(sub_string)):
#                 if string[i+j] != sub_string[j]:
#                     flag=0
#                     break
#             if flag==1:
#                 count += 1
#     return count
################################################################################
                                      #Q
################################################################################
# string-validators-English
################################################################################
################################################################################
                                     #A
################################################################################
# if __name__ == '__main__':
#     s = input()
#     print(*list(map(lambda x: eval('any(ch.{0} for ch in list(s))'.format(x)),
#     ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()'])), sep='\n')
################################################################################
                                      #Q
################################################################################
# designer-door-mat-English
################################################################################
################################################################################
                                     #A
################################################################################
# N, M = map(int,input().split())
# top = [('.|.'*(2*i - 1)).center(M,'-') for i in range(1,N//2 + 1)]
# print('\n'.join(top)+ '\n' +'WELCOME'.center(M ,'-')+ '\n' + '\n'.join(top[::-1]))
################################################################################
                                      #Q
################################################################################
# python-string-formatting-English
################################################################################
################################################################################
                                     #A
################################################################################
# def print_formatted(n):
#     width = len("{0:b}".format(n))
#     for num in range(1,n+1):
#         for base in 'dXob':
#             print('{0:{width}{base}}'.format(num, base=base, width=width),end = ' ')
#         print('\n', end='')
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
################################################################################
# def print_formatted(n):
#     width = len("{0:b}".format(n))
#     for i in range(1,n+1):
#         print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))
################################################################################
                                      #Q
################################################################################
# alphabet-rangoli-English
################################################################################
################################################################################
                                     #A
################################################################################
# def print_rangoli(size):
#     # your code goes here
#     l = [str(chr(i + 97)) for i in range(size)]
#     down = [l[-1:-(len(l)-i):-1] + l[i:(len(l))]  for i in range(len(l))]
#     for line in down[:-(len(down)):-1]:
#         print('-'.join(line).center(2 * len(down[0]) -1, '-'))
#     for line in down:
#         print('-'.join(line).center(2 * len(down[0]) -1, '-'))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
################################################################################
                                      #Q
################################################################################
# capitalize-English
################################################################################
################################################################################
                                     #A
################################################################################
# def solve(s):
#     return  ' '.join(list(map(lambda x:x.capitalize(),s.split(' '))))
#
# # ' '.join(map(str.capitalize, s.split(' ')))
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
################################################################################
                                      #Q
################################################################################
# itertools-product-English
################################################################################
################################################################################
                                     #A
################################################################################
# import itertools as it
#
# print(*(it.product(map(int,input().split()),map(int,input().split()))))
#
# A, B = [list(map(int, input().split())) for _ in range(2)]
# print(*(it.product(A,B)))
################################################################################
                                      #Q
################################################################################
# collections-counter-English
################################################################################
################################################################################
                                     #A
################################################################################
# from collections import Counter
#
# _, c = input(), Counter(input().split())
# tot = 0
# for _ in range(int(input())):
#     temp = input().split()
#     if c[temp[0]]:
#         tot+= int(temp[1])
#         c[temp[0]]-=1
# print(tot)
# ################################################################################
# from collections import Counter
#
# _, stock = input(), Counter(list(map(int,input().split())))
# money = 0
# for size, cost in [map(int, input().split()) for _ in range(int(input()))]:
#     if stock[size] > 0:
#         stock[size] -= 1
#         money += cost
# print(money)
################################################################################
                                      #Q
################################################################################
# defaultdict-tutorial-English
################################################################################
################################################################################
                                     #A
################################################################################
# from collections import defaultdict
#
# d = defaultdict(list)
# n, m = map(int, input().split())
# A, B = [input() for _ in range(n)], [input() for _ in range(m)]
# for idx, val in enumerate(A, start = 1):
#     d[val].append(idx)
# for key in B:
#     if key in d.keys():
#         print(*d[key])
#     else:
#         print('-1')
################################################################################
# or for the last for
# for key in B:
#     print(*d[key] or -1)
################################################################################
# without enuemarte and creating A and B
# for i in range(n):
#     d[input()].append(i + 1)
#
# for _ in range(m):
#     print(' '.join(map(str, d[input()])) or -1)
################################################################################
################################################################################
                                      #Q
################################################################################
# py-collections-namedtuple-English
################################################################################
################################################################################
                                     #A
################################################################################
# from collections  import namedtuple
# N, Student =int(input()), namedtuple('Student',input().split())
# print('%.2f' %float(sum(list(map(int,[Student._make(input().split()).MARKS for _ in range(N)])))/N))
################################################################################
################################################################################
                                      #Q
################################################################################
# py-collections-ordereddict-English
################################################################################
################################################################################
                                     #A
################################################################################
# from collections  import OrderedDict
#
# od = OrderedDict()
# for _ in range(int(input())):
#     temp = input().split()
#     if ' '.join(temp[0:-1]) not in od.keys():
#         od[' '.join(temp[0:-1])] = int(temp[-1])
#     else:
#         od[' '.join(temp[0:-1])] += int(temp[-1])
# print('\n'.join([k + ' ' + str(v) for k,v in od.items()]))
################################################################################
# d = OrderedDict()
# for _ in range(int(input())):
#     item, space, quantity = input().rpartition(' ')
#     d[item] = d.get(item, 0) + int(quantity)
# for item, quantity in d.items():
#     print(item, quantity)
################################################################################
# dct = OrderedDict()
# for _ in range(int(input())):
#     i = input().rpartition(" ")
#     dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
# for l in dct:
#     print(l, dct[l])
################################################################################
################################################################################
                                      #Q
################################################################################
# py-collections-deque-English
################################################################################
################################################################################
                                     #A
################################################################################
# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     temp = input().split()
#     if 'append' in temp[0]:
#         eval('d.{}({})'.format(temp[0], temp[1]))
#     else:
#         eval('d.{}()'.format(temp[0]))
#
#     # eval('d.{}({})'.format(temp[0], temp[1])) if 'append' in temp[0] else eval('d.{}()'.format(temp[0]))
# print(*d)
################################################################################
# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     cmd, *args = input().split()
#     getattr(d, cmd)(*args)
#     # getattr(d, command)(*map(int, args))
# [print(x, end=' ') for x in d]
################################################################################
################################################################################
################################################################################
                                      #Q
################################################################################
# symmetric-difference-English
################################################################################
################################################################################
                                     #A
################################################################################
# _, M = input(), set(map(int, input().split()))
# _, N = input(), set(map(int, input().split()))
# for i in map(str,sorted(N.difference(M).union(M.difference(N)))):
#     print(i)
# ################################################################################
# a,b = [set(input().split()) for _ in range(4)][1::2]
# print(*sorted(a^b, key=int), sep='\n')
################################################################################
################################################################################
################################################################################
                                      #Q
################################################################################
# py-set-add-English
################################################################################
################################################################################
                                     #A
################################################################################
# print(len(set([input() for _ in range(int(input()))])))
################################################################################
                                      #Q
################################################################################
# py-set-discard-remove-pop-English
################################################################################
################################################################################
                                     #A
################################################################################
# n = int(input())
# s = set(map(int, input().split()))
# for _ in range(int(input())):
#     cmd, *arg = input().split()
#     eval('s.{}({})'.format(cmd, *arg)) if 'pop' not in cmd else eval('s.{}()'.format(cmd))
# print(sum(s))
################################################################################
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))
#
# print(sum(s))
################################################################################
# n = int(input())
# s = set(map(int, input().split()))
# for _ in range(int(input())):
#     method, *args = input().split()
#     getattr(s, method)(*map(int,args))
# print(sum(s))
################################################################################
################################################################################
                                      #Q
################################################################################
# py-set-union-English
################################################################################
################################################################################
                                     #A
################################################################################
# a,b = [list(map(int,set(input().split()))) for _ in range(4)][1::2]
# print(len(set(b).union(set(a))))
################################################################################
# _,a,_,b=[set(input().split()) for _ in '1234']; print(len(a|b))
################################################################################
################################################################################
                                      #Q
################################################################################
# py-set-intersection-operation-English
################################################################################
################################################################################
                                     #A
################################################################################
# _,a,_,b=[set(input().split()) for _ in '1234']; print(len(a&b))
################################################################################
                                      #Q
################################################################################
# py-set-difference-operation-English
################################################################################
################################################################################
                                     #A
################################################################################
# _,a,_,b=[set(input().split()) for _ in '1234']; print(len(a-b))
################################################################################
                                      #Q
################################################################################
# py-set-mutations-English
################################################################################
################################################################################
                                     #A
################################################################################
# _, a = input(), set(map(int, input().split()))
# for i in range(int(input())):
#     eval('a.{}({})'.format(input().split()[0], set(map(int, input().split()))))
# print(sum(a))
################################################################################
                                      #Q
################################################################################
# py-the-captains-room-English
################################################################################
################################################################################
                                     #A
################################################################################
# _, args = input(), input().split()
# print(*[i for i in set(sorted(args)) if args.count(i) == 1])
################################################################################
# members = input().split()
# rooms = set()   # Contains all the rooms.
# room_more_mem = set()   # Contains only the rooms with families.
#
# for m in members:
#     if m not in room_more_mem:
#         target = room_more_mem if m in rooms else rooms
#         target.add(m)
# print(rooms.difference(room_more_mem).pop())
################################################################################
                                      #Q
################################################################################
# py-check-subset-English
################################################################################
################################################################################
                                     #A
################################################################################
# for _ in range(int(input())):
#     _, A, _, B = input(), set(input().split()), input(), set(input().split())
#     print(A.issubset(B))
################################################################################
                                      #Q
################################################################################
# py-check-strict-superset-English
################################################################################
################################################################################
                                     #A
################################################################################
# A = set(input().split())
# print(all([A.issuperset(input().split()) for _ in range(int(input()))]))
################################################################################
# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))
################################################################################
                                      #Q
################################################################################
# Polar-Coordinates
################################################################################
################################################################################
                                     #A
################################################################################
# from cmath import polar
# z = input()
# print('{:.3f}\n{:.3f}'.format(abs(complex(z)),phase(complex(z))))
################################################################################
# from cmath import polar
# print '{}\n{}'.format(*polar(complex(input())))
################################################################################
# import cmath
# print(*cmath.polar(complex(input())), sep='\n')
################################################################################
                                      #Q
################################################################################
# mod-divmod
################################################################################
################################################################################
                                     #A
################################################################################
# a = divmod(int(input()),int(input()))
# print(a[0],a[1],a,sep='\n')
################################################################################
# print('{0}\n{1}\n({0},{1})'.format(*divmod(int(input()), int(input()))))
################################################################################
                                      #Q
################################################################################
# power-mod-power
################################################################################
################################################################################
                                     #A
################################################################################
# from math import pow
# a,b,m = [int(input()) for _ in range(3)]
# print('{:.0f}\n{:.0f}'.format(pow(a,b),pow(a,b)%m))
################################################################################
                                      #Q
################################################################################
# triangle-quest
################################################################################
################################################################################
                                     #A
################################################################################
# for i in range(1,int(input())):
#     print((10**(i)//9)*i)
    # print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
################################################################################
                                      #Q
################################################################################
#
################################################################################
################################################################################
                                     #A
################################################################################
# import calendar
# m,d,y = map(int,input().split())
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())
################################################################################
                                      #Q
################################################################################
# exceptions
################################################################################
################################################################################
                                     #A
################################################################################
# for i in [input().split() for i in range(int(input()))]:
#     try:
#         print(int(i[0])//int(i[1]))
#     except Exception as e:
#         print("Error Code:",e)
################################################################################
                                      #Q
################################################################################
# incorrect-regex
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# for i in [input() for i in range(int(input()))]:
#     try:
#         re.compile(i)
#         print(True)
#     except Exception:
#         print(False)
#
# cube = lambda x: x**3
################################################################################
                                      #Q
################################################################################
# map-and-lambda-expression
################################################################################
################################################################################
                                     #A
################################################################################
# cube = lambda x: x**3
# def fibonacci(n):
#     # return a list of fibonacci numbers
#     lis = [0,1]
#     for i in range(2,n):
#         lis.append(lis[i-2] + lis[i-1])
#     return(lis[0:n])
#
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
################################################################################
                                      #Q
################################################################################
# zipped-English
################################################################################
################################################################################
                                     #A
################################################################################
# N, X = map(int,input().split())
# l = [list(zip([i+1 for i in range(N)],input().split())) for mark in range(X)]
# for student in range(N):
#     s = 0
#     for subject in range(X):
#         s += float(l[subject][student][1])
#     print('{:.1f}'.format(s/X))
################################################################################
# n, x = map(int, input().split())
# sheet = []
# for _ in range(x):
#     sheet.append( map(float, input().split()) )
# for i in zip(*sheet):
#     print( sum(i)/len(i) )
################################################################################
# _, X = map(int,input().split())
# sheet = [map(float, input().split()) for _ in range(X)]
# print(*[sum(i)/len(i) for i in zip(*sheet)], sep = '\n')
################################################################################
# [print(sum(i) / len(i)) for i in zip(*[map(float, input().split()) for _ in range(int(input().split()[1]))])]
################################################################################
################################################################################
                                      #Q
################################################################################
# input
################################################################################
################################################################################
                                     #A
################################################################################
# x, k = map(int,input().split())
# print(eval(input()) == k)
################################################################################
                                      #Q
################################################################################
# any-or-all-English
################################################################################
################################################################################
                                     #A
################################################################################
# _, L = input(), input().split()
# print(all([any(map(lambda x: x == x[::-1],L)),all(map(lambda x: int(x) >= 0,L))]))
################################################################################
# N,n = int(input()),input().split()
# print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))
################################################################################
################################################################################
                                      #Q
################################################################################
# class-2-find-the-torsional-angle
################################################################################
################################################################################
                                     #A
################################################################################
# import math
#
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __sub__(self, no):
#         return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))
#
#     def dot(self, no):
#         return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
#
#     def cross(self, no):
#         return Points((self.y * no.z - self.z * no.y),
#                       (self.z * no.x - self.x * no.z),
#                       (self.x * no.y - self.y * no.x))
#
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
#
# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)
#
#     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#
#     print("%.2f" % math.degrees(angle))
################################################################################
################################################################################
                                      #Q
################################################################################
# introduction-to-regex-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# print(*[bool(re.match('[+|-]?\d*\.\d*$', input())) for _ in range(int(input()))], sep = '\n')

# bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input()))
################################################################################
################################################################################
                                      #Q
################################################################################
# re-group-groups-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# r = re.search(r"([a-zA-Z0-9])\1+",input())
# print(r.group(1) if r else -1)
################################################################################
################################################################################
                                      #Q
################################################################################
# re-findall-re-finditer-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# s = '[qwrtypsdfghjklzxcvbnm]'
# a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
# print('\n'.join(a or ['-1']))
################################################################################
                                      #Q
################################################################################
# re-start-re-end-English
################################################################################
################################################################################
                                     #A
################################################################################
# from re import compile
# data, pattern = input(), compile( input() )
# m = pattern.search(data)
# if not m : print("(-1, -1)")
# while m:
#     print(f"({m.start()}, {m.end() - 1})")
#     m = pattern.search( data, m.start() + 1)
################################################################################
                                      #Q
################################################################################
# validate-a-roman-number-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# print(str(bool(re.match(regex_pattern, input()))))
################################################################################
                                      #Q
################################################################################
# validating-the-phone-number-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# l = [bool(re.match(r"^[7-9]\d{9}$", input())) for _ in range(int(input()))]
# print(*['YES' if i else 'NO' for i in l], sep= '\n')
################################################################################
# [print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]
################################################################################
# it is better to save pattern and do not loop through it.
# the seconf solution is better because it uses one loop.
################################################################################
################################################################################
                                      #Q
################################################################################
# validating-named-email-addresses-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# p = '<[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>'
# for _ in range(int(input())):
#     n, e = input().split(' ')
#     m = re.match(p, e, re.I)
#     if m:
#         print(n, e)
################################################################################
################################################################################
                                      #Q
################################################################################
# hex-color-code
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# reg = re.compile(r"(:|,| +)(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})\b")
# n = int(input())
# for i in range(n):
#     line  = input()
#     items = reg.findall(line)
#     if items:
#         for item in items:
#             print( item[1] )

# (?<=[:\s])#[a-f0-9A-F]{3,}(?!\s)
# (?<!^)(#(?:[\da-f]{3}){1,2})
################################################################################
################################################################################
                                      #Q
################################################################################
# html-parser-part-1-English
################################################################################
################################################################################
                                     #A
################################################################################
# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print ('{:6}: {}'.format('Start', tag))
#         temp = dict(attrs)
#         for k, v in temp.items():
#             print ("-> " + k + " > " + str(v))
#
#     def handle_endtag(self, tag):
#         print ('{:6}: {}'.format('End', tag))
#
#     def handle_startendtag(self, tag, attrs):
#         print ('{:6}: {}'.format('Empty', tag))
#         temp = dict(attrs)
#         for k, v in temp.items():
#             print ("-> " + k + " > " + str(v))
#
# MyParser = MyHTMLParser()
# MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

# for ele in attrs:
#     print ('->',ele[0],'>',ele[1])
################################################################################
################################################################################
                                      #Q
################################################################################
# html-parser-part-2-English
################################################################################
################################################################################
                                     #A
################################################################################
# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_data(self, data):
#         if data != '\n':
#             print (">>> Data\n" + data)
#
#     def handle_comment(self, data):
#         if '\n' in data:
#             print('>>> Multi-line Comment\n' + data)
#         else:
#             print (">>> Single-line Comment\n" + data)
#
# html = ""
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'
#
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()
################################################################################
################################################################################
                                      #Q
################################################################################
# detect-html-tags-attributes-and-attribute-values-English
################################################################################
################################################################################
                                     #A
################################################################################
# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         [print('-> {} > {}'.format(*attr)) for attr in attrs]
#
# html = '\n'.join([input() for _ in range(int(input()))])
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()
################################################################################
################################################################################
                                      #Q
################################################################################
# validating-uid-English
################################################################################
################################################################################
                                     #A
################################################################################
# import re
# for _ in range(int(input())):
#     s = input()
#     print('Valid' if all([re.search(r, s)
#     for r in [r'[A-Za-z0-9]{10}', r'([A-Z].*){2}', r'([0-9].*){3}']])
#     and not re.search(r'(.).*\1', s)
#     else 'Invalid')
################################################################################
# def is_valid(uid):
#     has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
#     has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
#     has_10_proper_elements = bool(re.match(r'^[a-zA-Z0-9]{10}$', uid))
#     no_repeats = not bool(re.search(r'(.)\1', uid))
#
#     if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
#         return "Valid"
#     else:
#         return "Invalid"
#
# for _ in range(int(input())):
#     print is_valid(input())
################################################################################
################################################################################
################################################################################
                                      #Q
################################################################################
# xml-1-find-the-score-English
################################################################################
################################################################################
                                     #A
################################################################################
# import sys
# import xml.etree.ElementTree as etree
#
# def get_attr_number(node):
#     # your code goes here
#     s = 0
#     for child in root.iter():
#         s += len(child.attrib)
#     return s
#
# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))
################################################################################
# return sum([len(elem.items()) for elem in tree.iter())
################################################################################
################################################################################
################################################################################
                                      #Q
################################################################################
# xml2-find-the-maximum-depth-English
################################################################################
################################################################################
                                     #A
################################################################################
# import xml.etree.ElementTree as etree
#
# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     if (level == maxdepth):
#         maxdepth += 1
#     # recursive call to function to get the depth
#     for child in elem:
#         depth(child, level + 1)
#
# if __name__ == '__main__':
#     n = int(input())
#     xml = ""
#     for i in range(n):
#         xml =  xml + input() + "\n"
#     tree = etree.ElementTree(etree.fromstring(xml))
#     depth(tree.getroot(), -1)
#     print(maxdepth)
################################################################################
                                      #Q
################################################################################
# np-shape-reshape-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# print(np.reshape(np.array(list(map(int, input().split()))), (3, 3)))
# print(np.array(input().split(),int).reshape(3,3))
# print (numpy.fromstring(input(), dtype=int, sep=" ").reshape(3,3))
################################################################################
                                      #Q
################################################################################
# np-transpose-and-flatten-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N, M = map(int,input().split())
# arr = [list(map(int,input().split()[:M])) for r in range(N)]
# print(np.array(arr).transpose() , np.array(arr).flatten() , sep = '\n')
################################################################################
                                      #Q
################################################################################
# np-concatenate-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N, M, P = map(int,input().split())
# print(np.array([input().split()[:P] for _ in range(N + M)], int))]]
#
# NxP = np.array([input().split()[:P] for _ in range(N)], int)
# MxP = np.array([input().split()[:P] for _ in range(M)], int)
# print(np.concatenate((NxP, MxP), axis = 0))
################################################################################
                                      #Q
################################################################################
# np-zeros-and-ones-English
################################################################################
################################################################################
                                     #A
################################################################################
# nums = tuple(map(int, input().split()))
# print (numpy.zeros(nums, dtype = numpy.int), numpy.ones(nums, dtype = numpy.int), sep = '\n')
################################################################################
                                      #Q
################################################################################
# np-array-mathematics-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N, M = map(int,input().split())
# A = np.array([input().split()[:M] for _ in range(N)], int)
# B = np.array([input().split()[:M] for _ in range(N)], int)
# print(A + B, A - B, A * B, A // B, A % B, A ** B, sep = '\n')
################################################################################
                                      #Q
################################################################################
# np-sum-and-prod-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N, M = map(int,input().split())
# print(np.prod(np.sum([np.array(input().split()[:M], int) for _ in range(N)], axis = 0), axis = None))
################################################################################
                                      #Q
################################################################################
# np-min-and-max-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N, M = map(int,input().split())
# NxM = np.array([input().split()[:M] for _ in range(N)], int)
# print(np.max(np.min(NxM, axis = 1)))
################################################################################
                                      #Q
################################################################################
# np-mean-var-and-std-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# np.set_printoptions(legacy='1.13')
# N, M = map(int,input().split())
# NxM = np.array([input().split()[:M] for _ in range(N)], int)
# print(np.mean(NxM, axis = 1), np.var(NxM, axis = 0), np.std(NxM), sep = '\n')
################################################################################
                                      #Q
################################################################################
# np-dot-and-cross-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N = int(input())
# A = np.array([input().split()[:N] for _ in range(N)], int)
# B = np.array([input().split()[:N] for _ in range(N)], int)
# print(A.dot(B)) # print(np.dot(A, B))
################################################################################
                                      #Q
################################################################################
# np-inner-and-outter-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# A = np.array(input().split(), int)
# B = np.array(input().split(), int)
# print(np.inner(A, B), np.outer(A, B),sep = '\n')
################################################################################
                                      #Q
################################################################################
# np-polynomials-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# P = np.array(input().split(), float)
# X = float(input())
# print(np.polyval(P, X))
################################################################################
# print(np.polyval(list(map(float,input().split())), float(input())))
################################################################################
                                      #Q
################################################################################
# np-linear-algebra-English
################################################################################
################################################################################
                                     #A
################################################################################
# import numpy as np
# N = int(input())
# A = np.array([input().split() for _ in range(N)], float)
# print(round(np.linalg.det(A), 2))
################################################################################
                                      #Q
################################################################################
# standardize-mobile-number-using-decorators-English
################################################################################
################################################################################
                                     #A
################################################################################
# def wrapper(f):
#     def fun(l):
#         f([f'+91 {i[-10:-5]} {i[-5:]}' for i in l])
#     return fun
#
# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')
#
# if __name__ == '__main__':
#     l = [input() for _ in range(int(input()))]
#     sort_phone(l)
################################################################################
                                      #Q
################################################################################
# the-minion-game-English
################################################################################
################################################################################
                                     #A
################################################################################
def minion_game(string):

    s = string.upper()
    S, K = 0, 0
    text_length = len(s)

    for idx, element in enumerate(s):
        if element[0]  in 'AEIOU':
            K += text_length - idx
        else:
            S += text_length - idx

    if S > K:
        print('Stuart {}'.format(S))
    elif S < K:
        print('Kevin {}'.format(K))
    elif S == K:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
# https://codereview.stackexchange.com/questions/106238/the-minion-game-challenge
