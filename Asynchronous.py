import asyncio

# Simulate an asynchronous task that fetches data (e.g., from an API)
async def fetch_data(url):
    print(f"Fetching data from {url}...")
    await asyncio.sleep(2)  # Simulates a delay like waiting for a web request
    print(f"Done fetching data from {url}")
    return f"Data from {url}"

# Simulate processing the fetched data
async def process_data(data):
    print(f"Processing {data}...")
    await asyncio.sleep(1)  # Simulate a short processing delay
    print(f"Done processing {data}")

# Main function to handle fetching and processing concurrently
async def main():
    # Define URLs to fetch data from
    urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]
    
    # Create tasks to fetch data from all URLs concurrently
    fetch_tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    
    # Wait for all fetch tasks to complete and get the fetched data
    fetched_data = await asyncio.gather(*fetch_tasks)
    
    # Create tasks to process the fetched data concurrently
    process_tasks = [asyncio.create_task(process_data(data)) for data in fetched_data]
    
    # Wait for all process tasks to complete
    await asyncio.gather(*process_tasks)

# Run the main asynchronous function
asyncio.run(main())
