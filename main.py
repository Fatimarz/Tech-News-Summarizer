import scraped
import summaries
import send_email

def run_pipeline():
    print('starting to scrape')
    scraped.scrape()
    print('scraping completed !!')
    print('Summarizing the results')
    summaries.summarize()
    send_email.send_email()
    print('Email Sent')


if __name__ == "__main__":
    run_pipeline()