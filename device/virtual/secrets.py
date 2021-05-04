OPEN_WEATHER_TOKEN = 'd9c3080b644e7fe28441413fdc7f24df' 
DEVICE_1_TOKEN = "A1_TEST_TOKEN"
DEVICE_2_TOKEN = "A2_TEST_TOKEN"
def getOpenWeatherToken():
    return OPEN_WEATHER_TOKEN

def getDeviceToken(id):
    return DEVICE_2_TOKEN

CITIES = [['V12mMG95NmrJ8Wu4asdf', 'Chieti'],
            ['TldN65VTzMukZnAasdf', 'Francavilla al Mare'],
            ['ssWgp3cschyZJf37aasd', 'L\'Aquila'],
            ['qZdNlOVhuMKf7fRasdd', 'Teramo']
        ]

NUM_CITIES = len(CITIES)
def getCities(id):
    return CITIES[id]