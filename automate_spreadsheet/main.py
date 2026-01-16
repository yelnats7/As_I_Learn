import pandas
import sqlite3


# Creating a database
def setup_database(excel_file):
    dataframe = pandas.read_excel(excel_file, sheet_name = "Sheet1")

    dataframe["Total Inventory"] = dataframe["Inventory"] * dataframe["Price"]

    connection = sqlite3.connect("inventory.db")

    dataframe.to_sql("products", connection, if_exists = "replace", index = False)

    print("Database created, connected and data imported successfully")

    return connection

def sql_queries(connection):
    cursor = connection.cursor()

    print("--- Products per supplier ---")
    cursor.execute("SELECT Supplier, COUNT(*) FROM products GROUP BY Supplier")

    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]}")

    print("--- Inventory less than 10 ---")
    cursor.execute("SELECT [Product No], Inventory FROM products WHERE Inventory < 10")

    for row in cursor.fetchall():
        print(f"Product {row[0]} is low: {row[1]} left")
def main():
    connection = setup_database("inventory.xlsx")

    sql_queries(connection)

    connection.close()

if __name__ == "__main__":
    main()