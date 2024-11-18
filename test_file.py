def create_test_file(file_name: str):
    # Sample lines to write into the file
    lines = [
        "1.5 2.3\n",  # Valid line
        "3.1 4.7\n",  # Valid line
        "5.0\n",  # Invalid line (only one value)
        "abc 2.0\n",  # Invalid line (non-numeric value)
        "7.0 8.9\n"  # Valid line
    ]

    try:
        with open(file_name, 'w') as file:
            file.writelines(lines)
        print(f"Test input file '{file_name}' created successfully.")
    except IOError:
        print(f"Error: Could not create the file '{file_name}'.")


if __name__ == '__main__':
    create_test_file("test_input.txt")