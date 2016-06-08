"""Helpers methods for player app."""

from bs4 import BeautifulSoup
import re
import requests

from models import PlayerDetails, DivTeamDetails


def save_player_details(html_content, player_id, team_id):
    """To save player details given the player_id."""
    soup = BeautifulSoup(html_content, 'html.parser')

    exp, form, fitness, _skill_index, _salary, region = [x.text for x in soup.find_all('div', class_='level')]
    skill_index = int(re.search(r'\S+', _skill_index).group().replace(',', ''))
    salary = int(_salary.replace(',', ''))

    try:
        if team_id:
            PlayerDetails.objects.get(player_id=player_id, team_id=team_id)
        else:
            PlayerDetails.objects.get(player_id=player_id)
    except:
        if team_id:
            PlayerDetails.objects.create(
                player_id=player_id,
                form=form,
                fitness=fitness,
                skill_index=skill_index,
                salary=salary,
                region=region,
                team_id=team_id
            )
        else:
            PlayerDetails.objects.create(
                player_id=player_id,
                form=form,
                fitness=fitness,
                skill_index=skill_index,
                salary=salary,
                region=region
            )


def save_div_team_details(league_team_ids, league_id, div_id):
    """Store div details and team relations to them."""
    # store the details in database
    try:
        new_objs = [DivTeamDetails(team_id=team_id, div_id=div_id, league_id=league_id) for team_id in league_team_ids]
        DivTeamDetails.objects.bulk_create(new_objs)
    except Exception as e:
        # to ignore errors (if any)
        # probably an object already exists?
        print "error occured while doing bulk update: ", e


def get_div_team_ids(div_id):
    """Take div_id and return the team ids in that div by going through each league.

    div 1 - 4 ^ 0 = 1
    div 2 - 4 ^ 1 = 4
    div 3 - 4 ^ 2 = 16
    div 4 - ...
    div 5 - ...
    div 6 - ...
    div 7 - ...
    div 8 - 4 ^ 7 = 16384
    """
    # accept only valid div ids
    div_id = int(div_id)
    if div_id not in range(1, 9):
        return "Wrong div id entered"

    # if it has been scraped already, just fetch teams from db
    if DivTeamDetails.objects.filter(div_id=div_id).exists():
        return [int(x[0]) for x in DivTeamDetails.objects.filter(div_id=div_id).values_list('team_id')]

    total_leagues = 4 ** (div_id - 1)
    league_url = "http://hitwicket.com/league/show/{}-{}"
    div_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII'}
    all_teams = []
    for league_id in xrange(1, total_leagues + 1):
        print "currently fetching teams from league: {}-{}".format(div_roman[div_id], league_id)
        current_league_url = league_url.format(div_roman[div_id], league_id)
        resp = requests.get(current_league_url)
        if resp.status_code == 200:
            league_soup = BeautifulSoup(resp.content, 'html.parser')
            league_team_ids = teamids_from_league(league_soup)

            # store the league_team_ids and league, div relns in db
            save_div_team_details(league_team_ids, league_id, div_id)

            all_teams += league_team_ids
        else:
            print "request to league url failed: ", current_league_url

    print "fetched all team id details for div ", div_id
    print all_teams

    # write to a file all the div team details
    try:
        print "writing to a new file... "
        div_teams_filename = 'extras/div-{}-teamids.txt'.format(div_id)
        with open(div_teams_filename, 'w') as div_file:
            div_file.write('\n'.join([str(team) for team in all_teams]))
        print "done writing to a file!"
    except Exception as e:
        # to ignore errors (if any)
        print "Error while writing to file: ", e

    return all_teams


def teamids_from_league(league_soup):
    """Get the team links from league html.

    Exclude bot teams.
    """
    all_links = []
    for team in league_soup.find_all('a', class_='teamname'):
        if 'bot_team_name' not in team.attrs['class']:
            all_links.append(team.attrs['href'])

    return [int(re.search(r'\/team\/show\/(\d+)\/.*', link).group(1)) for link in all_links]


def get_player_links_from_team(team_player_soup):
    """Get player links given team players response."""
    all_links = []
    for link in team_player_soup.findAll('a', attrs={'href': re.compile("^/player/show")}):
        current = link.get('href')
        all_links.append(current)
    return all_links
