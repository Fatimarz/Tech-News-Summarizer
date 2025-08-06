from email.message import EmailMessage
import smtplib
import json

def send_email():
    file_name = 'data/scraped_articles.json'

    with open(file_name, 'r') as f:
        articles = json.load(f)

    latest_articles = latest_articles[-4:]

    body = ''
    for item in articles:
        body += f"📰 Title: {item['Title']}\n\n📌 Summary: {item['Summary']}\n🔗 Link: {item['Link']}\n\n\n"

    msg = EmailMessage()
    msg['Subject'] = 'Tech Rewind: Weekly Wrap'
    msg['From'] = 'sender email'
    msg['To'] = 'receiver email'
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('sender email', 'app password')  # <-- App password
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email()