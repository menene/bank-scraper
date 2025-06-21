# parser.py
import pdfplumber
import pandas as pd
import re


def parse_pdf_transactions(pdf_file):
    transactions = []

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    # Coincide con: fecha, descripción, monto (positivo o negativo, con separador de miles)
                    match = re.match(
                        r"^(\d{4}-\d{2}-\d{2}) (.+?) ([+-]?[0-9,]+\.\d{2})$", line
                    )
                    if match:
                        date = match.group(1)
                        description = match.group(2).strip()
                        amount = float(match.group(3).replace(",", ""))
                        transactions.append(
                            {
                                "Fecha": date,
                                "Descripción": description,
                                "Monto (GTQ)": amount,
                            }
                        )

    return pd.DataFrame(transactions)
