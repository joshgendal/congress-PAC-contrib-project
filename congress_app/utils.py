import os, json, requests
from django.conf import settings
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"
candidate_summary_url = "https://www.opensecrets.org/api/?method=candSummary"

"""
A function to get US State Code List

Reads json file, packs state codes into list and returns it
"""
def get_state_code_list():
  print('GETTING STATE CODES')
  state_codes = []
  data = open(os.path.join(settings.BASE_DIR, 'congress_app/static/state_code_data.json'))
  data1 = json.load(data)
  for i in data1:
    state_codes.append(i["Code"])
  data.close()
  return state_codes
  
def get_cid_list(codes):
  print('GETTING CID LIST')
  cid_list = []
  for code in codes:
    r = requests.get(f"{getLegislatorsURL}&id={code}&apikey={openSecretsAPIKey}&output=json")
    for i in r.json()["response"]["legislator"]:
      if isinstance(i, dict):
        cid_list.append(i["@attributes"]["cid"])
  print('FINISHED CID LIST')
  return cid_list

def get_candidate_summaries(cids):
  print('GETTING CANDIDATE SUMMARY')
  data = []
  # r = requests.get(f"{candidate_summary_url}&cid={i}apikey={openSecretsAPIKey}&output=json")
  for i in cids:
    r = requests.get(f"{candidate_summary_url}&cid={i}&apikey={openSecretsAPIKey}&output=json")
    if r.status_code == 200:
      attributes = r.json()["response"]["summary"]["@attributes"]
      data.append(attributes)
      print(len(data))
      # print("================================================================")
  print('FINISHED CANDIDATE SUMMARY')
  return data
