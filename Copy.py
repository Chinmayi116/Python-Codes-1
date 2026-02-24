# Copy contents of one file to another

source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    # Open source file in read mode
    file1 = open(source_file, "r")
    
    # Open destination file in write mode
    file2 = open(destination_file, "w")
    
    # Read data from source file
    data = file1.read()
    
    # Write data into destination file
    file2.write(data)
    
    print("File copied successfully!")

    # Close both files
    file1.close()
    file2.close()

except FileNotFoundError:
    print("Source file not found!")
