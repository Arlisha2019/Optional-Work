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
    elif user_input == 'f':
       for j in range(len(input_array)):
           for h in range(1, len(input_array) -j):
               if input_array[h -1] > input_array[h]:
                   (input_array[h - 1], input_array[h]) = (input_array[h], input_array[h -1])
       print(input_array)
    else:
       print("Invaild Entry: Please enter R or F.")

reverse(array)
