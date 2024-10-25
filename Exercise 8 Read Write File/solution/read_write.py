def writeToFile(filename, text):
    """Writes the given text to the specified file, overwriting any existing content."""
    with open(filename, 'w') as file:
        file.write(text)

def appendToFile(filename, text):
    """Appends the given text to the specified file, preserving existing content."""
    with open(filename, 'a') as file:
        file.write(text)

def readFromFile(filename):
    """Reads the entire contents of the specified file and returns it as a string."""
    with open(filename, 'r') as file:
        return file.read()

# Example usage:
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')

# Assert to check that the content is correct
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
