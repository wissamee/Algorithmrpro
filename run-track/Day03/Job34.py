def count_words_with_length(file_path, word_length):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()            
            words = text.split()
            count = sum(1 for word in words if len(word) == word_length)
            return count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0
if __name__ == "__main__":
    file_path = r"C:\Users\pcBEN\Desktop\algo pro\data.txt" 
    
    try:
        word_length = int(input("Enter a whole number to specify the word size: "))
        if word_length < 0:
            print("Please enter a non-negative whole number.")
        else:
            word_count = count_words_with_length(file_path, word_length)
            print(f"Number of words with length {word_length}: {word_count}")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
import numpy as np 
print(np.exp(4))