import requests

class ApiMethods:

    @classmethod
    def post(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        data = {"user": obj.user, "password": obj.password, "loginType": obj.supportedAuthModes.index(obj.authMode)}
        return obj.session.post(obj.url_prefix + url + apiSrcStr, json=data, verify=False, timeout=120,
                                 headers=obj.headers)

    @classmethod
    def get(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.get(obj.url_prefix + url + apiSrcStr, verify=False, timeout=120, headers=obj.headers)

    @classmethod
    def delete(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.delete(obj.url_prefix + url + apiSrcStr, verify=False, timeout=120, headers=obj.headers)

    @classmethod
    def put(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.put(obj.url_prefix + url + apiSrcStr, json=data, verify=False, timeout=120,
                                headers=obj.headers)

