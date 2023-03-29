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
      "cmd": "bandwidth 100000",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "mtu 1500",
      "version": 1
    },
    "id": 4
  }
]


response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()


print('Your MTU and Bandwidth RollBacked Successfull!!!')
show_interface()