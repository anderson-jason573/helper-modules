"""
************************************************************************************
This script reuests general information on each appliance from 
the Orchestrator.
************************************************************************************
"""

import requests
import json
from login import OrchHelper #OrchHelper class from login.py
from appliancinfo import ApplianceInfo #ApplianceInfo class from appliancinfo.py  *Need to fix spelling error.

# User input for needed variables
url = input("OrchIP: ")
user = input("UserId: ")
pwd = input("Password: ")

o = OrchHelper(url, user, pwd) # Create OrchHelper object
o.login() # Call login method on OrchHelper object

# for MFA login:
#    o.send_mfa()
#    mfa = input("Enter MFA code: ")
#    o.mfa_login(mfa)

appliances = ApplianceInfo.get_appliances(o) # Pass OrchHelper object to get_appliances method in appliancinfo.py
print(json.dumps(appliances, indent=4))

o.logout()
