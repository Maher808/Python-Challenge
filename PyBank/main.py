import csv
# Path to the CSV file
csv_path= r"PyBank\Resources\budget_data.csv"
# Function to analyze financial data

def analyze_financial_data(csv_path):
    # Initialize variables
    total_months = 0
    net_total = 0
    prev_profit_loss = 0
    changes = []
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}

    # Read CSV file
    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        # Skip header
        next(csvreader)

        # Loop through rows in the CSV
        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and net total
            total_months += 1
            net_total += profit_loss

            # Calculate changes and update greatest increase/decrease
            if total_months > 1:
                change = profit_loss - prev_profit_loss
                changes.append(change)

                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = date
                    greatest_increase["amount"] = change

                if change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = date
                    greatest_decrease["amount"] = change

            # Update previous profit/loss for the next iteration
            prev_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

    # Write in Txt file 
    file= open("financial_analysis.txt", "w")
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months:" + str(total_months)+"\n")
    file.write(f"Net Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    # Display results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


 
# Call the function with the CSV file path
analyze_financial_data(csv_path)













