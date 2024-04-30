from collections import Counter # Importing Libraries
text = input("Enter the file path (Ensure there are no quotation marks at the start or end of the file path): ") # Getting user to input file location for script
char_to_count = input("Enter the character you want to count: ") # Getting user to identify character they want to count
try:
    with open(text, 'r') as file: # Opening the file in read mode
        text = file.read() # Creating a variable called text and making that read the file specified
        num_of_instances = Counter(text) # Using the counter function to count the occurrence of all characters in the text
        count_of_letter = num_of_instances[char_to_count] # Specifying that I want to count the character the user inputted
        print("Number of occurrences in the text:", count_of_letter) # Printing out the occurence of the letter specified
except FileNotFoundError: # Creating an error for when the file was not found
    print("This file was not found. Can you make sure the correct file path is being used.") # Stating error message
except IsADirectoryError: # Creating an error for when file path is not correct
    print("The file path you provided is a directory and not a path to a file. Please recheck the file path.") # Stating error message
except Exception as e:  # Creating an error for when script runs into an exception when running.
    print("An error occurred:",e) # Stating error message


# File Not Found: https://www.geeksforgeeks.org/why-am-i-getting-a-filenotfounderror-in-python/
# Exception: https://docs.python.org/3/tutorial/errors.html
# Directory Error: https://docs.python.org/3/library/exceptions.html
# Reading in Files: https://www.w3schools.com/python/python_file_open.asp
# Reading in Files: https://www.geeksforgeeks.org/reading-writing-text-files-python/
# Reading in Files: https://realpython.com/read-write-files-python/
# Counter Library: https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
