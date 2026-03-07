import pandas as pd
import re
import argparse
import sys
import os

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_playlist(input_csv):
    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: Could not find file '{input_csv}'.")
        sys.exit(1)
        
    required_cols = ['Track Name', 'Artist Name(s)']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        print(f"Error: Input CSV is missing required columns: {', '.join(missing_cols)}")
        print(f"Available columns are: {', '.join(df.columns)}")
        sys.exit(1)
        
    records = []
    
    for _, row in df.iterrows():
        track_name = row['Track Name']
        artist_names = row['Artist Name(s)']
        
        first_artist = str(artist_names).split(';')[0] if pd.notna(artist_names) else ""
        

        clean_artist = clean_text(first_artist)
        clean_track = clean_text(track_name)
        

        query_parts = []
        if clean_artist:
            query_parts.append(clean_artist)
        if clean_track:
            query_parts.append(clean_track)
        query_parts.append("mp3")
            
        query = " ".join(query_parts)
        
        records.append({
            'Artist': clean_artist,
            'Track': clean_track,
            'Query': query
        })
        
    out_df = pd.DataFrame(records)
    output_file = 'search_queries.csv'
    out_df.to_csv(output_file, index=False)
    
    print(f"Successfully processed {len(records)} tracks.")
    print(f"Saved results to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate search queries from Spotify playlist data.")
    # Making the input_csv optional so the user can run standard script or provide a path
    parser.add_argument("input_csv", nargs='?', default="playlist.csv", help="Path to the input CSV file.")
    args = parser.parse_args()
    
    if not os.path.exists(args.input_csv):
        print(f"File '{args.input_csv}' not found. Please provide a valid CSV file path as an argument.")
        print("Usage: python generate_queries.py <your_file.csv>")
        sys.exit(1)
        
    process_playlist(args.input_csv)
