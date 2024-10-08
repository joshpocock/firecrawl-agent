import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from firecrawl import FirecrawlApp

# Load environment variables
load_dotenv()

def get_domain(url):
    """Extract the domain name from the URL without the top-level domain"""
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    if domain_parts[0] == 'www':
        domain = domain_parts[1]
    else:
        domain = domain_parts[0]
    return domain

def save_content(content, filename):
    """Save the content to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def scrape_website(url):
    try:
        # Initialize Firecrawl
        firecrawl_app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        
        # Scrape the website using Firecrawl
        result = firecrawl_app.scrape_url(url, params={'formats': ['markdown']})
        markdown_content = result.get('markdown', 'No content found')

        # Generate filename
        domain = get_domain(url)
        filename = f"{domain}.md"

        # Save content
        save_content(markdown_content, filename)

        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error scraping website: {str(e)}")

if __name__ == "__main__":
    website_url = input("Enter the website URL to scrape: ").strip()
    scrape_website(website_url)