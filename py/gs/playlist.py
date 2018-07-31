def playlist(songs):
    """
    OA
    Music Playlist Full-Minute Dilemma
    [20, 40, 60, 120, 3]=>[(20, 40), (60, 120)]=>2 pairs
    """
    song_dict={}
    count=0
    for i in range(0, len(songs)):
        songs[i]=songs[i]%60
        if songs[i] in song_dict:
            song_dict[songs[i]]+=1
        else:
            song_dict[songs[i]]=1
    for i in range(0, len(songs)):
        complement=60-songs[i]
        if songs[i]==0:
            complement=0
        if complement in song_dict:
            count+=song_dict[complement]
            if complement==songs[i]:
                count-=1
            song_dict[songs[i]]-=1
    return count
test_playlist=[4, 10, 50, 90, 30]
print playlist(test_playlist)