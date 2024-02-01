import csv

def main():

    infile = open('customers.csv','r')

    csv_file = csv.reader(infile)

    outfile = open('customer_country.csv','w')

    next(csv_file)

    outfile.write("Full Name,Country\n")

    i = 0

    for rec in csv_file:
        outfile.write(f"{rec[1]} {rec[2]},{rec[4]}\n")
        i += 1
    outfile.write(f"Number of Records: {i}")
    outfile.close()

main()