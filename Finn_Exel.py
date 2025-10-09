import pandas as pd
# Load Excel file
df = pd.read_excel('Financial_Sample.xlsx')
# Show the first few rows
print(df)
total = df['Units Sold'].sum
print(total)

sum = df.select_dtypes(include='number').sum()
print(sum)

df_with_total = pd.concat([df,pd.DataFrame([sum])], ignore_index=True)

print(df_with_total)

df_with_total.to_excel("Financial_Sample.xlsx",index=False)