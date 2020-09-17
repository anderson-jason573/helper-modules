import requests
import json
from login import OrchHelper
from appliancinfo import ApplianceInfo

url = input("OrchIP: ")
user = input("UserId: ")
pwd = input("Password: ")

o = OrchHelper(url, user, pwd)
o.login()

# for MFA login:
#    o.send_mfa()
#    mfa = input("Enter MFA code: ")
#    o.mfa_login(mfa)

appliances = ApplianceInfo.get_appliances(o) # Pass OrchHelper object to get_appliances method in appliancinfo.py
print(json.dumps(appliances, indent=4))

o.logout()
