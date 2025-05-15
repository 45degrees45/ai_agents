# Web Scraper with LLM Integration

A Streamlit application that scrapes websites and uses large language models to extract and analyze specific information based on user queries.

## Features

- Web scraping using BeautifulSoup
- Integration with LLM API (compatible with Groq API)
- Simple and intuitive user interface
- Text processing and cleanup for better LLM comprehension
- Context window management for large web pages

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/web-scraper-llm.git
   cd web-scraper-llm
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run web_scraper_llm.py
   ```

## Usage

1. Enter your API key (you'll need to sign up for an API key from [Groq](https://groq.com) or use another compatible LLM API)
2. Enter the URL of the website you want to scrape
3. Enter a question about what information you want to extract
4. Click "Extract Information" to process the request

## Example Queries

- **URL**: https://en.wikipedia.org/wiki/Artificial_intelligence
  **Question**: Extract the definition of AI and list 3 key applications

- **URL**: https://news.ycombinator.com/
  **Question**: Find the top 5 news headlines and summarize each in one sentence

- **URL**: https://www.mathrubhumi.com/news/kerala
  **Question**: What are the main news topics from Kerala today?

## Security Note

This application requires an API key to function. Please keep your API key secure and never commit it to version control.

## Limitations

- The application limits scraped content to 15,000 characters to fit within typical LLM context windows
- Some websites may block scraping attempts
- Results are dependent on the quality of the LLM responses

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
