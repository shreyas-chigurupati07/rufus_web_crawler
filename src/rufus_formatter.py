import json
import pandas as pd
import pdfkit
import markdown2

def save_as_json(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved as JSON: {filename}")

def save_as_csv(data, filename="output.csv"):
    if not data:
        print("No data to save!")
        return
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Data saved as CSV: {filename}")


# def save_as_pdf(data, filename="output.pdf"):
#     html_content = markdown2.markdown(json.dumps(data, indent=4))
#     pdfkit.from_string(html_content, filename)