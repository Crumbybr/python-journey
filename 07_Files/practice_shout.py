fname = input("Enter the filename: ")
file = open(fname)
for line in file:
        u_print = line.upper()
        print(u_print)
file.close()