import requests
import json
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def show_interface():
    switchuser='admin'
    switchpassword='Lock&Key()19'
    url='https://172.26.21.101/ins'
    myheaders={'content-type':'application/json-rpc'}
    payload=[      {        "jsonrpc": "2.0",        "method": "cli",        "params": {          "cmd": "show int eth 1/1",          "version": 1        },        "id": 1      }    ]

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
    # print(response)

    eth_mtu = response["result"]["body"]["TABLE_interface"]["ROW_interface"]["eth_mtu"]
    eth_bw = response["result"]["body"]["TABLE_interface"]["ROW_interface"]["eth_bw"]

    print("Current Mtu is:", eth_mtu)
    print("Current Bandwidth is:", eth_bw)

# show_interface()
