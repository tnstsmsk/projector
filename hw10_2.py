text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

with open('file1.txt', 'w') as file1:
    file1.write(text)

with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
    data = file1.read()
    result = data.upper()
    file2.write(result)
