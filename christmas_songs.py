from random import choice
print('Welcome to the Virtual Playlist.') ## Christmas is near!
start = input('It\'s nearly Christmas again. Ready for the holidays? ')


def main():
  if start.lower() == 'yes':
    def collect_songs():
      song_title = ''
      song_artist = ''
      songs = ()
      song_list = []
      while song_title.upper() != 'EXIT':
        song_title = input('\nEnter a song title or exit: ')
        if song_title.upper() == 'EXIT':
          print()
        else:
          song_artist = input('Enter a song artist or band: ')
          songs = (song_title, song_artist)
          song_list.append(songs)
      return song_list

    def play_song(songs):
      song = choice(songs)
      print(f'Now playing... \n{song[0]}, by: {song[1]} \n')
    
    def run_playlist(songs):
      how_many = int(input('How many songs? '))
      print()
      for song in range(how_many):
        play_song(songs)

    song_list = collect_songs()
    
    run_playlist(song_list)

  else:
    print('Goodbye. See you on Thanksgiving day, I guess...')


main()