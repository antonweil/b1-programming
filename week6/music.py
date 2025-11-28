songs = []
genre_count = {}


for x in range(5):
    song = input("Song: ")
    genre = input("Genre: ")
    song_tuple = (song, genre)
    songs.append(song_tuple)
    genre_count[genre] = genre_count.get(genre, 0) + 1

for index,(name, genre) in enumerate(songs,1):
    print(f"{index}: {name} {genre}")

for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")

popular = max(genre_count, key=genre_count.get)
print(f"most popular genre: {popular}")