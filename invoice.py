import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path
import os


def generate(invoices_path, pdfs_path, logo_image_path, product_id_col, product_name_col,
             amount_purchased_col, price_per_unit_col, total_price_col):

    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        pdf = FPDF(orientation="L", unit="mm", format="A4")

        filename = Path(filepath).stem
        invoice_nr, date_nr = filename.split("-")

        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Date {date_nr}")
        pdf.ln(20)

        df = pd.read_excel(filepath)
        columns = df.columns
        columns = [title.replace("_", " ").title() for title in columns]

        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(80, 80, 80)

        pdf.cell(w=30, h=16, txt=columns[0], border=1)
        pdf.cell(w=70, h=16, txt=columns[1], border=1)
        pdf.cell(w=40, h=16, txt=columns[2], border=1)
        pdf.cell(w=30, h=16, txt=columns[3], border=1)
        pdf.cell(w=30, h=16, txt=columns[4], border=1, ln=1)

        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=16)
            pdf.set_text_color(80, 80, 80)

            pdf.cell(w=30, h=16, txt=str(row[product_id_col]), border=1)
            pdf.cell(w=70, h=16, txt=str(row[product_name_col]), border=1)
            pdf.cell(w=40, h=16, txt=str(row[amount_purchased_col]), border=1)
            pdf.cell(w=30, h=16, txt=str(row[price_per_unit_col]), border=1)
            pdf.cell(w=30, h=16, txt=str(row[total_price_col]), border=1, ln=1)

        total_price = df[total_price_col].sum()

        pdf.set_font(family="Times", size=16)
        pdf.cell(w=30, h=16, txt="", border=1)
        pdf.cell(w=70, h=16, txt="", border=1)
        pdf.cell(w=40, h=16, txt="", border=1)
        pdf.cell(w=30, h=16, txt="", border=1)
        pdf.cell(w=30, h=16, txt=str(total_price), border=1, ln=1)
        pdf.ln(20)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=30, h=16, txt=f"Total price is: {total_price}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=45, h=16, txt="Amazon Shopping")

        pdf.image(logo_image_path, w=18, h=18)

        os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")
