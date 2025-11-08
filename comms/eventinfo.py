##################################################################
#                                                                #
#                    TBA Event Info Class                        #
#                                                                #
#  This class provides methods for connecting to and retrieving  #
#  event information from The Blue Alliance servers.             #
#                                                                #
#  Author:  Timothy A. Fuller                                    #
#  Date:  10/27/2025                                             #
#                                                                #
#  Version:  1.0.0                                               #
#                                                                #
#  Revision Date:  10/27/2025                                    #
#                                                                #
##################################################################

# System module imports
import sys
import os

# Python imports
import pandas as pd

# TBA imports
import tbaapiv3client
from tbaapiv3client.rest import ApiException


# -- Define the Event Info Class --
class EventInfo():

    # Initialize the class
    def __init__(self, tbahost="", apikey="", teamkey="", eventkey=""):

        # Initialize class variables
        self.tba_host = tbahost
        self.api_key = apikey
        self.team_key = teamkey
        self.event_key = eventkey
        self.modified_since = ""

        # Set api configuration
        self.configuration = tbaapiv3client.Configuration(
            host = self.tba_host,
            api_key = {
                'X-TBA-Auth-Key': self.api_key
            }
        )

    # Define the method to get event playoff alliances
    def get_playoff_alliances(self):

        # Initialize local variables
        api_response = ""
        response_good = False
        playoff_list = {}

        # Connect to the TBA servers and request match info
        with tbaapiv3client.ApiClient(self.configuration) as api_client:

            # Create ab instance of the TBA Api class
            api_instance = tbaapiv3client.EventApi(api_client)

            # Call method from API
            try:
                api_response = api_instance.get_event_alliances(self.event_key, if_modified_since=self.modified_since)
                response_good = True
            except ApiException as e:
                print("Exception when calling TBAApi->get_team_event_matches: %s\n" % e)

        # Process the returned data if no errors
        if response_good:

            # Determine the number of matches
            num_alliances = len(api_response)

            # Loop over all alliances and create dictionary
            for num in range(num_alliances):

                # Create a dictionary to hold alliance details
                team_dict = {}

                # Get information for next alliance
                alliance = api_response[num]

                # Get teams on this alliance
                picks = alliance.picks
                i = 1
                for team in picks:
                    key = 'Team ' + str(i)
                    team_dict[key] = team
                    i += 1

                # Add alliance to master dictionary
                playoff_list[num] = team_dict

        # Return the playoff dictionary
        return playoff_list



