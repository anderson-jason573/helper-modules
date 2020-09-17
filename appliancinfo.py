class ApplianceInfo:

    @classmethod
    def get_appliances(self):
        # sample GET operation to retrieve list of appliances
        # JSON response is a list object
        r = self.get("/appliance")
        if r.status_code == 200:
            return r.json()
        else:
            print("{0}: unable to get appliance list: {1}".format(self.url, r.text))
            return []
