import pandas as pd
import ast

def parse_email(row):
    parsed_email = {}
    parsed_email['subject'] = row['subject'].strip()
    parsed_email['message_body'] = row['message_body'].strip()
    parsed_email['thread_id'] = row['thread_id'].strip()
    parsed_email['sender'] = row['sender'].strip()
    parsed_email["receiver"] = row["receiver"].strip()


    if isinstance(row['email_types'], str):
        parsed_email['email_types'] = ast.literal_eval(row['email_types'])
    else:
        parsed_email['email_types'] = row['email_types']

    parsed_email['email_status'] = row['email_status'].strip()
    parsed_email['email_criticality'] = row['email_criticality'].strip()

    if isinstance(row['product_types'], str):
        parsed_email['product_types'] = ast.literal_eval(row['product_types'])
    else:
        parsed_email['product_types'] = row['product_types']

    parsed_email['agent_effectivity'] = row['agent_effectivity'].strip()
    parsed_email['agent_efficiency'] = row['agent_efficiency'].strip()
    parsed_email['customer_satisfaction'] = float(row['customer_satisfaction'])

    parsed_email['is_reply'] = parsed_email['subject'].startswith("Re:")

    parsed_email['adjusted_criticality'] = parsed_email['email_criticality']

    return parsed_email

def main():
    df = pd.read_csv("dataset.csv")

    print("Parsing sample emails...\n")
    for index, row in df.head(5).iterrows():
        parsed = parse_email(row)
        print("Parsed Email:")
        for key, value in parsed.items():
            print(f"{key}: {value}")
        print("-" * 40)

if __name__ == "__main__":
    main()