# AI-Powered News Newsletter

This project automates the process of fetching real news, summarizing articles using OpenAI GPT-4, and sending a daily email newsletter.

## Features
- Fetches current articles from NewsAPI
- Summarizes content using GPT-4
- Sends formatted summaries via email

## Technologies Used
- Python 3
- OpenAI API
- NewsAPI
- SMTP (Gmail)
- dotenv for credential handling

## Setup Instructions
1. Clone this repo
2. Create a `.env` file with:
    ```
    OPENAI_API_KEY=your_key
    NEWS_API_KEY=your_key
    EMAIL_ADDRESS=you@example.com
    EMAIL_PASSWORD=your_app_password
    TO_EMAIL=recipient@example.com
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    python main.py
    ```
