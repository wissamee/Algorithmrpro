import matplotlib.pyplot as plt
def count_word_sizes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()            
            words = text.split()
            word_sizes = {}            
            for word in words:
                size = len(word)
                word_sizes[size] = word_sizes.get(size, 0) + 1
            return word_sizes
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return {}
def plot_histogram(word_sizes):
    if not word_sizes:
        return    
    total_words = sum(word_sizes.values())    
    percentages = {size: (count / total_words) * 100 for size, count in word_sizes.items()}    
    sorted_data = sorted(percentages.items())
    sizes, percentages = zip(*sorted_data)    
    plt.figure(figsize=(12, 6))
    plt.bar(sizes, percentages)
    plt.xlabel("Word Size")
    plt.ylabel("Percentage of Appearance (%)")
    plt.title("Percentage of Appearance of Each Word Size")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = r"C:\Users\pcBEN\Desktop\algo pro\data.txt" 
    word_sizes = count_word_sizes(file_path)
    plot_histogram(word_sizes)
