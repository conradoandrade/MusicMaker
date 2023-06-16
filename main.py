import spotfy
import genaudio

def main():
    song_name, song_path = spotfy.get_song()  # Get song name and path
    print(song_name)
    print(song_path)
    descriptions = ['lofi  electro chill  ']  # Sample descriptions, change it according to your need
    print(descriptions)
    genaudio.generate_music_with_melody(song_path, descriptions)  # Generate music
    print("Done")

if __name__ == "__main__":
    main()
