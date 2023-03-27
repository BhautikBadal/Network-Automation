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
    "cmd": "ping 8.8.8.8 vrf management",
    "version": 1
    },
      "id": 2
    },
    {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
    "cmd": "ping 10.10.10.2 packet-size 2000 vrf wan",
    "version": 1
    },
      "id": 3
    }

]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()

for response in response:
    if '100.00% packet loss' in response['result']['msg']:
        if response['id'] == 1:
            print("Your LAN  connection is Down")
            # raise Exception('Packet loss detected for id ')
        if response['id'] == 2:
            print("Your WAN is connected..")
            # raise Exception('Packet loss detected for id {}: {}'.format(response['id'], response['result']['msg']))
        if response['id'] == 3:
            print("MTU packet Droped")
            # raise Exception('Packet loss detected for id {}: {}'.format(response['id'], response['result']['msg']))
 

    else:
        if response['id'] == 1:
            print("LAN is connected..")
        if response['id'] == 2:
            print("WAN is connected..")
        if response['id'] == 3:
            print("MTU packet has been sent!!")

