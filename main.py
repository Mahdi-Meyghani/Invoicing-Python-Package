from invoicing import generate

generate("invoices", "output", "logo.png",
                 "product_id", "product_name", "amount_purchased",
                 "price_per_unit", "total_price")