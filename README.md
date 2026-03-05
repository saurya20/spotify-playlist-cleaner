# spotify-playlist-cleaner

Small R script I wrote because exporting playlists from Spotify quickly becomes messy if you’re doing it a lot.

I was exporting multiple playlists and liked songs as CSV files and ended up with a bunch of duplicates across files. This script just merges everything, removes duplicates, and creates a clean list of songs that can be used for building a local music library.

---

## What it does

* Reads **all Spotify playlist CSV exports** from a folder
* Combines them into a single dataset
* Removes duplicate songs
* Filters out incomplete rows
* Generates a simple `Artist - Track` search string
* Exports a **clean dataset** and a **search list**

---

## Example workflow

1. Export playlists from Spotify using a tool like Exportify
2. Put all CSV files in a folder
3. Run the script

The script will generate:

```
final_music_library.csv
song_search_list.txt
```

`song_search_list.txt` is just a simple list like:

```
Arctic Monkeys - Do I Wanna Know
Frank Ocean - Nights
Daft Punk - Get Lucky
```

Useful if you're building a local music library or using other tools to fetch tracks.

---


## Requirements

R packages:

```
readr
dplyr
```

Install if needed:

```r
install.packages(c("readr", "dplyr"))
```

---

## Running the script

Edit the folder path if needed:

```r
folder_path <- "spotify_csvs/"
```

Then run:

```r
source("clean_playlists.R")
```

---

## Why I made this

Mostly because I wanted to clean up playlist exports before using them to build a local music collection. Doing it manually gets annoying once you have a lot of playlists.

This just automates the boring part.
