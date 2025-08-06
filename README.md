## Goal: 
The goal of this project is to stay updated with the latest tech news without spending too much time reading full articles. It scrapes the latest articles from ZDNet, summarizes them using NLP techniques, and sends a concise weekly email digest — perfect for busy tech enthusiasts who want quick, readable updates in their inbox.

## Features
* Extracts the latest tech articles from ZDNet using Python and BeautifulSoup.
* Summarizes long-form articles into concise, readable points using NLP techniques.
* Sends summarized news via email on a scheduled basis.
* Runs automatically every week using Task Scheduler to ensure consistent updates.

## 🛠 Tech Stack 
* Python – Core programming language
* BeautifulSoup & Requests – For web scraping ZDNet articles
* NLTK / Transformers – For text summarization using NLP
* smtplib – For sending emails via SMTP
* JSON – To store and structure article data
* Task Scheduler – To automate weekly execution (Windows)

## ⚙️ Installation & Setup
1. Clone the repository
   
    `git clone https://github.com/Fatimarz/Tech-News-Summarizer.git`

     `cd tech-news-summarizer`

 2. Install dependencies

     `pip install -r requirements.txt`

3. Set up email configuration

    `SENDER_EMAIL=your_email@gmail.com`
    `APP_PASSWORD=your_app_password`

4. Run the script

    `python main.py`

5. Schedule weekly automation
Use Windows Task Scheduler (or cron on Linux/macOS) to schedule main.py to run weekly.


