import re
from bs4 import BeautifulSoup

from models import PlayerDetails

def save_player_details(html_content, player_id):
    soup = BeautifulSoup(html_content, 'html.parser')

    exp, form, fitness, _skill_index, _salary, region = [x.text for x in soup.find_all('div', class_='level')]
    if region != "Telangana":
        return

    skill_index = int(re.search(r'\d*\,\d*', _skill_index).group().replace(',', ''))
    salary = int(_salary.replace(',', ''))

    try:
        player = PlayerDetails.objects.get(player_id=player_id)
    except:
        PlayerDetails.objects.create(
            player_id=player_id,
            form=form,
            fitness=fitness,
            skill_index=skill_index,
            salary=salary,
            region=region
        )
