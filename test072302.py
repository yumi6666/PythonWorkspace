# -*- coding:utf-8 -*-

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["The 1st lyric",
                   "The 2nd lyric",
                   "The 3rd lyric"])


bulls_on_parade = Song(["The 4th lyric","The 5th lyric"])        

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
