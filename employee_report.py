import csv

HIGHLY_EFFICIENT = 2
INEFFICIENT = 1


def main():

    file_obj = open('employee_data.csv', 'r')
    csv_file = csv.reader(file_obj)

    next(csv_file)

    records = list(csv_file)
        
    print('Highly Efficient Individuals:')

    for rec in records:
        ef_factor = float(rec[5])/float(rec[4])
        if ef_factor > HIGHLY_EFFICIENT:
            print(rec[1])


    print()
    print()
    print()


    print('Low Efficiency Individuals:')

    for rec in records:
        ef_factor = float(rec[5])/float(rec[4])
        if ef_factor < INEFFICIENT:
            print(rec[1])

    print()
    print()
    print()

    print('Employees in their 40s')

    Employees_in_40s = 0
    for rec in records:
        if int(rec[2]) >= 40:
            print(rec[1])
            Employees_in_40s += 1

    print()
    print(f"Total number of employees in their 40s: {Employees_in_40s}")

    print()
    print()
    print()

    print('Employees in their 30s')

    Employees_in_30s = 0
    for rec in records:
        if int(rec[2]) >= 30 and int(rec[2]) < 40:
            print(rec[1])
            Employees_in_30s += 1

    print()
    print(f"Total number of employees in their 30s: {Employees_in_30s}")

    print()
    print()
    print()

    print('Employees in their 20s')

    Employees_in_20s = 0
    for rec in records:
        if int(rec[2]) >= 20 and int(rec[2]) < 30:
            print(rec[1])
            Employees_in_20s += 1

    print()
    print(f"Total number of employees in their 20s: {Employees_in_20s}")

    file_obj.close()

main()