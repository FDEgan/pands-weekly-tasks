int = user_input = int(input("Enter an integer: ")) # Prompting user to enter an integer)
num_list = [int] #Creating a new list that will take in the integer I chose
while int != 1: # Using a while loop to dictate, when the value is not 1 to persist through the loop
    if int % 2 == 0: # Using a modulo to see if the value is odd or even - This is in case the value is even
        int = int // 2 # When value is even, divide the value by 2
    else: # In case the value is not even
        int = 3 * int + 1 # Logic for when the value is odd. Multiply by 3 and add 1
    num_list.append(int) #append the value to the new list I created
print(num_list) # Print out that new list
