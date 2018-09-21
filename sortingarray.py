array = [ 20, 13, 32, 63, 64, 65, 66, 67, 68, 69, 510, 11, 412 ]

#new_array = []


#user_input = input("Enter R for reverse or F for foward: ")
#user_input = user_input.lower()

#def reverse(array):
#if user_input == 'r':
for i in range(len(array)):
    for k in range(1, len(array) -i):
        if array[k -1] < array[k]:
            (array[k - 1], array[k]) = (array[k], array[k - 1])

print(array)
    #elif user_input == 'f':
    #    for j in array:
    #        print(j)
    #else:
    #    print("Invalid Entry!")
