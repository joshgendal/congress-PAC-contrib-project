import os, json, requests
from django.conf import settings
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"

"""
A function to get US State Code List

Reads json file, packs state codes into list and returns it
"""
def get_state_code_list():
  state_codes = []
  data = open(os.path.join(settings.BASE_DIR, 'congress_app/static/state_code_data.json'))
  data1 = json.load(data)
  for i in data1:
    state_codes.append(i["Code"])
  data.close()
  return state_codes
  
def get_cid_list(codes):
  cid_list = []
  for code in codes:
    r = requests.get(f"{getLegislatorsURL}&id={code}&apikey={openSecretsAPIKey}&output=json")
    for i in r.json()["response"]["legislator"]:
      if isinstance(i, dict):
        cid_list.append(i["@attributes"]["cid"])
        print(len(cid_list))
  return cid_list