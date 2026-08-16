import os
import smtplib
from email.message import EmailMessage

import snowflake.connector
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization

# Load Gmail credentials from .env
load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# Snowflake settings
SNOWFLAKE_ACCOUNT = "CVXGZRX-XB16286"
SNOWFLAKE_USER = "MADHURIDUDDUPUDI"
SNOWFLAKE_DATABASE = "ATMOSYNC_DB"
SNOWFLAKE_SCHEMA = "WAREHOUSE"
SNOWFLAKE_WAREHOUSE = "ATMOSYNC_WH"
SNOWFLAKE_ROLE = "ACCOUNTADMIN"

PRIVATE_KEY_PATH = r"C:\Users\madhu\Desktop\Atmosync_realtime_project\snowflake_key.p8"


def load_private_key():
    with open(PRIVATE_KEY_PATH, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    return private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )


def get_high_priority_records():
    private_key = load_private_key()

    conn = snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        private_key=private_key,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        warehouse=SNOWFLAKE_WAREHOUSE,
        role=SNOWFLAKE_ROLE
    )

    cursor = conn.cursor()

    query = """
        SELECT
            CONTAINER_ID,
            CARGO_TYPE,
            ORIGIN,
            DESTINATION,
            TEMPERATURE,
            SPOILAGE_RISK,
            PRIORITY_LEVEL,
            SPOILAGE_ARBITRAGE_SCORE,
            RECOMMENDED_ACTION,
            ALERT_STATUS,
            TIMESTAMP
        FROM TELEMETRY_ANALYTICS
        WHERE PRIORITY_LEVEL = 'HIGH PRIORITY'
        ORDER BY TIMESTAMP DESC
        LIMIT 10
    """

    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records


def send_email(records):
    if not records:
        print("No HIGH PRIORITY alerts found.")
        return

    message = EmailMessage()
    message["Subject"] = "🚨 AtmoSync High Priority Container Alert"
    message["From"] = GMAIL_ADDRESS
    message["To"] = GMAIL_ADDRESS

    body = "AtmoSync detected HIGH PRIORITY container alerts.\n\n"

    for record in records:
        (
            container_id,
            cargo_type,
            origin,
            destination,
            temperature,
            spoilage_risk,
            priority,
            arbitrage_score,
            recommended_action,
            alert_status,
            timestamp
        ) = record

        body += f"""
Container ID: {container_id}
Cargo Type: {cargo_type}
Route: {origin} → {destination}
Temperature: {temperature}
Spoilage Risk: {spoilage_risk}
Priority: {priority}
Arbitrage Score: {arbitrage_score}
Alert Status: {alert_status}
Recommended Action: {recommended_action}
Timestamp: {timestamp}
----------------------------------------
"""

    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(message)

    print("Email alert sent successfully.")


if __name__ == "__main__":
    records = get_high_priority_records()
    print(f"Found {len(records)} HIGH PRIORITY records.")

    send_email(records)