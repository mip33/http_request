import requests
from datetime import timedelta
from datetime import datetime

def search_tag(days, tag):

    final_date = int(datetime.timestamp(datetime.now()))
    initial_date = final_date - days * 86400

    PARAMS = {
        'previous_day': initial_date,
        'the_next_day': final_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    response = requests.get('https://api.stackexchange.com/2.2/questions', params=PARAMS)
    for question in response.json().get('items'):
        print("все запросы, которые за последние 2 дня содержaт тэг 'Python': " + str(question['tags']), '\n')

search_tag(2, 'python')