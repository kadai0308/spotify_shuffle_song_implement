# try to implement the algorithm on: 
# https://labs.spotify.com/2014/02/28/how-to-shuffle-songs/

import random
import itertools
from functools import reduce

song_data = {
    "P!NK": 3,
    "Clean Bandit": 4,
    "Duo Lipa": 3,
    "Rixton": 1,
}

# give songs of singer a random distance(float)
def get_random_distence_between_songs(song_data):
    singer, song_amount = song_data
    result = [(singer, random.uniform(0, 100/song_amount), )]
    upper_bond = 100/song_amount - 5
    lower_bond = 100/song_amount + 5
    for index in range(1, song_amount):
        result.append((singer,  result[index-1][1] + random.uniform(upper_bond, lower_bond), ))
    return result

# shuffle the song by given distance
def shuffle_song(song_data):
    playlist = []
    # generate distance of each singer
    song_list_of_list = list(map(get_random_distence_between_songs, song_data.items()))
    # concat all songs set together
    playlist = list(reduce(itertools.chain, song_list_of_list))
    # sort it!
    playlist.sort(key=lambda song: song[1])
    return playlist

# show the playlist order with singer name
def display_playlist(ordered_data):
    print([i[0] for i in ordered_data])

display_playlist(shuffle_song(song_data))