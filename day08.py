# a program to read a file and count how many lines
#read an absolute file
with open(r"C:\Users\Triddles lamar\Downloads\test.txt") as file:
    print("These are the content of the txt file")
    print("====================================================================")
    #assign lines variable to read file lines
    lines=file.readlines()
    #loop through file for every line
    for line in lines:
        print(line, end=' ')
    line_numbers=len(lines)
    #print number of lines
    print(f"\nThe number oof lines in the txt file is {line_numbers} lines")
    