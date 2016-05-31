import grequests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from players.helpers import save_player_details

NO_OF_REQUESTS = 2000

class Command(BaseCommand):
    args = ''
    help = 'to search through player profiles and store all in db'

    def handle(self, *args, **options):
        default_start = 9027387
        default_end = 13000000

        player_url = "http://hitwicket.com/player/show/"
        with open('extras/indexed_till.txt', 'r') as rf:
            try:
                id_indexed = int(rf.read())
                if id_indexed == 0 or not id_indexed:
                    id_indexed = default_start
            except:
                id_indexed = default_start

        # start the indexing from start to end index, NO_OF_REQUESTS requests per firing
        current_start = default_start
        current_end = default_start + NO_OF_REQUESTS
        while current_end < default_end:
            print "inside loop... current_start: {} current_end: {}".format(current_start, current_end)
            req_list = []
            for player_id in xrange(current_start, current_end):
                current_req = grequests.get(player_url + str(player_id))
                req_list.append(current_req)

            print "requests are being sent now.. please wait..."
            responses = grequests.map(req_list)
            print "got responses!"

            ctr = current_start
            for resp in responses:
                try:
                    if resp.status_code == 200:
                        save_player_details(resp.content, ctr)
                except:
                    continue
                ctr += 1

            with open('extras/indexed_till.txt', 'w') as wf:
                wf.write(str(current_end))

            current_start = current_end
            current_end += NO_OF_REQUESTS
