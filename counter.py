# Importing Libraries
from collections import Counter
text = input("Enter the file location: ")
char_to_count = input("Enter the character you want to count: ")
try:
    # Opening the file in read mode
    with open(text, 'r') as file:
        # Reading the text from the file
        text = file.read()
        
        # Counting the number of occurrences of 'e' in the text
        num_of_instances = Counter(text)
        count_of_letter = num_of_instances[char_to_count]
        
        print("Number of occurrences in the text:", count_of_letter)
except FileNotFoundError:
    print("File not found. Please make sure you have entered the correct file location.")
except Exception as e:
    print("An error occurred:", e)

