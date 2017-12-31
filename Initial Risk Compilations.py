from random import randint


''' this projct assumes several global variables:
game
a list of players which are instances of the player class
all the countries countries
some other stuff
'''


class Country(object):
    ''' a class for defining the property of adjacency for each country'''

    def __init__(self, country_number, adjacent_countries, continent_number, owner, number_of_men):
        self.country_number = country_number
        self.continent_number = continent_number
        self.adjacent_countries = adjacent_countries  # a list of the adjacent country numbers
        self.number_of_men = number_of_men
        self.owner = owner

# let's assume that right here we creat a list of all the possible countries after we make each of them an instance of the country class


Alaska = Country(201, [104, 202, 204], 2)
Northwest_Territories = Country(202, [203, 205, 201], 2)
Greenland = Country(203, [202, 205, 206], 2)
Alberta = Country(204, [201, 202, 205, 207], 2)
Ontario = Country(206, [202, 203, 204, 206, 208], 2)


# let's change our plan again and make a list for the initial_distribution

[[101, None, 0, [102, 105, 106, 303]],
 [102, None, 0, [101, 106, 107, 108, 103]],
 [103, None, 0, [102, 108, 104]],
 [104, None, 0, [103, 108, 107, 109, 201]],
 [105, None, 0, [101, 106, 111, 110, 303]],
 [106, None, 0, [101, 102, 107, 105, 111, 112]],
 [107, None, 0, [102, 108, 104, 109, 106]],
 [108, None, 0, [102, 103, 104, 107]],
 [109, None, 0, [104, 107]],
 [110, None, 0, [105, 111, 303, 307, 402]],
 [111, None, 0, [110, 105, 106, 112]],
 [112, None, 0, [111, 106, 601]],
 [201, None, 0, [104, 202, 204]],
 [202, None, 0, [201, 203, 204, 205]],
 [203, None, 0, [202, 205, 206, 301]],
 [204, None, 0, [201, 202, 205, 207]],
 [205, None, 0, [202, 203, 204, 206, 207, 208]],
 [206, None, 0, [205, 203, 208]],
 [207, None, 0, [204, 205, 208, 209]],
 [208, None, 0, [207, 205, 206, 209]],
 [209, None, 0, [207, 208, 501]],
 [301, None, 0, [203, 302, 304]],
 [302, None, 0, [301, 303, 304, 305]],
 [303, None, 0, [302, 305, 307, 101, 105, 110]],
 [304, None, 0, [301, 302, 305, 306]],
 [305, None, 0, [302, 303, 304, 306, 307]],
 [306, None, 0, [304, 305, 307, 401]],
 [307, None, 0, [306, 305, 303, 110, 401, 402]],
 [401, None, 0, [306, 307, 402, 403, 404, 503]],
 [402, None, 0, [307, 110, 401, 404]],
 [403, None, 0, [401, 404, 405]],
 [404, None, 0, [401, 402, 403, 405, 406]],
 [405, None, 0, [403, 404, 406]],
 [406, None, 0, [405, 404]],
 [501, None, 0, [209, 502, 503]],
 [502, None, 0, [501, 503, 504]],
 [503, None, 0, [501, 502, 504, 401]],
 [504, None, 0, [502, 503]],
 [601, None, 0, [112, 602, 603]],
 [602, None, 0, [601, 603, 604]],
 [603, None, 0, [601, 602, 604]],
 [604, None, 0, [602, 603]]
 ]


class Player(object):
    '''This class defines everything which someone would like to know about a player.'''

    def __init__(self, color, risk_cards=[], board_distribution=[]):
        self.board_distribution = board_distribution  # form of a list of sublists where each sublists is ['country','player','number_of_men', [adjacents]]
        self.color = color
        self.risk_cards = risk_cards

    def add_men_to_country(self, country, number_of_men):
        for sublist in self.board_distribution:
            if country in sublist:
                sublist[2] += number_of_men
                break

    def remove_men_from_country(self, country, number_of_men):
        for sublist in self.board_distribution:
            if country in sublist:
                sublist[2] -= number_of_men
                break

    def move_men(self, country_from, country_to, number_of_men):
        self.remove_men_from_country(country_from, number_of_men)
        self.add_men_to_country(country_to, number_of_men)

    def one_attack(country_from, country_to, number_of_men):
        attacker_country_stats = game.get_country_stats(country_from)  # this assumes that the center item of the distribution lists is a instatnce not a string
        defender_country_stats = game.get_country_stats(country_to)
        attacker = attacker_country_stats[1]
        defender = defender_country_stats[1]
        if number_of_men >= 3 and attacker_country_stats[2] >= number_of_men + 1:
            die_1 = randint(1, 6)
            die_2 = randint(1, 6)
            die_3 = randint(1, 6)
            list_of_attackers_dice = [die_3, die_2, die_1]
            list_of_attackers_dice.sort()

            if defender_country_stats[2] >= 2:
                defender_die_1 = randint(1, 6)
                defender_die_2 = randint(1, 6)
                list_of_defenders_dice = [defender_die_1, defender_die_2]
                list_of_defenders_dice.sort()
                if list_of_defenders_dice[1] >= list_of_attackers_dice[2]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)
                if list_of_defenders_dice[0] >= list_of_attackers_dice[1]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)

            else:
                defender_die = randint(1, 6)
                if defender_die >= list_of_attackers_dice[2]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)
        if number_of_men == 2 and attacker_country_stats[2] > 2:
            die_1 = randint(1, 6)
            die_2 = randint(1, 6)
            list_of_attackers_dice = [die_2, die_1]
            list_of_attackers_dice.sort()

            if defender_country_stats[2] >= 2:
                defender_die_1 = randint(1, 6)
                defender_die_2 = randint(1, 6)
                list_of_defenders_dice = [defender_die_1, defender_die_2]
                list_of_defenders_dice.sort()
                if list_of_defenders_dice[1] >= list_of_attackers_dice[1]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)
                if list_of_defenders_dice[0] >= list_of_attackers_dice[0]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)

            else:
                defender_die = randint(1, 6)
                if defender_die >= list_of_attackers_dice[1]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)

        if number_of_men == 1 and attacker_country_stats[2] > 1:
            die_1 = randint(1, 6)

            if defender_country_stats[2] >= 2:
                defender_die_1 = randint(1, 6)
                defender_die_2 = randint(1, 6)
                list_of_defenders_dice = [defender_die_1, defender_die_2]
                list_of_defenders_dice.sort()
                if list_of_defenders_dice[1] >= die_1:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)

            else:
                defender_die = randint(1, 6)
                if defender_die >= list_of_attackers_dice[1]:
                    attacker.remove_men_from_country(country_from, 1)
                else:
                    defender.remove_men_from_country(country_to, 1)

        else:
            print("Did you try to attack with as many or more men than were on your attacking country to begin wtih?")

        def attack_decision(self, stuff):
            ''' have this function go through all the adjacent peices and create a number for the value of each attack'''
            pass

        def keep_attacking_decision(self, stuff):
            '''have this function decide wether to keep attacking'''
            pass

        def attack_phase(self, stuff):
            self.adjacent_territory


class Game(object):
    def __init__(self, board_distribution=[]):
        self.board_distribution = board_distribution

    def get_country_stats(self, country):
        ''' returns the sublist in the board_distribution of a given country'''
        for sublist in self.board_distribution:
            if country in sublist:
                return sublist
                break

    def
