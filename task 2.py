def write_to_file(filename):
    data = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')
    print("Data written to output.txt")

def append_to_file(filename):
    additional_data = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_data + '\n')
    print("Additional data appended to the file.")

def read_file(filename):
    print("\nFinal content of the file:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Main program flow
filename = "output.txt"
write_to_file(filename)
append_to_file(filename)
read_file(filename)