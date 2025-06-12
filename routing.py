import json
from classification import classify_email
from parse_email import parse_email
import pandas as pd

SUPPORT_EMAIL = "support@aetheros.com"

def route_email(classified_email):
    product_types = classified_email.get("product_types", [])
    product_to_team = {
        "mercury language": "Mercury Language Team",
        "api development": "API Support Team",
        "iam service": "Security Team",
        "api monitoring": "Monitoring Team",
        "cloud management": "Cloud Services Team"
    }
    teams = []
    for product in product_types or []:
        team = product_to_team.get(product.lower(), "General Support Team")
        if team not in teams:
            teams.append(team)
    if not teams:
        teams.append("General Support Team")
    return {
        "teams": teams,
        "priority": classified_email.get("adjusted_criticality", "low"),
        "classified_type": classified_email.get("classified_type", "unknown"),
        "product_types": product_types,
        "thread_id": classified_email.get("thread_id", "")
    }

def simulate_api_call(routing_details, classified_email):
    sender = classified_email.get("sender", "").lower()
    if sender == SUPPORT_EMAIL:
        destination = [classified_email.get("receiver", "unknown receiver")]
    else:
        destination = routing_details["teams"]

    payload = {
        "subject": classified_email.get("subject", ""),
        "thread_id": classified_email.get("thread_id", ""),
        "teams": destination,
        "priority": routing_details.get("priority", "low"),
        "classified_type": routing_details.get("classified_type", "unknown"),
        "keywords": classified_email.get("keywords", [])
    }
    print("\nSimulating API call with payload:")
    print(json.dumps(payload, indent=4))

def simulate_auto_reply(classified_email, routing_details):
    if classified_email.get("sender", "").lower() == SUPPORT_EMAIL:
        return

    orig = classified_email.get("subject", "")
    if orig.lower().startswith("re:"):
        reply_subject = orig
    else:
        reply_subject = f"Re: {orig}"
    
    to_address = classified_email["sender"]
    body = f"""
Hi there,
Thanks for reaching out about your {classified_email.get('classified_type', 'request')}, particularly regarding {', '.join(classified_email.get('product_types', []))}.
We've routed your email to the following team(s): {', '.join(routing_details['teams'])} with a {routing_details['priority']} priority.
Our support team will get back to you shortly.
Best regards,
Customer Support Bot
""".strip()

    print("\nSimulating sending auto-reply:")
    print(f"To: {to_address}")
    print(f"Subject: {reply_subject}")
    print(body)

if __name__ == "__main__":
    df = pd.read_csv("dataset.csv")
    print("Processing sample emails...\n")

    for _, row in df.head(5).iterrows():
        parsed = parse_email(row)
        classified = classify_email(parsed)
        
        if classified.get("sender", "").lower() == SUPPORT_EMAIL:
            print(f"Skipping internal message: {classified['subject']}")
            print("-" * 40)
            continue

        routing_details = route_email(classified)

        print("Routing Details:")
        for k, v in routing_details.items():
            print(f"{k}: {v}")

        simulate_api_call(routing_details, classified)
        simulate_auto_reply(classified, routing_details)
        print("-" * 40)