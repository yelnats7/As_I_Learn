import pandas
import csv

# Covert excel file to csv file
def convert_excel(excel_filename):
    excel_file = pandas.read_excel(str(excel_filename), sheet_name = "Sheet1")
    csv_file = excel_file.to_csv("temp.csv", index = False)
    
    return "temp.csv"


def main():
    csv_file = convert_excel("inventory.xlsx")
    with open(csv_file, mode = "r", newline = "") as input_file, open("updated_file.csv", mode = "w", newline = "") as output_file:
        reader = csv.DictReader(input_file)
        new_fieldnames = reader.fieldnames + ["Total Inventory"]

        writer = csv.DictWriter(output_file, fieldnames = new_fieldnames)
        writer.writeheader()
        
        product_count_per_company = {}
        product_inventory_less_10 = {}

        for row in reader:
            # Calculate the product per company
            if row["Supplier"] in product_count_per_company:
                product_count_per_company[row["Supplier"]] = product_count_per_company[row["Supplier"]] + 1
            else:
                product_count_per_company[row["Supplier"]] = 1

            
            # Calculate product with inventory less than 10
            if int(row["Inventory"]) < 10:
                product_inventory_less_10[row["Product No"]] = int(row["Inventory"])

            total_inventory = int(row["Inventory"]) * float(row["Price"])
            row["Total Inventory"] = total_inventory
            writer.writerow(row)

main()