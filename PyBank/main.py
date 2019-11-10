import os
import csv 

month_count = 0
net_amount = 0
change = 0
previous_month = 0
monthly_change = []
greatest_increase = 0
increase_month = 0
greatest_decrease = 0
decrease_month = 0

budget_path = os.path.join("c:/Users/Nada/Desktop/Data_Science_Bootcamp/Python/python-challenge/PyBank/budget_data.csv")

with open(budget_path, newline='') as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=',')
    next(budget_reader)
    row = next(budget_reader)
    previous_month = int(row[1])

    for row in budget_reader:
        month_count += 1 
        net_amount += int(row[1])

        change = int(row[1]) - int(previous_month)
        monthly_change.append(change)
        previous_month = row[1]

        average_change = sum(monthly_change)/ len(monthly_change)

        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            increase_month = row[0]
        
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            decrease_month = row[0]
        
    ave_change = float("{0:.2f}".format(average_change))
    increase = max(monthly_change)
    decrease = min(monthly_change)

print(f"""Financial Analysis 
----------------------------
Total Months: {month_count}
Total: ${net_amount} 
Average  Change: ${ave_change} 
Greatest Increase in Profits: {increase_month} (${increase}) 
Greatest Decrease in Profits: {decrease_month} (${decrease}) """)    
   

with open('budget_data_revised.text', 'w+') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {month_count}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${ave_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {increase_month}, (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {decrease_month}, (${decrease})\n")


        
    




