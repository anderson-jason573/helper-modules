from apicalls import ApiMethods
import json

class ApplianceInfo:

    @classmethod
    def get_appliances(cls, obj):
        # sample GET operation to retrieve list of appliances
        # JSON response is a list object
        r = ApiMethods.get("/appliance", obj)
        if r.status_code == 200:
            return r.json()
        else:
            print("{0}: unable to get appliance list: {1}".format(obj.url, r.text))
            return []
