import requests


class SupCompare:
    def __init__(self, token):
        self.token = token

    def get_powerstats_by_name(self, heroes_list):
        powerstats_dict = {}
        for hero in heroes_list:
            resp = requests.get(f'https://superheroapi.com/api/{self.token}/search/{hero}')
            resp = resp.json()
            for elem in resp['results']:
                if elem['name'] == hero:
                    powerstats_dict[hero] = elem['powerstats']
        return powerstats_dict

    def compare_heroes(self, heroes_list, powerstat):
        powerstats_dict = self.get_powerstats_by_name(heroes_list)
        max_powerstat = 0
        for hero in heroes_list:
            if int(powerstats_dict[hero][powerstat]) > max_powerstat:
                max_powerstat = int(powerstats_dict[hero][powerstat])
        print(f'The most {powerstat} with {max_powerstat} marks:')
        for hero, powerstats in powerstats_dict.items():
            if int(powerstats[powerstat]) == max_powerstat:
                print(hero)


TOKEN = 2619421814940190
heroes = ['Hulk', 'Captain America', 'Thanos']
supcompare = SupCompare(TOKEN)
supcompare.compare_heroes(heroes, 'intelligence')
