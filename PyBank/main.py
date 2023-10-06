import csv
from pathlib import Path

# Function to calculate financial analysis
def calculate_financial_analysis(csv_file_path):
    # Initialize variables to store the financial data
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_loss_change = 0
    profit_loss_changes = []
    months = []

    # Read the CSV file using the absolute path
    with open(csv_file_path, newline="") as csvfile:
        financial_data = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        next(financial_data)

        # Loop through each row of financial data and extract date and profit/loss 
        for row in financial_data:
            date = row[0]
            profit_loss = int(row[1])

            # Increment total_months count by 1 and total_profit_losses by each iteration's profit/loss
            total_months += 1
            total_profit_losses += profit_loss

            # Calculate profit change if there's enough data (total_months > 1).
            if total_months > 1:
                profit_loss_change = profit_loss - previous_profit_loss
                profit_loss_changes.append(profit_loss_change)
                months.append(date)

            previous_profit_loss = profit_loss

    # Calculate the average change in profit/loss
    if len(profit_loss_changes) > 0:
        average_change = sum(profit_loss_changes) / len(profit_loss_changes)
    else:
        average_change = 0

    # Find the greatest increase and decrease in profit
    greatest_increase = max(profit_loss_changes) if profit_loss_changes else 0
    greatest_decrease = min(profit_loss_changes) if profit_loss_changes else 0

    # Find the corresponding months for the greatest increase and decrease
    if greatest_increase:
        greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
    else:
        greatest_increase_month = "N/A"
    
    if greatest_decrease:
        greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]
    else:
        greatest_decrease_month = "N/A"

    return {
        "total_months": total_months,
        "total_profit_losses": total_profit_losses,
        "average_change": average_change,
        "greatest_increase": greatest_increase,
        "greatest_increase_month": greatest_increase_month,
        "greatest_decrease": greatest_decrease,
        "greatest_decrease_month": greatest_decrease_month,
        "months": months,
        "profit_loss_changes": profit_loss_changes
    }

# Get the absolute path to the CSV file
csv_file_path = Path("Resources/budget_data.csv").resolve()

# Calculate financial analysis
results = calculate_financial_analysis(csv_file_path)

# Print the results to the terminal
print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {results['total_months']}")
print(f"Total: ${results['total_profit_losses']}")
print(f"Average Change: ${results['average_change']:.2f}")
print(f"Greatest Increase in Profits: {results['greatest_increase_month']} (${results['greatest_increase']})")
print(f"Greatest Decrease in Profits: {results['greatest_decrease_month']} (${results['greatest_decrease']})")

# Print the 'months' and 'profit_loss_changes' lists in column format
print("\nMonths\tProfit/Loss Changes\n")
for month, change in zip(results['months'], results['profit_loss_changes']):
    print(f"{month}\t{change}\n")

# Export the results to a text file
with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-" * 28 + "\n")
    textfile.write(f"Total Months: {results['total_months']}\n")
    textfile.write(f"Total: ${results['total_profit_losses']}\n")
    textfile.write(f"Average Change: ${results['average_change']:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {results['greatest_increase_month']} (${results['greatest_increase']})\n")
    textfile.write(f"Greatest Decrease in Profits: {results['greatest_decrease_month']} (${results['greatest_decrease']})\n")

# Write the months and profit loss changes in column format 
    textfile.write("\nMonths\tProfit/Loss Changes\n")
    for month, change in zip(results['months'], results['profit_loss_changes']):
        textfile.write(f"{month}\t{change}\n")