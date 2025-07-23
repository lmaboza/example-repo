# Inventory Management System (Python + PowerShell)

This project contains two scripts developed as part of a practical task:

- A PowerShell script (`file_cd.ps1`) for creating and manipulating directories.
- A Python inventory management system (`inventory.py`) that reads from and writes to a text file (`inventory.txt`).

---

# PowerShell Script: `file_cd.ps1`

This script performs the following:
- Creates three top-level folders.
- Navigates into one of them and creates three more subfolders.
- Deletes two of the top-level folders.

This demonstrates basic PowerShell operations such as directory creation, navigation, and deletion.

---

# Python Script: `inventory.py

A text-based inventory management system that:

- Reads product data from a file (`inventory.txt`).
- Allows adding new shoes to the inventory.
- Displays all products neatly.
- Identifies the product with the lowest quantity and allows restocking.
- Searches for a product by its code.
- Calculates the total value per item.
- Identifies the product with the highest quantity and marks it for sale.

# inventory.txt Format:
```txt
Country,Code,Product,Cost,Quantity
South Africa,SKU001,Nike Air,1200,50
USA,SKU002,Adidas Ultra,1500,35
