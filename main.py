import requests
from login import OrchHelper

url = input("OrchIP: ")
user = input("UserId: ")
pwd = input("Password: ")
o = OrchHelper(url, user, pwd)

o.authMode = "local"  # not required as local is the default
o.login()

# for MFA login:
#    o.send_mfa()
#    mfa = input("Enter MFA code: ")
#    o.mfa_login(mfa)

appliances = o.get_appliances()
print("Total appliances: ", len(appliances))

o.logout()