import pandas as pd
# # Load Excel file
# df = pd.read_excel('Financial_Sample.xlsx')
# # Show the first few rows
# print(df)
# total = df['Units Sold'].sum
# print(total)

# sum = df.select_dtypes(include='number').sum()
# print(sum)

# df_with_total = pd.concat([df,pd.DataFrame([sum])], ignore_index=True)

# print(df_with_total)

# df_with_total.to_excel("Financial_Sample.xlsx",index=False)
 df = pd.read_excel('Sales_Data.xlsx')
total_bonuses = 0

# Print the report header
print("SALES PERFORMANCE REPORT")
print("========================")

# Loop through each row in the dataframe
for index, row in df.iterrows():
    employee_name = row['Employee_Name']
    monthly_sales = row['Monthly_Sales']
    sales_target = row['Sales_Target']

    # Check if the employee met the sales target
    if monthly_sales >= sales_target:
        status = "MET"
        bonus_rate = 0.10  # 10% bonus
    else:
        status = "NOT MET"
        bonus_rate = 0.05  # 5% bonus

    # Calculate the bonus
    bonus = monthly_sales * bonus_rate
    total_bonuses += bonus

    # Print the employee's performance details
    print(f"{employee_name}: Target {status} | Sales: ${monthly_sales:,} | Bonus: ${bonus:,.2f}")

# Print the total bonuses to be paid
print("\nTotal Bonuses to Pay: ${:,.2f}".format(total_bonuses))