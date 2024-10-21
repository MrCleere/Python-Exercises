def printASCIITable():
    for i in range(32, 127):
        # Get the ASCII character corresponding to the ASCII value
        char = chr(i)
        # Print the ASCII value followed by the character
        print(f"{i} {char}")

# Call the function to display the ASCII table
printASCIITable()
