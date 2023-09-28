import matplotlib.pyplot as plt
def count_letter_occurrences(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()            
            text = text.lower()
            letter_counts = {}            
            for char in text:
                if char.isalpha():
                    letter_counts[char] = letter_counts.get(char, 0) + 1
            return letter_counts
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return {}
def plot_histogram(letter_counts):
    if not letter_counts:
        return    
    total_letters = sum(letter_counts.values())
    percentages = {letter: (count / total_letters) * 100 for letter, count in letter_counts.items()}    
    sorted_data = sorted(percentages.items(), key=lambda x: x[0])
    letters, percentages = zip(*sorted_data)    
    plt.figure(figsize=(12, 6))
    plt.bar(letters, percentages)
    plt.xlabel("Letters")
    plt.ylabel("Percentage of Appearance (%)")
    plt.title("Percentage of Appearance of Each Letter")
    plt.xticks(rotation=90)
    plt.tight_layout()    
    plt.show()
if __name__ == "__main__":
    file_path = r"C:\Users\pcBEN\Desktop\algo pro\data.txt" 
    letter_counts = count_letter_occurrences(file_path)
    plot_histogram(letter_counts)
