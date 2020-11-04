import random
from entities.location import Location
from collections import Counter

import math
class Chat_main():
    def __init__(self, start, chat_id, chat_name, online):
        self.start = start
        self.game_begin = False
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.game_for_online = online
        self.list_of_list_with_roles = []
        self.current_object_of_roles = None
        self.current_location = ""
        self.list_of_players = []
        self.list_of_admins = []
        self.id_of_kills_buttons_message = None
        self.spy_name = ""
    def get_roles(self):
        if any(True == i.in_game for i in self.current_object_of_roles.list_of_location):
            while True:
                a = random.randint(0, len(self.current_object_of_roles.list_of_location) - 1)
                if self.current_object_of_roles.list_of_location[a].in_game:
                    for player in self.list_of_players:
                        player.current_role = self.current_object_of_roles.list_of_location[a]
                        self.current_location = self.current_object_of_roles.list_of_location[a].name
                    break
            b = random.randint(0, len(self.list_of_players) - 1)
            self.list_of_players[b].current_role = Location("Шпион", "images/spy.jpg")


    def kill_guy(self):

        def count_of_time_vote_player(list_a):
            skoka_est = 0
            for i in list_a:
                if i != '':
                    skoka_est +=1
            return skoka_est
        count_of_player = len(self.list_of_players)
        skoka_nado = math.floor((count_of_player) / 2)+1 #2 голоса
        time_vote_player = []
        for player in self.list_of_players:
            time_vote_player.append(player.vote)
        if  count_of_time_vote_player(time_vote_player)>= skoka_nado: # Надо найти все повторы,
            for vote in time_vote_player:
                c =  Counter(time_vote_player)
                if c[vote] == skoka_nado:
                    for ide,player_2 in enumerate(self.list_of_players):
                        if player_2.name == vote:
                            if self.list_of_players[ide].current_role.name != 'Шпион':
                                a = "mir",self.list_of_players[ide].id,self.list_of_players[ide].name
                                self.list_of_players.pop(ide)
                                return a
                            else:
                                return "spy",self.list_of_players[ide].id

                    break
        #print(self.list_of_players)
        #print(skoka_nado,"skoka_nado")
        #print(count_of_time_vote_player(time_vote_player),"sko_ko est")
        #print(time_vote_player)



#Раздавать роли только те, которые включены в игру