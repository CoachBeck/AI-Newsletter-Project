from getNews import fetch_articles
from summarizeArticles import summarize_article
from emailSender import send_email

def run_newsletter():
    articles = fetch_articles(query="technology", num_articles=3)
    email_body_lines = ["🗞️ AI-Powered News Summary (Reuters)", ""]

    for i, article in enumerate(articles):
        try:
            summary = summarize_article(article["content"])
        except Exception as e:
            summary = f"⚠️ Failed to summarize article: {e}"

        email_body_lines.append(f"{i+1}. {article['title']}")
        email_body_lines.append(summary)
        email_body_lines.append(f"Source: {article['url']}")
        email_body_lines.append("")  # Add blank line for spacing

    email_body = "\n".join(email_body_lines)
    send_email("AI-Powered Daily News Summary", email_body)
    print("✅ Newsletter sent!")

if __name__ == "__main__":
    run_newsletter()
