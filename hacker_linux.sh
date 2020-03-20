################################################################################
                                      #Q
################################################################################
# Your task is to use for loops to display only odd natural numbers from  to .
# Input Format
# There is no input.
# Constraints
# -
# Output Format
# 1
# 3
# 5
# .
# .
# .
# .
# .
# 99
# Sample Input
# -
# Sample Output
# 1
# 3
# 5
# .
# .
# .
# .
# .
# 99
################################################################################
                                     #A
################################################################################
# HACKER
##!/bin/bash
# for i in {1..99..2}
# do
#   echo "$i"
# done
################################################################################
# MAC
##!/usr/bin/env bash
# for i in $(seq 1 2 100)
# do
#    echo "$i"
# done
################################################################################
                                      #Q
################################################################################
# Write a Bash script which accepts  as input and displays a greeting:
# "Welcome (name)"
# Input Format
# One line, containing a .
# Output Format
# One line: "Welcome (name)" (quotation marks excluded).
# The evaluation will be case-sensitive.
# Sample Input 0
# Dan
# Sample Output 0
# Welcome Dan
# Sample Input 1
# Prashant
# Sample Output 1
# Welcome Prashant
################################################################################
                                     #A
################################################################################
#!/usr/bin/env bash
# read name
# echo "Welcome $name"
################################################################################
                                      #Q
################################################################################
# Given two integers,x and y, find their sum, difference, product, and quotient.
# Input Format
# Two lines containing one integer each (x and ,y respectively).
# Constraints
#
#
# Output Format
# Four lines containing the sum (x+y), difference (x-y), product (x*y),
# and quotient (x/y), respectively.
# (While computing the quotient, print only the integer part.)
# Sample Input
# 5
# 2
# Sample Output
# 7
# 3
# 10
# 2
# Explanation
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2 (Integer part)
################################################################################
                                     #A
################################################################################
# #!/usr/bin/env bash
# read x
# read y
#
# echo $((x + y))
# echo $((x - y))
# echo $((x * y))
# echo $((x / y))

##!/bin/bash
# read x
# read y
# printf "%s\n" $x{+,-,*,/}$y | bc


##!/bin/bash
# read x
# read y
# for i in {+,-,"*",/}
# do
#     var=$(((x)$i(y)))
#     echo $var
# done

##!/bin/bash
# read x
# read y
# for i in {+,-,\*,/}
# do
#     echo `expr $(((x)$i(y)))`
# done

##!/bin/bash
# read x
# read y
# echo `expr $x + $y`
# echo `expr $x - $y`
# echo `expr $x \* $y`
# echo `expr $x / $y`

##!/bin/bash
# read x
# read y
# echo -e "$((x+y))\n$((x-y))\n$((x*y))\n$((x/y))"
################################################################################
                                      #Q
################################################################################
# Read in one character from the user (this may be 'Y', 'y', 'N', 'n').
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.
# Input Format
# One character (this may be 'Y', 'y', 'N', 'n').
################################################################################
                                     #A
################################################################################
#!/bin/bash

# read char;
# if [[ $char == "y" || $char == "Y" ]];
# then
#     echo "YES"
# elif [[ $char == "n" || $char == "N" ]];
# then
#     echo "NO"
# fi

# read char; echo -e "YES\nNO\n" | grep -i $char

# read a
# [[ "$a" == [yY] ]] && echo 'YES'
# [[ "$a" == [nN] ]] && echo 'NO'
################################################################################
                                      #Q
################################################################################
