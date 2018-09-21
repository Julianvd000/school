import requests
import xmltodict


auth_details = ('Julian@kruijdijk.nl', 'Sc3aFyDjwj2tbYc3prIRL4Z-2828dQvQqc898R7cV88ee2Pch4UN0Q')

def getTrains():
    inputStation = input('Geef station op: ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + inputStation
    response = requests.get(api_url, auth=auth_details)
    return xmltodict.parse(response.text)

vertrekXML = getTrains()
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36
    treinSoort = vertrek['TreinSoort']
    vertrekSpoor = vertrek['VertrekSpoor']
    volgendeStations = vertrek['RouteTekst']
    print(
        'Om '
        + vertrektijd +
        ' vertrekt een trein naar '
        + eindbestemming +
        ' de trein is een '
        + treinSoort +
        ' het vertrekspoor is '
        + vertrekSpoor +
        ' en de volgende stations zijn '
        + volgendeStations 
    )
class TrainStation:
    def __init__(Station):
