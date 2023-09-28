import matplotlib.pyplot as plt

def count_next_letters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.lower()
            next_letter_counts = {}
            for i in range(len(text) - 1):
                current_char = text[i]
                next_char = text[i + 1]
                if current_char.isalpha() and next_char.isalpha():
                    next_letter_counts.setdefault(current_char, {}).setdefault(next_char, 0)
                    next_letter_counts[current_char][next_char] += 1
            return next_letter_counts
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return {}
def plot_superimposed_curves(next_letter_counts):
    if not next_letter_counts:
        return
    plt.figure(figsize=(12, 6))
    for letter, counts in next_letter_counts.items():
        total_counts = sum(counts.values())
        percentages = {next_letter: (count / total_counts) * 100 for next_letter, count in counts.items()}
        sorted_data = sorted(percentages.items(), key=lambda x: x[0])
        next_letters, percentages = zip(*sorted_data)
        print(f"{letter.upper()}: {', '.join([f'{next_letter}({percent:.1f}%)' for next_letter, percent in percentages.items()])}")        
        plt.plot(next_letters, percentages, label=letter)    
    plt.xlabel("Next Letters")
    plt.ylabel("Percentage of Appearance (%)")
    plt.title("Percentage of Appearance of Each Next Letter")
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    file_path = r"C:\Users\pcBEN\Desktop\algo pro\data.txt"
    next_letter_counts = count_next_letters(file_path)
    plot_superimposed_curves(next_letter_counts)
