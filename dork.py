import aiohttp
import asyncio
import random
import time
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        elif response.status == 429:
            print("Rate limit exceeded. Waiting to retry...")
            await asyncio.sleep(random.uniform(5, 15))  # Wait before retrying
            return await fetch_page(session, url)  # Retry the request
        else:
            print(f"Failed to retrieve page. Status code: {response.status}")
            return None

async def google_search(query, max_results=1000):
    search_url = "https://www.google.com/search?q={}&start={}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    results = []
    num_pages = max_results // 10  # Each page contains 10 results

    urls = [search_url.format(query, page * 10) for page in range(num_pages)]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_page(session, url))
            await asyncio.sleep(random.uniform(1, 3))  # Random sleep between requests

        pages = await asyncio.gather(*tasks)

        for page_content in pages:
            if page_content:
                soup = BeautifulSoup(page_content, 'html.parser')
                for g in soup.find_all('div', class_='g'):
                    link = g.find('a')
                    if link:
                        href = link.get('href')
                        results.append(href)

            # Stop if we've reached the desired number of results
            if len(results) >= max_results:
                break

    return results[:max_results]

def save_results_to_file(results, file_name="search_results.txt"):
    with open(file_name, "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")

if __name__ == "__main__":
    query = 'site:"instagram.com" "model" "new york" "@gmail.com"'
    results = asyncio.run(google_search(query, max_results=1000))
    save_results_to_file(results, "search_results.txt")
    print(f"Saved {len(results)} results to 'search_results.txt'")
