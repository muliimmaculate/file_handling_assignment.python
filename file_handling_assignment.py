# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2 with numbers: 12345.\n")
    file.write("This is line 3, the last line.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading complete.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4, appended.\n")
        file.write("This is line 5, appended.\n")
        file.write("This is line 6, appended.\n")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending complete.")

