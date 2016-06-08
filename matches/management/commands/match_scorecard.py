"""To fetch scorecard details about all matches in HW."""

import grequests

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """To fetch scorecard details about all matches in HW."""

    args = ''
    help = 'To fetch scorecard details about all matches in HW.'

    def send_req_save_file(self, first, last):
        req_list = []
        match_details_url = "http://hitwicket.com/match/show/{}?details=1"
        for match_id in xrange(first, last):
            req_list.append(grequests.get(match_details_url.format(match_id), timeout=30))

        print "sending requests for matches between {} and {}...".format(first, last)
        resp_list = grequests.map(req_list)
        print "saving results to files... "

        ctr = first
        for resp in resp_list:
            if resp and resp.status_code < 400:
                with open('extras/matches/' + str(ctr), 'w') as match_file:
                    match_file.write(resp.content)
            ctr += 1

    def handle(self, *args, **options):
        # initial_match_id = 1  # initial match for which data will be taken
        # max_match_id = 13000000  # max match_id until which the requests will be sent
        initial_match_id = 202001
        max_match_id = 12000000
        max_requests = 500  # no of requests to be fired at a time

        current_max = initial_match_id + max_requests
        while current_max <= max_match_id:
            self.send_req_save_file(initial_match_id, current_max)
            initial_match_id = current_max
            current_max += max_requests
