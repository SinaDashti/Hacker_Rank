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
for i in range(1,int(input())):
    print((10**(i)//9)*i)
    # print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
