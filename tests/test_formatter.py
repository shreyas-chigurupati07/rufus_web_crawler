import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rufus_formatter import save_as_json, save_as_csv

# Sample extracted data
extracted_data = [
    {
        "url": "https://tesla.com/model-x",
        "title": "Tesla Model X Plaid Features",
        "text": "The Model X Plaid has a 333-mile range, tri-motor setup, and advanced Autopilot."
    },
    {
        "url": "https://www.irs.gov/tax-policy",
        "title": "2025 Tax Policy Updates",
        "text": "The corporate tax rate is reduced to 18%, and low-income earners receive rebates."
    }
]

# Save as JSON
save_as_json(extracted_data, "tesla_tax_data.json")

# Save as CSV
save_as_csv(extracted_data, "tesla_tax_data.csv")