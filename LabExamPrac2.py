#Alyn  Ovell
#LabExamPractice2

# initialize variables
total_sales = 0
highest_sales = -float('inf')
lowest_sales = float('inf')
months = []

# loop through 12 months
for i in range(12):
    # get sales for the month
    month_name = input(f"Enter the name of month {i+1}: ")
    sales = float(input(f"Enter sales for {month_name}: "))

    # update variables
    total_sales += sales
    months.append((month_name, sales))
    if sales > highest_sales:
        highest_sales = sales
        highest_month = month_name
    if sales < lowest_sales:
        lowest_sales = sales
        lowest_month = month_name

# calculate monthly average
monthly_average = total_sales / 12

# print results
print(f"\nTotal sales for the year: ${total_sales:.2f}")
print(f"Monthly average sales: ${monthly_average:.2f}")
print(f"Highest monthly sales: ${highest_sales:.2f} (in {highest_month})")
print(f"Lowest monthly sales: ${lowest_sales:.2f} (in {lowest_month})")

