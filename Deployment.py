import requests
import json
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Showinterface import show_interface
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
      "cmd": "conf t",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "int eth 1/1",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "bandwidth 500000",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "mtu 9216",
      "version": 1
    },
    "id": 4
  }
]

print("Here is your Current MTU and Bandwidth Details")
show_interface()

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
print(response)

print("Your Mtu and Bandwidth has been updated!!")
show_interface()
