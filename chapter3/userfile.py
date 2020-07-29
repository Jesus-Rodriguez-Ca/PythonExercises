def main():
    print("This program allaws you to enter data that is written to a text file: ")
    print("from your files")
    infilename=input("Enter the file name with the names: ")
    outfilename=input("Enter the name of the output file: ")
    infile=open(infilename, "r")
    outfile=open(outfilename, "w")
    for line in infile:
        first, last= line.split()
        username=(first[0] + last[:7]).lower()
        print(username, file=outfile)
    infile.close()
    outfile.close()

    print("The user names have been written to", outfilename)
main()
