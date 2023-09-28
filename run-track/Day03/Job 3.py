user_input = input("Enter a character string: ")
custom_file_path = "c:/Users/pcBEN/Desktop/algo pro/output.txt"
with open(custom_file_path, "a") as file:
    file.write(user_input + "\n")
print(f"String has been written to {custom_file_path}")
with open(custom_file_path, "r") as file:
    file_contents = file.read()
    print("Contents of output.txt:")
    print(file_contents)