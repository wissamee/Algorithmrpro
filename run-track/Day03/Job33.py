import re
def count_words_without_special_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)            
            count = sum(1 for word in words if word.isalpha())
            
            return count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0
if __name__ == "__main__":
    file_path = "data.txt"  
    word_count = count_words_without_special_characters(file_path)
    print(f"Number of words without special characters: {word_count}")
