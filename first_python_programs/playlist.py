import os

playlist = {}  # dict
playlist['songs'] = []  # list of songs


def add_songs():
    add_songs = True  # enable to input songs flag
    msj = 'Do you want to add another song? Input s|n: '
    playlist_added_msj = 'Add songs into your ' + \
        playlist['playlist_name'] + ' playlist \n'

    while add_songs:
        print(playlist_added_msj)
        input_song_name = input('Song name: ')  # user input - song name

        if input_song_name:  # check user input - not empty input
            playlist['songs'].append(input_song_name)
        else:
            os.system('CLS')
            continue

        ctrl = input(msj).lower()  # user input - another song name

        if ctrl == 's' or ctrl == 'n':  # check user input - yes or not respectively
            if ctrl == 's':
                os.system('CLS')
                continue
            add_songs = not add_songs  # disable to input new songs names
        else:
            os.system('CLS')
            continue


def close_app():
    # closing app - no more songs to add
    closed_app_msj = 'Thanks for create your playlist'

    os.system('CLS')

    # acknowledgments and playlist info printed
    print(closed_app_msj + '\n')
    print('\tPlaylist: ' + playlist['playlist_name'])

    for song in playlist['songs']:
        print(f"\t\t. {song}")


# init function
def app():
    os.system('CLS')
    add_playlist = True  # enable to input the playlist flag
    welcome_msj = 'Welcome to spythify \n'

    print(welcome_msj)

    # adding a playlist
    while add_playlist:
        playlist['playlist_name'] = input(
            'Playlist name: ')  # user input - playlist name

        if not playlist['playlist_name']:  # check user input - empty input
            continue
        else:
            os.system('CLS')

        add_playlist = not add_playlist  # disable to input the playlist

    # adding songs to the playlist added
    add_songs()
    # close
    close_app()


if __name__ == '__main__':
    app()  # start app
