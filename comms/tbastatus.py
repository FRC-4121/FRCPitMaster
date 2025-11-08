##################################################################
#                                                                #
#                       TBA Status Class                         #
#                                                                #
#  This class provides methods for connecting to and retrieving  #
#  status information from The Blue Alliance servers.            #
#                                                                #
#  Author:  Timothy A. Fuller                                    #
#  Date:  9/28/2025                                              #
#                                                                #
#  Version:  1.0.0                                               #
#                                                                #
#  Revision Date:  9/28/2025                                     #
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


#-- Define the TbaInterface class --
class TbaStatus():

    # Initialize the class
    def __init__(self, tbahost="", apikey=""):
        
        # Initialize class variables
        self.tba_host = tbahost
        self.api_key = apikey
        self.modified_since = ""

        # Set api configuration
        self.configuration = tbaapiv3client.Configuration(
            host = self.tba_host,
            api_key = {
                'X-TBA-Auth-Key': self.api_key
            }
        )

    # Define TBA status method
    def get_status(self):

        # Initialize local variables
        status = None

        # Connect to the TBA servers and request status info
        with tbaapiv3client.ApiClient(self.configuration) as api_client:

            # Create ab instance of the TBA Api class
            api_instance = tbaapiv3client.TBAApi(api_client)