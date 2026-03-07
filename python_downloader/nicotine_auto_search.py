import pandas as pd
import urllib.parse
import webbrowser
import time
import os
import sys

def main():
    csv_file = "spotify-playlist-cleaner\output"
    
    if not os.path.exists(csv_file):
        print(f"Error: Could not find '{csv_file}'. Please run generate_queries.py first.")
        sys.exit(1)

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    if 'Query' not in df.columns:
        print("Error: The CSV does not contain a 'Query' column.")
        sys.exit(1)

    # Get all valid queries
    queries = df['Query'].dropna().tolist()
    total_queries = len(queries)

    print(f"Found {total_queries} queries. Starting automated search in Nicotine+...\n")

    for i, query in enumerate(queries, 1):
        print(f"[{i}/{total_queries}] Executing search: {query}")
        
        # URL safe encoding (replaces spaces with %20, etc.)
        encoded_query = urllib.parse.quote(str(query))
        slsk_url = f"slsk://search/{encoded_query}"
        
        # Open the link via webbrowser module
        # This will securely prompt Nicotine+ to handle the slsk:// protocol
        webbrowser.open(slsk_url)
        
        # Wait 2 seconds between searches to prevent flooding Nicotine+
        if i < total_queries:
            time.sleep(2)

    print("\nFinished sending all search queries.")

if __name__ == "__main__":
    main()
