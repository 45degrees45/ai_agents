# Save this as web_scraper_llm.py
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

st.title("Simple Web Scraper with LLM Integration")
st.caption("Extract information from websites using powerful large language models")

# Get the API key
api_key = st.text_input("Enter your API Key", type="password")

# Get the URL to scrape
url = st.text_input("Enter the URL to scrape", placeholder="https://en.wikipedia.org/wiki/Artificial_intelligence")

# Get the user's question
question = st.text_input("What information would you like to extract?", 
                         placeholder="Extract the definition and key applications")

# Function to scrape the website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the text content, removing script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        
        text = soup.get_text()
        
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:15000]  # Limit to 15k characters to fit in context window
    except Exception as e:
        return f"Error scraping the website: {str(e)}"

# Function to query LLM API
def query_llm(content, question, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that extracts specific information from web content."},
            {"role": "user", "content": f"I have the following web content:\n\n{content}\n\nBased on this content, please {question}"}
        ],
        "temperature": 0.1,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error querying LLM API: {str(e)}"

# Process when the button is clicked
if st.button("Extract Information"):
    if not api_key:
        st.error("Please enter your API key")
    elif not url:
        st.error("Please enter a URL to scrape")
    elif not question:
        st.error("Please enter what information you want to extract")
    else:
        with st.spinner("Scraping the website..."):
            content = scrape_website(url)
            
        if content.startswith("Error"):
            st.error(content)
        else:
            st.success("Website scraped successfully!")
            
            with st.spinner("Extracting information using LLM..."):
                answer = query_llm(content, question, api_key)
                
            if answer.startswith("Error"):
                st.error(answer)
            else:
                st.subheader("Extracted Information:")
                st.write(answer)

# Add some examples
with st.expander("Example URLs and Questions"):
    st.markdown("""
    **Example URLs:**
    - https://en.wikipedia.org/wiki/Artificial_intelligence
    - https://news.ycombinator.com/
    - https://www.mathrubhumi.com/news/kerala
    
    **Example Questions:**
    - Extract the definition of AI and list 3 key applications
    - Find the top 5 news headlines and summarize each in one sentence
    - What are the main news topics from Kerala today?
    """)
