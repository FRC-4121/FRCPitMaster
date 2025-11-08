##################################################################
#                                                                #
#                    TBA Match Info Class                        #
#                                                                #
#  This class provides methods for connecting to and retrieving  #
#  match information from The Blue Alliance servers.             #
#                                                                #
#  Author:  Timothy A. Fuller                                    #
#  Date:  10/20/2025                                             #
#                                                                #
#  Version:  1.0.0                                               #
#                                                                #
#  Revision Date:  10/20/2025                                    #
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


# --- Define the Match Info Class ---
class MatchInfo():

    # Initialize the class
    def __init__(self, tbahost="", apikey="", teamkey="", eventkey=""):

        # Initialize class variables
        self.tba_host = tbahost
        self.api_key = apikey
        self.team_key = teamkey
        self.event_key = eventkey
        self.modified_since = ""
        self.match_list = {}

        # Set api configuration
        self.configuration = tbaapiv3client.Configuration(
            host = self.tba_host,
            api_key = {
                'X-TBA-Auth-Key': self.api_key
            }
        )
    
    # Define the method to get event matches for a team
    def get_event_match_list(self):

        # Initialize local variables
        api_response = ""
        response_good = False

        # Connect to the TBA servers and request match info
        with tbaapiv3client.ApiClient(self.configuration) as api_client:

            # Create ab instance of the TBA Api class
            api_instance = tbaapiv3client.TBAApi(api_client)

            # Call method from API
            try:
                api_response = api_instance.get_team_event_matches(self.team_key, self.event_key, if_modified_since=self.modified_since)
                response_good = True
            except ApiException as e:
                print("Exception when calling TBAApi->get_team_event_matches: %s\n" % e)

        # Process the returned data if no errors
        if response_good:

            # Determine the number of matches
            num_matches = len(api_response)

            # Loop over all matches and create dictionary
            for num in range(num_matches):

                # Create local variables
                alliance = ''

                # Create a dictionary to hold match details
                match_dict = {}

                # Get information for next match
                match = api_response[num]

                # Retrieve basic match info and put in dictionary
                match_dict['Match Type'] = match.comp_level
                match_dict['Match No.'] = match.match_number

                # Retrieve blue alliance info
                blue_alliance = match.alliances.blue
                blue_alliance_teams = blue_alliance.team_keys
                i = 1
                for team in blue_alliance_teams:
                    key = 'Blue ' + str(i)
                    match_dict[key] = team
                    if team == self.team_key:
                        alliance = 'Blue'
                    i+=1
                
                # Retrieve red alliance info
                red_alliance = match.alliances.red
                red_alliance_teams = red_alliance.team_keys
                i = 1
                for team in red_alliance_teams:
                    key = 'Red ' +str(i)
                    match_dict[key] = team
                    if team == self.team_key:
                        alliance = 'Red'
                    i+=1

                match_dict["Alliance"] = alliance

                # Add match to the master dictionary
                match_key = 'match' + str(num)
                self.match_list[match_key] = match_dict

        # Return the match list
        return self.match_list
  





