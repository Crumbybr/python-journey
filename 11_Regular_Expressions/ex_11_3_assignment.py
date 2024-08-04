import re
tot = 0

fname = input("Enter Filename: ")
if fname != 'data-files-assignment.txt' :
    print('Incorrect filename, please try again.')
    quit()


with open(fname) as f:
    for line in f:
        extract_digits = re.findall('\d+', line)
        
        for digit in extract_digits:
            int_digit = int(digit)
            tot += int_digit
    
print(tot)
    