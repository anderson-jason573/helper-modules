import requests

class ApiMethods:

    @classmethod
    def post(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        data = {"user": obj.user, "password": obj.password, "loginType": obj.supportedAuthModes.index(obj.authMode)}
        return obj.session.post(obj.url_prefix + url + apiSrcStr, json=data, verify=False, timeout=120,
                                 headers=obj.headers)

    @classmethod
    def get(self, url):
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.get(self.url_prefix + url + apiSrcStr, verify=False, timeout=120, headers=self.headers)

    @classmethod
    def delete(self, url):
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.delete(self.url_prefix + url + apiSrcStr, verify=False, timeout=120, headers=self.headers)

    @classmethod
    def put(self, url, data):
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.put(self.url_prefix + url + apiSrcStr, json=data, verify=False, timeout=120,
                                headers=self.headers)
