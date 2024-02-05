import csv

def main():

    infile = open('employee_data.csv','r')

    csv_file = csv.reader(infile)


    next(csv_file)

    bonus_value = 0
    total_pay = 0
    
    for rec in csv_file:
        print(f"Name: {rec[1]}")

        salary_value = float(rec[3])
        print(f"Salary: $  {salary_value:,.2f}")

        bonus_value = float(rec[7]) * float(rec[3])
        print(f"Bonus:  $   {bonus_value:,.2f}")
        
        total_pay = bonus_value + float(rec[3])
        print(f"Pay:    $  {total_pay:,.2f}")
        input()
        print("hi")


main()