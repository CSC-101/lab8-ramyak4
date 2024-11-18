import sys

def main():
    if len(sys.argv) != 2:
        print("Error")
        sys.exit()

    file_name = sys.argv[1]

    try:
        # Try to open the file
        with open(file_name, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                # Strip newline and whitespace characters
                line = line.strip()
                try:
                    # Split the line into two values
                    values = line.split()
                    if len(values) != 2:
                        raise ValueError("Line does not contain exactly two values.")

                    # Convert the values to floats
                    num1 = float(values[0])
                    num2 = float(values[1])

                    # Print the sum
                    print(f"Line {line_num}: {num1 + num2}")
                except ValueError as e:
                    print(f"Error on line {line_num}: {e}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")
        sys.exit(1)

    if __name__ == "__main__":
        main()
