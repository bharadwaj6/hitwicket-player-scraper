"""To fetch player details from a whole division."""

from bs4 import BeautifulSoup
import grequests
import re
import requests

from django.core.management.base import BaseCommand

from players.helpers import save_player_details, get_div_team_ids, get_player_links_from_team

NO_OF_REQUESTS = 2000
REQUEST_TIMEOUT = 30


class Command(BaseCommand):
    """To search through player profiles and store all in db."""

    args = ''
    help = 'to search through player profiles and store all in db'

    def handle(self, *args, **options):
        """The actual script."""
        # div_id = input("Enter the division you want to search in: ")
        rest_divs = [7, 8]
        for div_id in rest_divs:
            team_ids = get_div_team_ids(div_id)
            team_url = "http://hitwicket.com/players/index/"
            for team_id in team_ids:
                current_team_players_url = team_url + str(team_id)
                print "sending request to team players url: ", current_team_players_url

                team_resp = requests.get(current_team_players_url)
                if team_resp.status_code == 200:
                    players_html = team_resp.content
                    players_soup = BeautifulSoup(players_html, 'html.parser')
                    player_links = get_player_links_from_team(players_soup)

                    req_list = [grequests.get("http://hitwicket.com" + link) for link in player_links]
                    # store the corresponding player_id for each player link
                    player_ids = [int(re.search(r'\/player\/show\/(\d+)\/.*', link).group(1)) for link in player_links]
                    print "no of reqs: ", len(req_list)
                    print "sending requests for team: ", team_id
                    responses = grequests.map(req_list)
                    print "saving details of players..."

                    ctr = 0
                    for resp in responses:
                        if resp is not None and resp.status_code == 200:
                            save_player_details(resp.content, player_ids[ctr], team_id)
                        ctr += 1
