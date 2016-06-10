"""To fetch and store player types in db."""

import grequests

from django.core.management.base import BaseCommand

from players.models import PlayerDetails
from players.helpers import save_player_type_details

MAX_REQUESTS = 200


class Command(BaseCommand):
    """To search through TLG player profiles and store all types in db."""

    args = ''
    help = 'to search through TLG player profiles and store all types in db'

    def handle(self, *args, **options):
        """Handle only Telangana players here."""
        tlg_players = PlayerDetails.objects.filter(region='Telangana', skill_index__gte=70000)
        player_ids = [x.player_id for x in tlg_players]
        max_index = len(player_ids) - 1

        current_index = 0
        while current_index + MAX_REQUESTS < max_index:
            req_list = []
            for pid in player_ids[current_index:current_index + MAX_REQUESTS]:
                req_list.append(grequests.get('http://www.hitwicket.com/player/show/' + str(pid)))
            print "sending requests for requests between index: {} and index: {}".format(
                current_index, current_index + MAX_REQUESTS
            )
            responses = grequests.map(req_list)
            save_player_type_details(
                responses,
                player_ids[current_index:current_index + MAX_REQUESTS],
                skill_index_list[current_index:current_index + MAX_REQUESTS]
            )
            current_index += MAX_REQUESTS

        # end the other players in list also
        if current_index < max_index:
            req_list = []
            for pid in player_ids[current_index:max_index]:
                req_list.append(grequests.get('http://www.hitwicket.com/player/show/' + str(pid)))
            print "Final request batch..."
            responses = grequests.map(req_list)
            save_player_type_details(
                responses,
                player_ids[current_index:max_index]
            )
