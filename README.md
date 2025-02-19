# Invoicing-Python-Package
> excel-invoice-to-pdf


## Overview

`excel-invoice-to-pdf` is a Python package that allows users to easily convert Excel invoices into PDF format. This package supports the processing of multiple Excel files stored in a directory, converting them into PDFs with the same filenames as the original Excel files. The PDF invoices include a company logo and display the total price of the products in a neatly formatted table. 

This package is available on PyPI, and you can install it using:

```bash
pip install excel-invoice-to-pdf
```
## Features
- Converts multiple Excel invoices into PDFs.
- Preserves the exact names of the original Excel files in the generated PDFs.
- Includes a company logo on each invoice.
- Displays essential details like invoice number, date, and total price in the PDF.
- Automatically creates the destination directory for PDF files if it does not exist.
- Licensed under the MIT License.

## Installation
To install the package, simply run:
```bash
pip install excel-invoice-to-pdf
```

## Usage
After installing the package, you can import and use it in your Python project as follows:

```python
import invoicing
# or
from invoicing import invoice
```

## Example Usage
The `invoice` module contains a `generate` function that converts Excel invoices into PDF files. Here is how you can use it:
```python
from invoicing import invoice

invoice.generate(
    invoices_path="path_to_excel_invoices_folder",
    pdfs_path="path_to_output_pdfs_folder",
    logo_image_path="path_to_company_logo_image",
    product_id_col="Product ID",
    product_name_col="Product Name",
    amount_purchased_col="Amount Purchased",
    price_per_unit_col="Price per Unit",
    total_price_col="Total Price"
)
```

## Parameters
- `invoices_path`: The directory where Excel invoice files are stored.
- `pdfs_path`: The directory where the generated PDF invoices will be stored.
- `logo_image_path`: The path to the company logo image file to be included in the PDFs.
- `product_id_col`: The column name in the Excel files containing the product IDs.
- `product_name_col`: The column name in the Excel files containing the product names.
- `amount_purchased_col`: The column name in the Excel files containing the quantities of purchased products.
- `price_per_unit_col`: The column name in the Excel files containing the price per unit.
- `total_price_col`: The column name in the Excel files containing the total price of products.

The function will process all Excel files in the specified invoices_path, generate PDFs with the same names as the Excel files, and save them in the pdfs_path folder. If the pdfs_path directory does not exist, it will be created automatically.

## License
This package is open-source and available under the MIT License.

## Contribute

Developers are welcome to contribute, suggest new features, or report issues. 

To contribute:

1. Fork the repository.
2. Create a new branch with your feature or fix.
3. Submit a pull request for review.

You can check out the source code and additional documentation on PyPI:

[excel-invoice-to-pdf on PyPI](https://pypi.org/project/excel-invoice-to-pdf/)

[excel-invoice-to-pdf on Github](https://github.com/Mahdi-Meyghani/Invoicing-Python-Package/)

Feel free to contribute and help improve the package!

Enjoy using `excel-invoice-to-pdf`!

