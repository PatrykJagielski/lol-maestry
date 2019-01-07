from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import requests

ids = ['266',
       '103',
       '84',
       '12',
       '32',
       '34',
       '1',
       '22',
       '136',
       '268',
       '432',
       '53',
       '63',
       '201',
       '51',
       '164',
       '69',
       '31',
       '42',
       '122',
       '131',
       '119',
       '36',
       '245',
       '60',
       '28',
       '81',
       '9',
       '114',
       '105',
       '3',
       '41',
       '86',
       '150',
       '79',
       '104',
       '120',
       '74',
       '420',
       '39',
       '427',
       '40',
       '59',
       '24',
       '126',
       '202',
       '222',
       '145',
       '429',
       '43',
       '30',
       '38',
       '55',
       '10',
       '141',
       '85',
       '121',
       '203',
       '240',
       '96',
       '7',
       '64',
       '89',
       '127',
       '236',
       '117',
       '99',
       '54',
       '90',
       '57',
       '11',
       '21',
       '62',
       '82',
       '25',
       '267',
       '75',
       '111',
       '518',
       '76',
       '56',
       '20',
       '2',
       '61',
       '516',
       '80',
       '78',
       '555',
       '133',
       '497',
       '33',
       '421',
       '58',
       '107',
       '92',
       '68',
       '13',
       '113',
       '35',
       '98',
       '102',
       '27',
       '14',
       '15',
       '72',
       '37',
       '16',
       '50',
       '134',
       '223',
       '163',
       '91',
       '44',
       '17',
       '412',
       '18',
       '48',
       '23',
       '4',
       '29',
       '77',
       '6',
       '110',
       '67',
       '45',
       '161',
       '254',
       '112',
       '8',
       '106',
       '19',
       '498',
       '101',
       '5',
       '157',
       '83',
       '154',
       '238',
       '115',
       '26',
       '142',
       '143']

champions = {'Aatrox': '266',
             'Ahri': '103',
             'Akali': '84',
             'Alistar': '12',
             'Amumu': '32',
             'Anivia': '34',
             'Annie': '1',
             'Ashe': '22',
             'AurelionSol': '136',
             'Azir': '268',
             'Bard': '432',
             'Blitzcrank': '53',
             'Brand': '63',
             'Braum': '201',
             'Caitlyn': '51',
             'Camille': '164',
             'Cassiopeia': '69',
             'Chogath': '31',
             'Corki': '42',
             'Darius': '122',
             'Diana': '131',
             'Draven': '119',
             'DrMundo': '36',
             'Ekko': '245',
             'Elise': '60',
             'Evelynn': '28',
             'Ezreal': '81',
             'Fiddlesticks': '9',
             'Fiora': '114',
             'Fizz': '105',
             'Galio': '3',
             'Gangplank': '41',
             'Garen': '86',
             'Gnar': '150',
             'Gragas': '79',
             'Graves': '104',
             'Hecarim': '120',
             'Heimerdinger': '74',
             'Illaoi': '420',
             'Irelia': '39',
             'Ivern': '427',
             'Janna': '40',
             'JarvanIV': '59',
             'Jax': '24',
             'Jayce': '126',
             'Jhin': '202',
             'Jinx': '222',
             'Kaisa': '145',
             'Kalista': '429',
             'Karma': '43',
             'Karthus': '30',
             'Kassadin': '38',
             'Katarina': '55',
             'Kayle': '10',
             'Kayn': '141',
             'Kennen': '85',
             'Khazix': '121',
             'Kindred': '203',
             'Kled': '240',
             'KogMaw': '96',
             'Leblanc': '7',
             'LeeSin': '64',
             'Leona': '89',
             'Lissandra': '127',
             'Lucian': '236',
             'Lulu': '117',
             'Lux': '99',
             'Malphite': '54',
             'Malzahar': '90',
             'Maokai': '57',
             'MasterYi': '11',
             'MissFortune': '21',
             'MonkeyKing': '62',
             'Mordekaiser': '82',
             'Morgana': '25',
             'Nami': '267',
             'Nasus': '75',
             'Nautilus': '111',
             'Neeko': '518',
             'Nidalee': '76',
             'Nocturne': '56',
             'Nunu': '20',
             'Olaf': '2',
             'Orianna': '61',
             'Ornn': '516',
             'Pantheon': '80',
             'Poppy': '78',
             'Pyke': '555',
             'Quinn': '133',
             'Rakan': '497',
             'Rammus': '33',
             'RekSai': '421',
             'Renekton': '58',
             'Rengar': '107',
             'Riven': '92',
             'Rumble': '68',
             'Ryze': '13',
             'Sejuani': '113',
             'Shaco': '35',
             'Shen': '98',
             'Shyvana': '102',
             'Singed': '27',
             'Sion': '14',
             'Sivir': '15',
             'Skarner': '72',
             'Sona': '37',
             'Soraka': '16',
             'Swain': '50',
             'Syndra': '134',
             'TahmKench': '223',
             'Taliyah': '163',
             'Talon': '91',
             'Taric': '44',
             'Teemo': '17',
             'Thresh': '412',
             'Tristana': '18',
             'Trundle': '48',
             'Tryndamere': '23',
             'TwistedFate': '4',
             'Twitch': '29',
             'Udyr': '77',
             'Urgot': '6',
             'Varus': '110',
             'Vayne': '67',
             'Veigar': '45',
             'Velkoz': '161',
             'Vi': '254',
             'Viktor': '112',
             'Vladimir': '8',
             'Volibear': '106',
             'Warwick': '19',
             'Xayah': '498',
             'Xerath': '101',
             'XinZhao': '5',
             'Yasuo': '157',
             'Yorick': '83',
             'Zac': '154',
             'Zed': '238',
             'Ziggs': '115',
             'Zilean': '26',
             'Zoe': '142',
             'Zyra': '143'}

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

API_KEY = "RGAPI-52b59041-06ff-4882-9e4a-d5a431b7182d"


class Summoner(Resource):
    # @cross_origin()
    def get(self, nick,server):
        response = requests.get(
            'https://'+server+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + nick + '?api_key=' + API_KEY)
        id = response.json()['id']

        response = requests.get(
            'https://'+server+'.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + id + '?api_key=' + API_KEY)

        played = [] #champions ids
        not_played = []
        summary_points = 0
        champion_points = []
        champion_levels = []
        chest_granted = [] #boolean
        champion_points_since_last_level = []
        champion_points_until_next_level = []

        for i in response.json():
            played.append(str(i["championId"]))
            champion_points.append(i["championPoints"])
            chest_granted.append(i["chestGranted"])
            champion_levels.append(i["championLevel"])
            champion_points_since_last_level.append(i["championPointsSinceLastLevel"])
            champion_points_until_next_level.append(i["championPointsUntilNextLevel"])
            summary_points += i["championPoints"]

        for i in ids:
            if (not i in played):
                not_played.append(i)

        rotation_champions = requests.get(
            'https://'+server+'.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + API_KEY).json().get(
            "freeChampionIds")
        rotation_champions_not_played = []
        rotation_champions_not_played_names = []
        for i in rotation_champions:
            if (str(i) in not_played):
                rotation_champions_not_played.append(str(i))

        not_played_champions = []
        for k, v in champions.items():
            if (v in not_played):
                not_played_champions.append(k)
            if (v in rotation_champions_not_played):
                rotation_champions_not_played_names.append(k)

        response = requests.get(
            'https://'+server+'.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + id + '?api_key=' + API_KEY)
        score = response.json()

        response = requests.get(
            'https://'+server+'.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + id + '?api_key=' + API_KEY)
        is_playing = False
        if (response.status_code == 200):
            is_playing = True

        return {
            "is_playing": is_playing,
            "not_played_count": len(not_played_champions),
            "id": id,
            "score": score,
            "real_score": score + len(not_played_champions),
            "champions": not_played_champions,
            "rotation_champions_not_played": rotation_champions_not_played_names,
            "summary_points": summary_points
        }


#
# class Rotation(Resource):
#     def get(self, name):
#         response = requests.get('https://+'srv'+.api.riotgames.com/lol/platform/v3/champion-rotations?api_key='+ API_KEY)
#         return response.json().get("freeChampionIds")


api.add_resource(Summoner, '/summoner/<string:server>/<string:nick>')
# api.add_resource(Rotation, '/rotation/<string:name>')


if __name__ == '__main__':
    app.run()
