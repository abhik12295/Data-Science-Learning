'''
Real-world Example: Multi-threading for I/O outbound Tasks
Scenario = Web Scraping
Web scraping generally involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of time
waiting for the responses from servers. 
Multithreading can significantly improve the performance by allowing multiple 
web pages to fetched concurrently.
'''

# https://python.langchain.com/docs/introduction/
# https://python.langchain.com/v0.2/docs/introduction/

# https://python.langchain.com/docs/concepts/
# https://python.langchain.com/v0.2/docs/concepts/

# https://python.langchain.com/docs/tutorials/
# https://python.langchain.com/v0.2/docs/tutorials/

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/'
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetches")