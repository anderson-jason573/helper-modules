"""
*******************************************************************************
This module is the API call to Orchestrator, which retrieves general
information on each appliance.
*******************************************************************************
"""

from apicalls import ApiMethods
import json

class ApplianceInfo:

    @classmethod
    def get_appliances(cls, obj):

        """ This method takes the OrchHelper object, which is passed
        to it, and passes both the object and appropriate url for the api
        call, to the 'GET' method in apicalls.py """

        r = ApiMethods.get("/appliance", obj)
        if r.status_code == 200:
            return r.json()
        else:
            print("{0}: unable to get appliance list: {1}".format(obj.url, r.text))
            return []
