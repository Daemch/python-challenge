import os
import csv

#PyBank_csvpath = os.path.join("..", "Resources", "budget_data")

with open('budget_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

    months = []
    profits = []
    monthly_changes = []

    for row in reader:
        months.append(row[0])
        profits.append(int(row[1]))

    total_months = len(months)
    net_total = sum(profits)

    for i in range(1, total_months):
        monthly_changes.append(profits[i] - profits[i - 1])

    average_change = sum(monthly_changes) / (total_months - 1)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    increase_date = months[monthly_changes.index(greatest_increase) + 1]
    decrease_date = months[monthly_changes.index(greatest_decrease) + 1]

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

    # export results to a text file
    
    with open('PyBank_Results.txt', 'w') as text:
        text.write("Financial Analysis\n")
        text.write("-------------------------\n")
        text.write(f"Total Months: {total_months}\n")
        text.write(f"Total Profits: ${net_total}\n")
        text.write(f"Average Change: ${average_change:.2f}\n")
        text.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
        text.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")



