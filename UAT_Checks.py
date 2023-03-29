import requests
import json
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from Showinterface import show_interface
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
    "cmd": "ping 10.10.10.2 packet-size 2000 vrf wan",
    "version": 1
    },
      "id": 1
    }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()


if '100.00% packet loss' in response['result']['msg']:
    print("MTU packet Droped")
else:
    print("MTU packet has been sent!!")

print("Here is your Current MTU and Bandwidth Details")
show_interface()