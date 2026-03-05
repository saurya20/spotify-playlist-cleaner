library(readr)
library(dplyr)

# Folder containing all playlist CSV files
folder_path <- "spotify_csvs/"

# Get all CSV files in folder
files <- list.files(folder_path, pattern = "*.csv", full.names = TRUE)

# Read and combine all CSV files
songs <- files |>
  lapply(read_csv) |>
  bind_rows()

# Clean dataset
songs_clean <- songs |>
  filter(!is.na(`Track Name`),
         !is.na(`Artist Name`)) |>
  distinct(`Track Name`, `Artist Name`, .keep_all = TRUE) |>
  mutate(search_query = paste(`Artist Name`, "-", `Track Name`))

# Save final dataset
write_csv(songs_clean, "output/final_music_library.csv")

# Also export simple search list
writeLines(songs_clean$search_query, "song_search_list.txt")

print("Cleaning complete!")