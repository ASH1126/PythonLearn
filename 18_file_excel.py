import pandas as pd

file = pd.ExcelFile("sales.xlsx")

print(file.sheet_names)

sheet = file.parse("sales")
print(sheet, "\n", type(sheet))
print(sheet.Date)
print(sheet.Amount.sum())
print(sheet.loc[0])
print(sheet.loc[0, "Amount"])

sheet.set_index("Customer", inplace=True)
print(sheet.loc["MMC Inc."])

sheet = sheet.reset_index()

print(sheet["Invoice"], "\n", type(sheet["Invoice"]))

print(sheet.loc[sheet["Invoice"] == 99])
print(sheet.loc[sheet["Amount"] > 2000])
print(sheet.loc[sheet["Amount"].idxmax()])
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])
print(sheet.loc[sheet["Amount"] > 1800])
print(sheet.loc[sheet["Amount"] > 1800]["Customer"])
print(sheet.loc[sheet["Amount"] > 1800]["Customer"].unique())

for customer in sheet.loc[sheet["Amount"] > 1800]["Customer"].unique():
    print(customer)
