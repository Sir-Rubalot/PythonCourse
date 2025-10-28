playlist = []

def add_song(playlist):
    song_to_add = input("add song: ")
    if song_to_add == "":
        print("Title is empty")
    else:
        playlist.append(song_to_add)
        print("Song successfully added")

def remove_song(playlist):
    if len(playlist) == 0:
        print("playlist is empty")
        return
    
    show_playlist(playlist)
    
    print("---PLAYLIST---")
    for i, song in enumerate(playlist, start=1):
        print(f"{i}: {song}")

    song_to_remove = (input("What song do you want to remove?: ")).strip()
    if not song_to_remove.isdigit():
        print("Not a number!!!")

    song_number = int(song_to_remove)
    if song_number < 1 or song_number >len(playlist):
        print("Not in range of playlist, idiot")

    removed_song = playlist.pop(song_number - 1)
    print (f"success! Removed song {removed_song}")

def show_playlist(playlist):

    if len(playlist) == 0:
        print("Playlist is empty")

    print("---PLAYLIST---")
    for i, song in enumerate(playlist, start=1):
        print(f"{i}: {song}")

def main():
    while True:
        print("===My Playlist===")
        print("1) Show playlist")
        print("2) Add song to playlist")
        print("3) Remove song from playlist")
        print("0) Exit menu")
        user_choice = input(">: ").strip()

        if user_choice == "1":
            show_playlist(playlist)
        elif user_choice == "2":
            add_song(playlist)
        elif user_choice == "3":
            remove_song(playlist)
        elif user_choice == "0":
            break
        else:
            print("Invalid choice")

main()