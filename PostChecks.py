import requests
import json
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
switchuser='admin'
switchpassword='Lock&Key()19'
url='https://172.26.21.101/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
    {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
    "cmd": "ping 10.10.0.2 vrf wan",
    "version": 1
    },
      "id": 1
    },
    {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
    "cmd": "ping 10.10.10.2 vrf wan",
    "version": 1
    },
      "id": 2
    }

]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()

for response in response:
    if '100.00% packet loss' in response['result']['msg']:
        if response['id'] == 1:
            print("Your LAN  connection is Down...")
            #raise Exception('Your LAN  connection is Down!!! Contacting Administration...')
        if response['id'] == 2:
            print("Your WAN  connection is down...")
            #raise Exception('Your WAN  connection is down!!! Contacting Administration...')       
    else:
        if response['id'] == 1:
            print("LAN is connected..")
        if response['id'] == 2:
            print("WAN is connected..")
       
