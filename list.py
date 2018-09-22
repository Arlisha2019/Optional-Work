
numbers = [ 15, -15, 45, 35, 89, 23, 23, 28, 28, 32, 32, 66, 66, 151, 151, 209, 18, 11, -17, 9, 0, -67, 12 ]
#Printing the sum of the numbers variable
numbers_sum = sum(numbers)
print("The sum of the numbers in your list equals {0}!".format(numbers_sum))
numbers.sort()

#Printing the highest number in the variable numbers
print("The maximum number in the list is: ", max(numbers))

#Printing the lowest number in the variable numbers
print("The minimum number in the list is: ", min(numbers))

#Printing the even numbers in the variable numbers
even_numbers = [ x for x in numbers if x % 2 == 0]
print("The even numbers in your list are {0}: ".format(even_numbers))

# Another way to print the even and odd numbers in the variable numbers
#even = [ ]
#odd = [ ]
#def even_odd(nummbers):
  #for i in numbers:
    #if i % 2 == 0:
      #even.append(i)
    #else:
      #odd.append(i)

#even_odd(numbers)

#even.sort()
#odd.sort()

#print("The even numbers in your list are: {0}.".format(even))
#print("The odd numbers in your list are: {0}.".format(odd))

#Printing the numbers that are greater than zero
greater_than_zero = [ y for y in numbers if y > 0]
print("The numbers greater than zero in your list are: {0}. ".format(greater_than_zero))

#Printing positive numbers only
positive_number_only = list(filter(lambda i: i > 0, numbers))
print("The positive numbers in your list are: {0}. ".format(positive_number_only))

#Printing the results of multiplying the list by a single element
def multiply_by_5(numbers):
    for f in range(len(numbers)):
        numbers[f] = numbers[f] * 5
    return numbers
print("When you multiply the numbers in you list by 5, the results are: {0}. ".format(numbers))

#Printing multiply Vectors of the same length
a = [15, 20, 25, 30, 45]
h = [45, 30, 25, 20, 15]
ah = []
for k in range(0, len(a)):
    ah.append(a[k]*h[k])
print("The results of multiplying the list from a & b are: {0}.".format(ah))

#Printing Matrix Addition and Matrix Addition II
i = [[15, 20],
     [20, 15]]

q = [[2, 10],
     [10, 2]]

results = [[0, 0],
          [0, 0]]

for v in range(len(i)):
    for z in range(len(i[0])):
        results[v][z] = i[v][z] + q[v][z]

for r in results:
    print("The results of adding the matrix list of i and q are: {0}. ".format(r))

c = [[ 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 25]]

g = [[1, 2, 3, 4, 5],
    [ 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]

result = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

for w in range(len(c)):
    for o in range(len(c[0])):
        result[w][o] = c[w][o] + g[w][o]

for p in result:
    print("The result of adding the matrix list of c and g are: {0}. ".format(p))

#Printing the duplicate values removed from the orginal numbers variable
def remove_dup(numbers):
    final_list = []
    for y in numbers:
        if y not in final_list:
            final_list.append(y)
    return final_list

print(remove_dup(numbers))
