# Imports
import psycopg2
import os
from datetime import datetime as dt, timedelta
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# Define constants
## Database Connection Details
DB_HOST = os.getenv('DB_SCRIPT_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')

## Email Configuration
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_FROM_PASSWORD = os.getenv('EMAIL_FROM_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT')

# Functions
## connect to database
def connect(db_host, db_name, db_user, db_password):
    conn = psycopg2.connect( host=db_host, database=db_name, user=db_user, password=db_password)
    return conn

## Retrieve Items from Database
def fetch_new_entries():
    # calculate 24 hours ago
    twenty_four = dt.now() - timedelta(days=1)

    # connect to Postgres Database
    conn = connect(DB_HOST, DB_NAME, DB_USER, DB_PASS)
    try:
        cursor = conn.cursor()

        # Fetch new entries from last 24 hours
        query = "SELECT * FROM waitlist WHERE created >= %s;"
        cursor.execute(query, (twenty_four,))
        new_entries = cursor.fetchall()

        return new_entries
    
    # exception handling
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    
    # close database connections
    finally:
        if conn:
            cursor.close()
            conn.close()

## Send email
def send_email(new_entries):
    # prepare email content
    body = "New Waitlist Entries in the past 24 hours:\n\n"
    for entry in new_entries:
        body += f"{entry}\n"

    # create message content
    msg = MIMEText(body)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    # send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_FROM_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print("Email send successfully!")
    
    # exception handling
    except Exception as e:
        print(f"Error sending email: {e}")


# Main Function
def main():
    new_entries = fetch_new_entries()
    if new_entries:
        send_email(new_entries)
    else:
        print("No new waitlist entries found.")

# Main Function call:
if __name__ == "__main__":
    main()