array = [ 20, 13, 32, 63, 64, 65, 66, 67, 68, 69, 510, 11, 412 ]

user_input = input("Enter R for reverse or F for foward: ")
user_input = user_input.lower()

def reverse(input_array):
    if user_input == 'r':
        for i in range(len(input_array)):
            for k in range(1, len(input_array) -i):
                if input_array[k -1] < input_array[k]:
                    (input_array[k - 1], input_array[k]) = (input_array[k], input_array[k - 1])
        print(input_array)

def forward(new_array):
    if user_input == 'f':
       for j in range(len(new_array)):
           for h in range(1, len(new_array) -j):
               if new_array[h -1] > new_array[h]:
                   (new_array[h - 1], new_array[h]) = (new_array[h], new_array[h -1])
       print(new_array)


reverse(array)
forward(array)






#array = [ 20, 13, 32, 63, 64, 65, 66, 67, 68, 69, 510, 11, 412 ]

#new_array = []


#user_input = input("Enter R for reverse or F for foward: ")
#user_input = user_input.lower()

#def reverse(array):
#if user_input == 'r':
#for i in range(len(array)):
#    for k in range(1, len(array) -i):
#        if array[k -1] < array[k]:
#            (array[k - 1], array[k]) = (array[k], array[k - 1])

#print(array)
    #elif user_input == 'f':
    #    for j in array:
    #        print(j)
    #else:
    #    print("Invalid Entry!")
