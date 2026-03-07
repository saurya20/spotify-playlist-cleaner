library(readr)
library(dplyr)

folder_path <- "spotify_csvs/"

files <- list.files(folder_path, pattern = "*.csv", full.names = TRUE)

songs <- files |>
  lapply(function(file) read_csv(file, show_col_types = FALSE)) |>
  bind_rows()

songs_clean <- songs |>
  filter(!is.na(`Track Name`), !is.na(`Artist Name(s)`)) |>
  distinct(`Track Name`, `Artist Name(s)`, .keep_all = TRUE) |>
  mutate(
    `Artist Name(s)` = gsub(";", ", ", `Artist Name(s)`),
    search_query = paste(`Artist Name(s)`, "-", `Track Name`)
  )

write_csv(songs_clean, "output/final_music_library.csv")
writeLines(songs_clean$search_query, "output/song_search_list.txt")

print(nrow(songs_clean))
