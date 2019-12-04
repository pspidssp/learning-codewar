#encoding:utf-8
song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
new = song.split('WUB')
new2 = []
for a in new :
    if a != '':
        new2.append(a)
' '.join(new2)
print(' '.join(new2))


#def song_decoder(song):
#   return " ".join(song.replace('WUB', ' ').split())