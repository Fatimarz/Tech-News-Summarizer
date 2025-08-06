import json
from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text_bart(text, max_length=180, min_length=100, do_sample=True):
    inputs = tokenizer.batch_encode_plus([text], return_tensors="pt", max_length=1024, truncation=True)
    
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        do_sample=do_sample
    )
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize():
    with open('data/scraped_articles.json','r') as file:
        articles_data = json.load(file)

    for article in articles_data:
        if 'Summary' not in article or not article['Summary'].strip():  # Avoid duplicating
            article_text = article['Article']
            summary = summarize_text_bart(article_text)
            article['Summary'] = summary

    with open("data/scraped_articles.json", "w") as f:
        json.dump(articles_data, f, indent=4)

if __name__ == "__main__":
    summarize()