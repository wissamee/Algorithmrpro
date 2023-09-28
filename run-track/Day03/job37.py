import matplotlib.pyplot as plt
def count_starting_letters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()            
            text = text.lower()
            words = text.split()
            starting_letter_counts = {}            
            for word in words:
                if word and word[0].isalpha():
                    letter = word[0]
                    starting_letter_counts[letter] = starting_letter_counts.get(letter, 0) + 1
            return starting_letter_counts
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return {}
def plot_histogram(starting_letter_counts):
    if not starting_letter_counts:
        return
    total_starting_letters = sum(starting_letter_counts.values())
    percentages = {letter: (count / total_starting_letters) * 100 for letter, count in starting_letter_counts.items()}    
    sorted_data = sorted(percentages.items(), key=lambda x: x[0])
    letters, percentages = zip(*sorted_data)
    plt.figure(figsize=(12, 6))
    plt.bar(letters, percentages)
    plt.xlabel("Starting Letters")
    plt.ylabel("Percentage of Presence (%)")
    plt.title("Percentage of Presence of Each Starting Letter")
    plt.xticks(rotation=90)
    plt.tight_layout()    
    plt.show()
if __name__ == "__main__":
    file_path = r"C:\Users\pcBEN\Desktop\algo pro\data.txt" 
    starting_letter_counts = count_starting_letters(file_path)
    plot_histogram(starting_letter_counts)
