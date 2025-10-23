import pandas as pd
# read excel file
df = pd.read_excel('Sales_Data.xlsx')
#initialize total bonus
total_bonuses = 0
#Create heading
print("SALES PERFORMANCE REPORT")
print("="*25)
#Using loop through each row of the dataframe:
for employee_name, row in df.iterrows():
    employee_name = row['Employee_Name']
    monthly_sales = row['Monthly_Sales']
    sales_target = row['Sales_Target']
    #Check the condition for each employee:
    if monthly_sales >= sales_target:
        status = "MET"
        bonus_rate = 0.10  
    else:
        status = "NOT MET"
        bonus_rate = 0.05 
    #Calculate the bonus
    bonus = monthly_sales * bonus_rate
    total_bonuses += bonus
    #Print the employee's performance: 
    print(f"{employee_name}: Target {status} | Sales: ${monthly_sales:,} | Bonus: ${bonus:,.0f}")
#Print total Bonus to Pay:
print(f"\nTotal Bonuses to Pay: ${total_bonuses:,.0f}")
